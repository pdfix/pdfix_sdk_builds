#!/usr/bin/env bash
# Finish a pdfix_sdk_builds release after release/vX.Y.Z is merged into main.
# Usage: ./scripts/finish-release.sh 9.1.0

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <version>" >&2
  echo "Example: $0 9.1.0" >&2
  exit 1
fi

VERSION="$1"
BRANCH="release/v${VERSION}"
TAG="v${VERSION}"
RELEASE_TITLE="PDFix SDK ${VERSION}"

if ! command -v gh >/dev/null 2>&1; then
  echo "error: gh CLI is required (https://cli.github.com/)" >&2
  exit 1
fi

git checkout main
git pull origin main

if git rev-parse "${TAG}" >/dev/null 2>&1; then
  echo "error: tag ${TAG} already exists" >&2
  exit 1
fi

git tag -a "${TAG}" -m "${RELEASE_TITLE}"
git push origin "${TAG}"

gh release create "${TAG}" \
  --title "${RELEASE_TITLE}" \
  --notes "See [changelog](https://github.com/pdfix/pdfix_sdk_builds/blob/main/changelog.md#${VERSION//./}-$(date +%Y-%m-%d)) for details."

if git show-ref --verify --quiet "refs/heads/${BRANCH}"; then
  git branch -d "${BRANCH}"
fi

if git ls-remote --exit-code --heads origin "${BRANCH}" >/dev/null 2>&1; then
  git push origin --delete "${BRANCH}"
fi

echo "Release ${TAG} published. Branch ${BRANCH} removed."
