"""Grep-based audit: no personal names, handles, or absolute paths leak
into system files. LICENSE is exempt (legal document names the original
author). Content files (if any example content is added later) are
excluded from this check.

Patterns are loaded from tests/fixtures/audit_patterns.json if present
(gitignored, user-specific). Falls back to tests/fixtures/audit_patterns.example.json
whose placeholder patterns intentionally won't match anything real — a
fresh fork passes vacuously until the forker copies the example to the
gitignored file and fills in their own patterns."""

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).parent / "fixtures"

SYSTEM_GLOBS = [
    "CLAUDE.md",
    "AGENTS.md",
    "README.md",
    "grimoire.example.json",
    "schema.json",
    "scrolls/index.example.md",
    ".claude/skills/**/SKILL.md",
    "shelves/scripts/**/*.py",
    "docs/**/*.md",
]


def _load_patterns() -> dict:
    personal = FIXTURES / "audit_patterns.json"
    example = FIXTURES / "audit_patterns.example.json"
    path = personal if personal.exists() else example
    return json.loads(path.read_text())


def _files():
    out = []
    for pattern in SYSTEM_GLOBS:
        out.extend(REPO.glob(pattern))
    return [p for p in out if p.is_file()]


def test_no_personal_leaks():
    patterns = _load_patterns()
    substrings = patterns.get("substrings", [])
    regexes = [(r[0], r[1]) for r in patterns.get("regexes", [])]

    files = _files()
    assert files, "expected at least one system file to audit"

    failures = []
    for f in files:
        text = f.read_text(errors="ignore")
        for needle in substrings:
            if needle.lower() in text.lower():
                failures.append((str(f.relative_to(REPO)), needle))
        for pattern, label in regexes:
            if re.search(pattern, text):
                failures.append((str(f.relative_to(REPO)), label))

    assert not failures, "personal data leaks:\n" + "\n".join(
        f"  {path}: {needle!r}" for path, needle in failures
    )
