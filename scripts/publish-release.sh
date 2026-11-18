#!/usr/bin/env bash
# Create a DRAFT GitHub Release "PDFix SDK <version>" from a finished Bitbucket build.
#
# Downloads every build artifact from dl.pdfix.net (S3), names the assets for the release
# and creates a draft release with the standard release notes. It never touches an existing
# release or tag: if `v<version>` already exists in any form, it stops with an error.
#
# Usage:
#   scripts/publish-release.sh <version> <branch> <commit> [--dry-run]
#
#   version   X.Y.Z, same as pdfix/version.txt (e.g. 10.0.0)
#   branch    full pdfix branch name of the build (S3 folder), e.g. release/v10.0.0
#   commit    full 40-char pdfix commit of the build (S3 folder)
#   --dry-run download + package into a local directory, create nothing on GitHub
#
# If changelog.md has no dated '## [X.Y.Z] - <date>' heading, the changelog link in the release
# notes uses 'yyyy-mm-dd' as the date; fix the link by hand in the release if needed.
#
# Needs: bash, curl, zip, sha256sum or shasum, gh (authenticated, write access). Run from a checkout
# of pdfix_sdk_builds (the changelog anchor is read from ./changelog.md).
# Env: WORK_DIR (default: mktemp) - where files are downloaded and packaged.

set -euo pipefail

BASE_URL="https://dl.pdfix.net/builds/pdfix-sdk"
REPO="pdfix/pdfix_sdk_builds"
TARGET_BRANCH="main" # branch of pdfix_sdk_builds the tag is created on when the draft is published

die() { echo "error: $*" >&2; exit 1; }

# ---- arguments --------------------------------------------------------------
DRY_RUN=0
POSITIONAL=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) sed -n '2,22p' "$0"; exit 0 ;;
    -*) die "unknown option: $1" ;;
    *) POSITIONAL+=("$1"); shift ;;
  esac
