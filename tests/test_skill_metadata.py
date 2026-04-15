"""Every Grimoire skill must have a valid frontmatter block with
name and description fields. The name in frontmatter must match the
enclosing directory name."""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / ".claude" / "skills"
EXPECTED = {"inscribe", "bind", "consult", "divine", "audit", "illuminate"}


def _parse_frontmatter(text: str) -> dict:
    """Parses simple `key: value` frontmatter. Single-line values only;
    multi-line YAML (folded, literal, lists) is not supported."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end]
    data = {}
    for line in block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data


def test_all_expected_skills_present():
    present = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
    assert present == EXPECTED, f"skills present={present} expected={EXPECTED}"


def test_each_skill_has_valid_frontmatter():
    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        skill_file = skill_dir / "SKILL.md"
        assert skill_file.exists(), f"missing SKILL.md for {skill_dir.name}"
        fm = _parse_frontmatter(skill_file.read_text())
        assert fm.get("name") == skill_dir.name, (
            f"{skill_dir.name}: frontmatter name={fm.get('name')!r} "
            f"does not match directory"
        )
        desc = fm.get("description", "")
        assert len(desc) >= 40, (
            f"{skill_dir.name}: description too short ({len(desc)} chars): {desc!r}"
        )
