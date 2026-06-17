# Branch policy — pdfix_sdk_builds

## Branches

| Branch | Purpose | Lifetime |
|--------|---------|----------|
| `main` | Latest published docs and changelog | Permanent (default) |
| `release/vX.Y.Z` | Prepare changelog + `docs/en/X.Y.Z/` for one SDK release | Delete after merge |
| `gh-pages` | GitHub Pages hosting | Permanent (separate flow) |

## Tags

| Name | Purpose |
|------|---------|
| `vX.Y.Z` | Immutable pointer to the published release (GitHub Release + npm `releases/latest`) |

**Keep using tags.** Release branches are for preparation; tags are for publication.

## Release workflow

1. From `main`: `git checkout -b release/v9.1.0`
2. Commit changelog, `docs/en/9.1.0/`, and root doc updates
3. Open PR `release/v9.1.0` → `main`, merge
4. Run `./scripts/finish-release.sh 9.1.0` (tags, GitHub Release, deletes release branch)

## Naming matrix

| Artifact | Example |
|----------|---------|
| Release branch | `release/v9.1.0` |
| Git tag | `v9.1.0` |
| GitHub Release title | `PDFix SDK 9.1.0` |
| Docs folder | `docs/en/9.1.0/` |
| Changelog header | `## [9.1.0]` |

## GitHub settings

Run once (requires `gh` CLI):

```bash
./scripts/setup-branch-protection.sh
```

Or configure manually:

- **main**: require PR before merge, no force push
- **tags `v*`**: prevent deletion and force push
