#!/usr/bin/env bash
# Configure GitHub branch/tag protection for pdfix_sdk_builds.
# Requires: gh CLI authenticated with admin access to pdfix/pdfix_sdk_builds
# Usage: ./scripts/setup-branch-protection.sh

set -euo pipefail

REPO="pdfix/pdfix_sdk_builds"

if ! command -v gh >/dev/null 2>&1; then
  echo "error: gh CLI is required (https://cli.github.com/)" >&2
  exit 1
fi

echo "Protecting main branch..."
gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/${REPO}/branches/main/protection" \
  -f required_status_checks='null' \
  -F enforce_admins=false \
  -F required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  -F restrictions='null' \
  -F required_linear_history=false \
  -F allow_force_pushes=false \
  -F allow_deletions=false

echo "Protecting v* tags..."
gh api \
  --method GET \
  -H "Accept: application/vnd.github+json" \
  "/repos/${REPO}" \
  --jq .id >/dev/null

# Tag protection uses rulesets on newer GitHub; fall back to documented manual step if API fails.
if gh api \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  "/repos/${REPO}/rulesets" \
  -f name="Protect version tags" \
  -f target="tag" \
  -f enforcement="active" \
  -f conditions='{"ref_name":{"include":["refs/tags/v*"],"exclude":[]}}' \
  -f rules='[{"type":"deletion"},{"type":"non_fast_forward"}]' 2>/dev/null; then
  echo "Tag ruleset created."
else
  echo "Note: enable tag protection manually in GitHub:"
  echo "  Settings → Tags → Add rule pattern v* → Block force pushes and deletions"
fi

echo "Done. Verify at https://github.com/${REPO}/settings/branches"
