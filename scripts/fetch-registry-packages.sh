#!/usr/bin/env bash
# Download the registry packages (npm, PyPI, NuGet) of a finished Bitbucket build from dl.pdfix.net,
# check that every package carries the expected version, and report what is already published.
#
# Usage:
#   scripts/fetch-registry-packages.sh <version> <branch> <commit> <out-dir>
#
#   version   X.Y.Z, same as pdfix/version.txt (e.g. 10.0.0)
#   branch    full pdfix branch name of the build (S3 folder), e.g. release/v10.0.0
#   commit    full 40-char pdfix commit of the build (S3 folder)
#   out-dir   one sub-folder per target: npm-sdk, npm-cli, pypi-sdk, pypi-cli, nuget
#
# Writes <out-dir>/status.md (Markdown table: package, registry, already published?).
# Publishes nothing. Needs: bash, curl, tar, unzip, python3.

set -euo pipefail

BASE_URL="https://dl.pdfix.net/builds/pdfix-sdk"
die() { echo "error: $*" >&2; exit 1; }

[[ $# -eq 4 ]] || die "usage: $0 <version> <branch> <commit> <out-dir>"
VERSION="$1" BRANCH="$2" COMMIT="$3" OUT="$4"
[[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || die "version must look like 10.0.0, got '$VERSION'"
[[ "$BRANCH" =~ ^[A-Za-z0-9._/-]+$ ]] || die "invalid branch '$BRANCH'"
[[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || die "commit must be the full 40-char lowercase SHA, got '$COMMIT'"
SRC_URL="${BASE_URL}/${BRANCH}/${COMMIT}"

# target folder | file in the build (S3)
FILES=(
  "npm-sdk|npm/pdfix-sdk-${VERSION}.tgz"
  "npm-cli|npm-cli/pdfix-cli-darwin-arm64-${VERSION}.tgz"
  "npm-cli|npm-cli/pdfix-cli-darwin-x64-${VERSION}.tgz"
  "npm-cli|npm-cli/pdfix-cli-linux-arm64-${VERSION}.tgz"
  "npm-cli|npm-cli/pdfix-cli-linux-x64-${VERSION}.tgz"
  "npm-cli|npm-cli/pdfix-cli-win32-x64-${VERSION}.tgz"
  "npm-cli|npm-cli/pdfix-cli-${VERSION}.tgz"
  "pypi-sdk|python/pdfix_sdk-${VERSION}-py3-none-any.whl"
  "pypi-sdk|python/pdfix_sdk-${VERSION}.tar.gz"
  "pypi-cli|pip-cli/pdfix_cli-${VERSION}-py3-none-macosx_10_13_x86_64.whl"
  "pypi-cli|pip-cli/pdfix_cli-${VERSION}-py3-none-macosx_11_0_arm64.whl"
  "pypi-cli|pip-cli/pdfix_cli-${VERSION}-py3-none-manylinux_2_17_aarch64.whl"
  "pypi-cli|pip-cli/pdfix_cli-${VERSION}-py3-none-manylinux_2_17_x86_64.whl"
  "pypi-cli|pip-cli/pdfix_cli-${VERSION}-py3-none-win_amd64.whl"
  "nuget|nuget/PDFix.SDK.${VERSION}.nupkg"
)

rm -rf "$OUT"
mkdir -p "$OUT"/{npm-sdk,npm-cli,pypi-sdk,pypi-cli,nuget}

# ---- download ---------------------------------------------------------------
echo "Source: ${SRC_URL}"
for entry in "${FILES[@]}"; do
  target="${entry%%|*}" rel="${entry#*|}"
  dest="${OUT}/${target}/$(basename "$rel")"
  echo "  download ${rel}"
  curl -fsSL --retry 3 --retry-delay 5 -o "$dest" "${SRC_URL}/${rel}" \
    || die "cannot download ${SRC_URL}/${rel} - wrong version/branch/commit, or the build is not finished?"
  [[ -s "$dest" ]] || die "downloaded file is empty: ${rel}"
done

# ---- check the version inside each package ----------------------------------
# npm: name + version from package/package.json; NuGet: id + version from the .nuspec.
NPM_NAMES=()
for f in "$OUT"/npm-sdk/*.tgz "$OUT"/npm-cli/*.tgz; do
  read -r name ver < <(tar -xzOf "$f" package/package.json \
    | python3 -I -c 'import sys,json; d=json.load(sys.stdin); print(d["name"], d["version"])')
  [[ "$ver" == "$VERSION" ]] || die "$(basename "$f"): package.json version is ${ver}, expected ${VERSION}"
  NPM_NAMES+=("$name")
done
read -r nuget_id nuget_ver < <(unzip -p "$OUT"/nuget/*.nupkg '*.nuspec' | python3 -I -c '
import sys, xml.etree.ElementTree as ET
m = ET.fromstring(sys.stdin.read()).find("{*}metadata")
print(m.find("{*}id").text, m.find("{*}version").text)')
[[ "$nuget_ver" == "$VERSION" ]] || die "NuGet .nuspec version is ${nuget_ver}, expected ${VERSION}"
# Wheels and sdists carry the version in the file name (checked by the download list above).

# ---- what is already published ----------------------------------------------
published() { # url -> "yes" when the registry knows that version
  local code; code="$(curl -s -o /dev/null -w '%{http_code}' "$1")"
  case "$code" in 200) echo yes ;; 404) echo no ;; *) echo "unknown (HTTP ${code})" ;; esac
}
{
  echo "| Package | Registry | ${VERSION} already published |"
  echo "|---|---|---|"
  for n in "${NPM_NAMES[@]}"; do
    echo "| \`${n}\` | npm | $(published "https://registry.npmjs.org/${n/\//%2f}/${VERSION}") |"
  done
  for n in pdfix-sdk pdfix-cli; do
    echo "| \`${n}\` | PyPI | $(published "https://pypi.org/pypi/${n}/${VERSION}/json") |"
  done
  lower_id="$(tr '[:upper:]' '[:lower:]' <<<"$nuget_id")"
  echo "| \`${nuget_id}\` | NuGet | $(published "https://api.nuget.org/v3-flatcontainer/${lower_id}/${VERSION}/${lower_id}.nuspec") |"
} > "${OUT}/status.md"

echo
echo "Packages:"
(cd "$OUT" && find . -type f ! -name status.md | sort | while read -r f; do
  printf '  %10s  %s\n' "$(wc -c < "$f" | tr -d ' ')" "${f#./}"; done)
echo
cat "${OUT}/status.md"
