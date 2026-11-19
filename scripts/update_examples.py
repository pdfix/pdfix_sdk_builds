"""Set the exact PDFix SDK version of a published release in the example repos and in
pdfix-version-updates/v1/versions.json.

Used by .github/workflows/update-examples.yml (see the comments there for inputs and secrets).
Python standard library only. Every target is handled on its own: a failure in one target is
logged, reported as "skipped" in the summary and never stops the others.

Target repos and files: update_repositories.json next to this script.

Pure functions (covered by the local tests in scripts/tests/, gitignored): parse_version, is_higher, derive_release,
rewrite_text, rewrite_versions_json, next_patch_tag.

Usage:
    update_examples.py derive --release-json release.json [--expect-version 9.3.0]
    update_examples.py run --release-json release.json [--dry-run] [--only python,npm]
                           [--url-template '/local/clones/{repo}'] [--workdir DIR]
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass, field
from functools import partial
from pathlib import Path
from typing import Any

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
ASSET_RE = re.compile(
    r"^pdfix_sdk_(?P<version>\d+\.\d+\.\d+)_(?P<commit>[0-9a-f]{8})_"
    r"(?:linux_aarch64|linux_x86_64|macos_arm64|macos_x86_64|wasm|windows_x86_64)"
    r"\.(?:tar\.gz|zip)$"
)
RELEASE_NAME_RE = re.compile(r"^PDFix SDK (?P<version>\d+\.\d+\.\d+)$")

COMMIT_AUTHOR = ("PDFix Support", "support@pdfix.net")
CONFIG_PATH = Path(__file__).with_name("update_repositories.json")

# Statuses returned by rewrite_text / rewrite_versions_json.
UPDATED = "updated"
ALREADY_SET = "already-set"
NOT_HIGHER = "not-higher"


class RewriteError(Exception):
    """A file does not look the way the config expects (pattern not found)."""


class ReleaseError(Exception):
    """The release has no usable SDK version (nothing to derive)."""


# --------------------------------------------------------------------------------------
# Pure functions
# --------------------------------------------------------------------------------------


def parse_version(text: str) -> tuple[int, int, int] | None:
    """Parse a strict ``X.Y.Z`` version. Anything else (``8.*``, ``.4.0``, ``^9.3.0``) is None."""
    match = SEMVER_RE.match(text.strip())
    if match is None:
        return None
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def is_higher(new: str, current: str) -> bool:
    """True if ``new`` is strictly higher than ``current``.

    An unparseable ``current`` (wildcard, broken value) counts as upgradeable, so the first run
    repairs it. ``new`` must be a strict ``X.Y.Z``.
    """
    new_parsed = parse_version(new)
    if new_parsed is None:
        raise ValueError(f"release version is not X.Y.Z: {new!r}")
    current_parsed = parse_version(current)
    if current_parsed is None:
        return True
    return new_parsed > current_parsed


@dataclass
class Release:
    version: str
    commit: str
    published: str  # YYYY-MM-DD (UTC)
    skip_reason: str = ""


def derive_release(release: dict[str, Any]) -> Release:
    """Derive version + 8-char commit from the platform asset names of a GitHub Release.

    Raises ReleaseError when nothing can be derived or the sources disagree. A draft or
    prerelease is returned with ``skip_reason`` set instead.
    """
    published = str(release.get("published_at") or release.get("created_at") or "")[:10]
    if release.get("draft"):
        return Release("", "", published, "release is a draft")
    if release.get("prerelease"):
        return Release("", "", published, "release is a prerelease")

    found: set[tuple[str, str]] = set()
    for asset in release.get("assets") or []:
        match = ASSET_RE.match(str(asset.get("name", "")))
        if match:
            found.add((match.group("version"), match.group("commit")))
    if not found:
        raise ReleaseError("no asset named pdfix_sdk_<version>_<commit8>_<platform>.*")
    if len(found) > 1:
        listing = ", ".join(f"{v}_{c}" for v, c in sorted(found))
        raise ReleaseError(f"platform assets disagree: {listing}")
    version, commit = next(iter(found))

    name_match = RELEASE_NAME_RE.match(str(release.get("name") or "").strip())
    if name_match is None:
        raise ReleaseError(
            f"release name is not 'PDFix SDK <version>': {release.get('name')!r}"
        )
    if name_match.group("version") != version:
        raise ReleaseError(
            f"release name says {name_match.group('version')}, assets say {version}"
        )
    return Release(version, commit, published)


def replace_val(match: re.Match[str], value: str) -> str:
    """The whole match with only the ``val`` group replaced."""
    base = match.start(0)
    whole = match.group(0)
    return whole[: match.start("val") - base] + value + whole[match.end("val") - base :]


def rewrite_text(
    text: str, rules: list[dict[str, Any]], values: dict[str, str]
) -> tuple[str, str, str]:
    """Apply the rewrite rules of one file.

    Each rule has ``pattern`` (regex with a named group ``val``), ``value`` (template using
    ``{version}`` / ``{commit}``) and optionally ``compare: true``. The first compare rule
    decides: equal -> already-set, lower -> not-higher, otherwise all rules are applied.
    Returns ``(new_text, status, current_value)``. Raises RewriteError if a pattern has no match.
    """
    compiled = [(re.compile(rule["pattern"], re.MULTILINE), rule) for rule in rules]
    for regex, rule in compiled:
        if regex.search(text) is None:
            raise RewriteError(f"pattern not found: {rule['pattern']}")

    for regex, rule in compiled:
        if not rule.get("compare"):
            continue
        match = regex.search(text)
        assert match is not None
        current = match.group("val")
        target = rule["value"].format(**values)
        if current.strip() == target:
            return text, ALREADY_SET, current
        if not is_higher(target, current):
            return text, NOT_HIGHER, current
        break
    else:
        current = ""

    for regex, rule in compiled:
        target = rule["value"].format(**values)
        text = regex.sub(partial(replace_val, value=target), text)
    return text, UPDATED, current


def rewrite_versions_json(
    text: str, entry: str, version: str, release_date: str
) -> tuple[str, str, str]:
    """Set ``<entry>.version`` and ``<entry>.release_date`` only (4-space indent like jq).

    Same status semantics as rewrite_text. All other keys are left unchanged.
    """
    data = json.loads(text)
    if entry not in data or "version" not in data[entry]:
        raise RewriteError(f"{entry}.version not found")
    current = str(data[entry]["version"])
    if current == version:
        return text, ALREADY_SET, current
    if not is_higher(version, current):
        return text, NOT_HIGHER, current
    data[entry]["version"] = version
    data[entry]["release_date"] = release_date
    return json.dumps(data, indent=4, ensure_ascii=False) + "\n", UPDATED, current


def next_patch_tag(tags: list[str]) -> str:
    """Latest ``vX.Y.Z`` tag with the patch number incremented (``v0.0.1`` when none)."""
    versions = []
    for tag in tags:
        parsed = parse_version(tag[1:]) if tag.startswith("v") else None
        if parsed is not None:
            versions.append(parsed)
    if not versions:
        return "v0.0.1"
    major, minor, patch = max(versions)
    return f"v{major}.{minor}.{patch + 1}"


# --------------------------------------------------------------------------------------
# Git / process helpers
# --------------------------------------------------------------------------------------


class Context:
    def __init__(
        self, args: argparse.Namespace, release: Release, workdir: Path
    ) -> None:
        self.dry_run: bool = args.dry_run
        self.release = release
        self.workdir = workdir
        self.url_template: str = args.url_template
        self.npm_timeout_s: float = args.npm_timeout_min * 60
        self.npm_interval_s: float = args.npm_interval_s
        self.skip_checks: bool = args.skip_checks
        name, email = COMMIT_AUTHOR
        # Identity for every git command (commit, rebase, annotated tag); CI runners have none.
        self.env = dict(
            os.environ,
            GIT_TERMINAL_PROMPT="0",
            GIT_AUTHOR_NAME=name,
            GIT_AUTHOR_EMAIL=email,
            GIT_COMMITTER_NAME=name,
            GIT_COMMITTER_EMAIL=email,
        )
        token = os.environ.get("GH_APP_TOKEN", "")
        if token:
            # Keeps the token out of argv and remote URLs.
            basic = base64.b64encode(f"x-access-token:{token}".encode()).decode()
            self.env.update(
                GIT_CONFIG_COUNT="1",
                GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
                GIT_CONFIG_VALUE_0=f"Authorization: basic {basic}",
            )

    def git(self, cwd: Path, *args: str, check: bool = True) -> str:
        return run(["git", *args], cwd, self.env, check)


def run(
    cmd: list[str], cwd: Path | None, env: dict[str, str], check: bool = True
) -> str:
    proc = subprocess.run(
        cmd, check=False, cwd=cwd, env=env, capture_output=True, text=True
    )
    if check and proc.returncode != 0:
        detail = (proc.stderr or proc.stdout).strip().splitlines()
        raise RuntimeError(
            f"{' '.join(cmd[:3])} failed: {detail[-1] if detail else proc.returncode}"
        )
    return proc.stdout.strip()


@dataclass
class Outcome:
    target: str
    status: str
    detail: str = ""
    diff: str = ""
    warnings: list[str] = field(default_factory=list)


def read_file(path: Path) -> str:
    """Read without newline translation (and keep a BOM) so untouched lines stay byte-identical."""
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read()


def write_file(path: Path, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def clone(ctx: Context, repo: str) -> Path:
    dest = ctx.workdir / repo
    url = ctx.url_template.format(repo=repo)
    ctx.git(ctx.workdir, "clone", "--quiet", url, str(dest))
    return dest


def default_branch(ctx: Context, repo_dir: Path) -> str:
    ref = ctx.git(repo_dir, "symbolic-ref", "refs/remotes/origin/HEAD")
    return ref.removeprefix("refs/remotes/origin/")


def commit_all(ctx: Context, repo_dir: Path, message: str) -> None:
    name, email = COMMIT_AUTHOR
    ctx.git(repo_dir, "add", "-u")
    ctx.git(
        repo_dir,
        "-c",
        f"user.name={name}",
        "-c",
        f"user.email={email}",
        "commit",
        "-q",
        "-m",
        message,
    )


def check_url_reachable(url: str) -> bool:
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return 200 <= response.status < 300
    except (urllib.error.URLError, TimeoutError, ValueError):
        return False


def npm_has_version(ctx: Context, repo_dir: Path, package: str, version: str) -> bool:
    out = run(
        ["npm", "view", f"{package}@{version}", "version"],
        repo_dir,
        ctx.env,
        check=False,
    )
    return out == version


def wait_for_npm(ctx: Context, repo_dir: Path, package: str, version: str) -> bool:
    """Poll the npm registry. Dry runs check once and never wait."""
    deadline = time.monotonic() + ctx.npm_timeout_s
    while True:
        if npm_has_version(ctx, repo_dir, package, version):
            return True
        if ctx.dry_run or time.monotonic() >= deadline:
            return False
        print(
            f"npm: {package}@{version} not published yet, waiting {ctx.npm_interval_s:.0f}s"
        )
        time.sleep(ctx.npm_interval_s)


# --------------------------------------------------------------------------------------
# Targets
# --------------------------------------------------------------------------------------


def process_example(ctx: Context, target: dict[str, Any]) -> Outcome:
    name, repo = target["name"], target["repo"]
    release = ctx.release
    values = {"version": release.version, "commit": release.commit}

    if target.get("requires_commit"):
        if not release.commit:
            return Outcome(name, "skipped-cpp-no-commit")
        url = target["check_url"].format(**values)
        if not ctx.skip_checks and not check_url_reachable(url):
            return Outcome(name, "skipped-cpp-url-unreachable", url)

    repo_dir = clone(ctx, repo)
    default = default_branch(ctx, repo_dir)
    if (
        ctx.git(repo_dir, "rev-parse", "--verify", "--quiet", "origin/dev", check=False)
        == ""
    ):
        return Outcome(name, "skipped-no-dev-branch")
    in_sync = ctx.git(repo_dir, "rev-parse", "origin/dev") == ctx.git(
        repo_dir, "rev-parse", f"origin/{default}"
    )
    ctx.git(repo_dir, "checkout", "--quiet", "-B", "dev", "origin/dev")

    statuses: dict[str, str] = {}
    current = ""
    for file_cfg in target["files"]:
        path = repo_dir / file_cfg["path"]
        new, status, current = rewrite_text(read_file(path), file_cfg["rules"], values)
        statuses[file_cfg["path"]] = status
        if status == UPDATED:
            write_file(path, new)

    if UPDATED not in statuses.values():
        if NOT_HIGHER in statuses.values():
            return Outcome(name, "skipped-not-higher", f"current {current}")
        return Outcome(name, "skipped-already-set")

    package = target.get("wait_for_npm")
    if package:
        if shutil.which("npm") is None:
            return Outcome(name, "skipped-npm-missing")
        if not wait_for_npm(ctx, repo_dir, package, release.version):
            note = " (dry run: not waiting)" if ctx.dry_run else ""
            return Outcome(
                name,
                "skipped-npm-timeout",
                f"{package}@{release.version} not on npm{note}",
            )
        run(
            [
                "npm",
                "install",
                f"{package}@{release.version}",
                "--save-exact",
                "--package-lock-only",
                "--ignore-scripts",
                "--no-audit",
                "--no-fund",
            ],
            repo_dir,
            ctx.env,
        )

    diff = ctx.git(repo_dir, "diff")
    if ctx.dry_run:
        return Outcome(name, "would-update", f"{current} -> {release.version}", diff)

    commit_all(ctx, repo_dir, f"ci: update PDFix SDK to {release.version}")
    ctx.git(repo_dir, "push", "origin", "dev")
    warnings = []
    where = "dev"
    if in_sync:
        try:
            ctx.git(repo_dir, "push", "origin", f"dev:{default}")
            where = f"dev + {default}"
        except RuntimeError as exc:
            warnings.append(f"{default} not moved: {exc}")
    else:
        warnings.append(f"{default} differs from dev, left unchanged")
    return Outcome(
        name, "updated", f"{current} -> {release.version} ({where})", diff, warnings
    )


def process_versions_repo(ctx: Context, cfg: dict[str, Any]) -> Outcome:
    name = "versions.json"
    release = ctx.release
    repo_dir = clone(ctx, cfg["repo"])
    default = default_branch(ctx, repo_dir)
    ctx.git(repo_dir, "checkout", "--quiet", default)
    ctx.git(repo_dir, "fetch", "--quiet", "--tags")

    path = repo_dir / cfg["path"]
    new, status, current = rewrite_versions_json(
        read_file(path), cfg["entry"], release.version, release.published
    )
    if status == ALREADY_SET:
        return Outcome(name, "skipped-already-set")
    if status == NOT_HIGHER:
        return Outcome(name, "skipped-not-higher", f"current {current}")
    write_file(path, new)
    diff = ctx.git(repo_dir, "diff")

    tags = ctx.git(repo_dir, "tag", "-l", "v*.*.*").splitlines()
    new_tag = next_patch_tag(tags)
    if ctx.dry_run:
        return Outcome(
            name, "would-update", f"{current} -> {release.version}, tag {new_tag}", diff
        )

    commit_all(ctx, repo_dir, f"{cfg['entry']} {release.version}")
    try:
        ctx.git(repo_dir, "push", "origin", default)
    except RuntimeError:
        # Another release job (e.g. an action) pushed first: rebase once and retry.
        ctx.git(repo_dir, "pull", "--quiet", "--rebase", "origin", default)
        ctx.git(repo_dir, "push", "origin", default)

    warnings = []
    ctx.git(repo_dir, "fetch", "--quiet", "--tags")
    if ctx.git(repo_dir, "describe", "--exact-match", "--tags", "HEAD", check=False):
        warnings.append("HEAD already has a tag, no new tag created")
    else:
        new_tag = next_patch_tag(ctx.git(repo_dir, "tag", "-l", "v*.*.*").splitlines())
        try:
            ctx.git(repo_dir, "tag", "-a", new_tag, "-m", f"Release {new_tag}")
            ctx.git(repo_dir, "push", "origin", new_tag)
        except RuntimeError as exc:
            warnings.append(
                f"tag-conflict: {new_tag} not pushed ({exc}); tag it manually"
            )
    return Outcome(name, "updated", f"{current} -> {release.version}", diff, warnings)


# --------------------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------------------


def load_release(path: str, expect_version: str = "") -> Release:
    release = derive_release(json.loads(Path(path).read_text(encoding="utf-8")))
    if expect_version and not release.skip_reason and release.version != expect_version:
        raise ReleaseError(f"requested {expect_version}, release has {release.version}")
    return release


def write_summary(title: str, outcomes: list[Outcome], dry_run: bool) -> None:
    lines = [
        f"## {title}{' (dry run)' if dry_run else ''}",
        "",
        "| Target | Result | Detail |",
        "|---|---|---|",
    ]
    for o in outcomes:
        lines.append(f"| {o.target} | {o.status} | {o.detail} |")
    for o in outcomes:
        for warning in o.warnings:
            lines.append(f"\n:warning: **{o.target}**: {warning}")
    for o in outcomes:
        if o.diff:
            lines += [
                "",
                f"<details><summary>{o.target} diff</summary>",
                "",
                "```diff",
                o.diff,
                "```",
                "",
                "</details>",
            ]
    text = "\n".join(lines) + "\n"
    print(text)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as handle:
            handle.write(text)


def cmd_derive(args: argparse.Namespace) -> int:
    try:
        release = load_release(args.release_json, args.expect_version)
    except ReleaseError as exc:
        print(f"warning: {exc}")
        return 1
    if release.skip_reason:
        print(f"skip: {release.skip_reason}")
        return 1
    print(
        f"version={release.version}\ncommit={release.commit}\npublished={release.published}"
    )
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    if args.skip_checks and not args.dry_run:
        print("--skip-checks is only allowed with --dry-run")
        return 2
    try:
        release = load_release(args.release_json, args.expect_version)
    except ReleaseError as exc:
        write_summary_note(f"No SDK version derived, nothing changed: {exc}")
        return 0
    if release.skip_reason:
        write_summary_note(f"Release skipped, nothing changed: {release.skip_reason}")
        return 0

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    if args.url_template is None:
        args.url_template = f"https://github.com/{config['org']}/{{repo}}.git"
    only: set[str] | None = (
        set(filter(None, args.only.split(","))) if args.only else None
    )

    tmp = None if args.workdir else tempfile.mkdtemp(prefix="update-examples-")
    workdir = Path(args.workdir or tmp or "")
    workdir.mkdir(parents=True, exist_ok=True)
    ctx = Context(args, release, workdir)

    # npm waits for the registry, so it runs after everything else.
    plain = [t for t in config["targets"] if not t.get("wait_for_npm")]
    waiting = [t for t in config["targets"] if t.get("wait_for_npm")]
    steps: list[tuple[str, Callable[[], Outcome]]] = [
        (t["name"], partial(process_example, ctx, t)) for t in plain
    ]
    steps.append(
        ("versions.json", partial(process_versions_repo, ctx, config["versions_repo"]))
    )
    steps += [(t["name"], partial(process_example, ctx, t)) for t in waiting]

    outcomes = []
    for name, step in steps:
        if only is not None and name not in only:
            continue
        try:
            outcomes.append(step())
        except Exception as exc:  # one failing target must not stop the others  # noqa: BLE001
            outcomes.append(Outcome(name, "skipped-error", str(exc)))
    write_summary(
        f"PDFix SDK {release.version} ({release.commit})", outcomes, args.dry_run
    )
    if tmp:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0


def write_summary_note(text: str) -> None:
    print(text)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as handle:
            handle.write(f":warning: {text}\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)

    derive = sub.add_parser(
        "derive", help="print version/commit/date derived from a release JSON"
    )
    derive.add_argument("--release-json", required=True)
    derive.add_argument("--expect-version", default="")
    derive.set_defaults(func=cmd_derive)

    runner = sub.add_parser("run", help="update all targets")
    runner.add_argument("--release-json", required=True)
    runner.add_argument("--expect-version", default="")
    runner.add_argument(
        "--dry-run", action="store_true", help="show diffs, never commit or push"
    )
    runner.add_argument("--only", default="", help="comma-separated target names")
    runner.add_argument(
        "--url-template", default=None, help="clone URL with {repo}; default GitHub"
    )
    runner.add_argument(
        "--workdir", default="", help="keep clones here (default: temp dir)"
    )
    runner.add_argument("--npm-timeout-min", type=float, default=60)
    runner.add_argument("--npm-interval-s", type=float, default=60)
    runner.add_argument(
        "--skip-checks",
        action="store_true",
        help="dry run only: skip the C++ URL check",
    )
    runner.set_defaults(func=cmd_run)

    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
