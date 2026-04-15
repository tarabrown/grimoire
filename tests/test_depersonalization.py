"""Grep-based audit: no personal names, emails, or absolute paths
leak into system files. LICENSE is exempt (legal document names the
original author). Content files (if any example content is added
later) are excluded from this check."""

import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# LICENSE is intentionally excluded — legal attribution is not a leak.
SYSTEM_GLOBS = [
    "CLAUDE.md",
    "AGENTS.md",
    "README.md",
    "review.html",
    "grimoire.example.json",
    "schema.json",
    ".claude/skills/**/SKILL.md",
    "shelves/scripts/**/*.py",
    "docs/**/*.md",
]

SUBSTRING_FORBIDDEN = [
    "Sean Bonner",
    "seanbonner",
    "/Users/seanbonner",
]

REGEX_FORBIDDEN = [
    (r"\bSean\b", "bare first-name 'Sean'"),
    (r"\bSBL\b", "old project name 'SBL'"),
    (r"\bSBW\b", "old project name 'SBW'"),
]


def _files():
    out = []
    for pattern in SYSTEM_GLOBS:
        out.extend(REPO.glob(pattern))
    return [p for p in out if p.is_file()]


def test_no_personal_leaks():
    files = _files()
    assert files, "expected at least one system file to audit"
    failures = []
    for f in files:
        text = f.read_text(errors="ignore")
        for needle in SUBSTRING_FORBIDDEN:
            if needle.lower() in text.lower():
                failures.append((str(f.relative_to(REPO)), needle))
        for pattern, label in REGEX_FORBIDDEN:
            if re.search(pattern, text):
                failures.append((str(f.relative_to(REPO)), label))
    assert not failures, "personal data leaks:\n" + "\n".join(
        f"  {path}: {needle!r}" for path, needle in failures
    )