done
[[ ${#POSITIONAL[@]} -eq 3 ]] || die "usage: $0 <version> <branch> <commit> [--dry-run]"
VERSION="${POSITIONAL[0]}"; BRANCH="${POSITIONAL[1]}"; COMMIT="${POSITIONAL[2]}"

[[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || die "version must look like 10.0.0, got '$VERSION'"
[[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || die "commit must be the full 40-char lowercase SHA, got '$COMMIT'"
[[ "$BRANCH" =~ ^[A-Za-z0-9._/-]+$ ]] || die "invalid branch '$BRANCH'"

C8="${COMMIT:0:8}"
TAG="v${VERSION}"
TITLE="PDFix SDK ${VERSION}"
SRC_URL="${BASE_URL}/${BRANCH}/${COMMIT}"

command -v gh >/dev/null || die "gh CLI is required"
command -v zip >/dev/null || die "zip is required"
sha256() { if command -v sha256sum >/dev/null; then sha256sum "$@"; else shasum -a 256 "$@"; fi; }

WORK_DIR="${WORK_DIR:-$(mktemp -d)}"
SRC_DIR="${WORK_DIR}/src"   # files exactly as on S3
OUT_DIR="${WORK_DIR}/assets" # files exactly as they go into the release
rm -rf "$SRC_DIR" "$OUT_DIR"
mkdir -p "$SRC_DIR" "$OUT_DIR"

# ---- refuse to touch an existing release / tag ------------------------------
# `gh release list` includes drafts; a tag can also exist without a release.
EXISTING_TAGS="$(gh release list -R "$REPO" --limit 1000 --json tagName --jq '.[].tagName')" \
  || die "cannot list releases of ${REPO} (gh auth?)"
if grep -qx "$TAG" <<<"$EXISTING_TAGS"; then
  die "a release for ${TAG} already exists (draft or published). This script never modifies releases.
  To redo it: delete that release and its tag on GitHub, then run this again."
fi
if TAG_OUT="$(gh api "repos/${REPO}/git/ref/tags/${TAG}" 2>&1)"; then
  die "tag ${TAG} already exists in ${REPO} without a release. Delete the tag first, then run this again."
elif ! grep -q "Not Found" <<<"$TAG_OUT"; then
  die "cannot check whether tag ${TAG} exists: ${TAG_OUT}"
fi

# ---- release notes (changelog anchor from ./changelog.md) -------------------
[[ -f changelog.md ]] || die "changelog.md not found - run from a checkout of pdfix_sdk_builds"
HEADING="$(grep -m1 -E "^## \[${VERSION//./\\.}\]" changelog.md || true)"
if [[ ! "$HEADING" =~ [0-9]{4}-[0-9]{2}-[0-9]{2} ]]; then
  echo "warning: changelog.md has no dated '## [${VERSION}] - <date>' heading (found: '${HEADING:-none}')." >&2
  echo "         The changelog link uses yyyy-mm-dd; fix it in the release by hand if needed." >&2
  HEADING="## [${VERSION}] - YYYY-MM-DD"
fi
# GitHub heading anchor: lowercase, drop everything except letters, digits, spaces, hyphens; spaces -> hyphens.
ANCHOR="$(echo "${HEADING#\#\# }" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9 -]//g; s/ /-/g')"
NOTES_FILE="${WORK_DIR}/notes.md"
cat > "$NOTES_FILE" <<EOF
[Changelog](https://github.com/${REPO}/blob/main/changelog.md#${ANCHOR})
[SDK Documentation](https://docs.pdfix.net/sdk/overview)
[CLI Documentation](https://docs.pdfix.net/sdk/cli)
[PDF Batch Actions Documentation](https://docs.pdfix.net/actions/overview)
EOF

# ---- the release assets, a subset of the build output (pdfix/bitbucket-pipelines.yml) ----
# Not in the release: npm/, npm-cli/, python/, pip-cli/, nuget/ - these packages are distributed only
# through npm, PyPI and NuGet (see README.md "Download").
# Native SDK packages go to the release as they are.
AS_IS=(
  "pdfix_sdk_${VERSION}_${C8}_linux_aarch64.tar.gz"
  "pdfix_sdk_${VERSION}_${C8}_linux_x86_64.tar.gz"
  "pdfix_sdk_${VERSION}_${C8}_macos_arm64.zip"
  "pdfix_sdk_${VERSION}_${C8}_macos_x86_64.zip"
  "pdfix_sdk_${VERSION}_${C8}_wasm.zip"
  "pdfix_sdk_${VERSION}_${C8}_windows_x86_64.zip"
)
# These are zipped so that the release asset carries the version and the commit:
#   <folder>-<file with _<commit8> after the version>.zip
#   java/net.pdfix.pdfixlib-10.0.0.jar -> java-net.pdfix.pdfixlib-10.0.0_14ecb689.jar.zip
ZIPPED=(
  "java/net.pdfix.pdfixlib-${VERSION}.jar"
)

# ---- download ---------------------------------------------------------------
echo "Source: ${SRC_URL}"
for rel in "${AS_IS[@]}" "${ZIPPED[@]}"; do
  mkdir -p "${SRC_DIR}/$(dirname "$rel")"
  echo "  download ${rel}"
  curl -fsSL --retry 3 --retry-delay 5 -o "${SRC_DIR}/${rel}" "${SRC_URL}/${rel}" \
    || die "cannot download ${SRC_URL}/${rel} - wrong version/commit/branch, or the build is not finished?"
  [[ -s "${SRC_DIR}/${rel}" ]] || die "downloaded file is empty: ${rel}"
done

# ---- package ----------------------------------------------------------------
for rel in "${AS_IS[@]}"; do
  cp "${SRC_DIR}/${rel}" "${OUT_DIR}/$(basename "$rel")"
done
for rel in "${ZIPPED[@]}"; do
  dir="$(dirname "$rel")"; file="$(basename "$rel")"
  [[ "$file" == *"${VERSION}"* ]] || die "no version in file name: ${file}"
  named="${file/${VERSION}/${VERSION}_${C8}}"            # first occurrence of the version
  (cd "${SRC_DIR}/${dir}" && zip -q -X "${OUT_DIR}/${dir}-${named}.zip" "$file")
done

echo
echo "Release ${TAG} \"${TITLE}\" - assets:"
(cd "$OUT_DIR" && ls -1 | sort | while read -r f; do printf '  %10s  %s\n' "$(wc -c < "$f" | tr -d ' ')" "$f"; done)
(cd "$OUT_DIR" && sha256 -- * | sort -k2) > "${WORK_DIR}/sha256.txt"
echo "Checksums: ${WORK_DIR}/sha256.txt"
echo "Notes:"; sed 's/^/  /' "$NOTES_FILE"

EXPECTED=$(( ${#AS_IS[@]} + ${#ZIPPED[@]} ))
[[ "$(ls -1 "$OUT_DIR" | wc -l | tr -d ' ')" -eq "$EXPECTED" ]] || die "asset count mismatch (expected ${EXPECTED}) - duplicate names?"

if [[ $DRY_RUN -eq 1 ]]; then
  echo
  echo "Dry run: nothing created on GitHub. Assets are in ${OUT_DIR}"
  exit 0
fi

# ---- create the draft release ----------------------------------------------
# Only deletes what THIS run created (a half-uploaded draft), never anything else.
CREATED=0
cleanup() {
  if [[ $CREATED -eq 1 ]]; then
    echo "Upload failed - removing the draft this run created" >&2
    gh release delete "$TAG" -R "$REPO" --yes >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

gh release create "$TAG" -R "$REPO" --draft --target "$TARGET_BRANCH" \
  --title "$TITLE" --notes-file "$NOTES_FILE"
CREATED=1   # set only after the create succeeded, so cleanup can never delete someone else's release
gh release upload "$TAG" -R "$REPO" "${OUT_DIR}"/*
CREATED=0

URL="$(gh release list -R "$REPO" --limit 20 --json tagName,url --jq ".[] | select(.tagName==\"${TAG}\") | .url" || true)"
echo
echo "Draft release created: ${URL:-https://github.com/${REPO}/releases}"
echo "Next: check it, then publish it (the tag ${TAG} is created on ${TARGET_BRANCH} at publish time)."
