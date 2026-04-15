"""Smoke test: shelves scripts run end-to-end on an empty catalog.

Uses the GRIMOIRE_SHELVES_ROOT env var to redirect scripts at a tmp
directory so tests pass regardless of what's in the real catalog.
No behavior asserted beyond exit code 0 — the goal is path-correctness
after the port, not re-testing the upstream scripts' logic."""

import os
import shutil
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPTS = REPO / "shelves" / "scripts"


def _fake_empty_shelves(tmp_path: Path) -> dict:
    """Stage a tmp Grimoire with an empty catalog and return a subprocess env."""
    shelves = tmp_path / "shelves"
    shelves.mkdir()
    (shelves / "catalog.json").write_text("[]")
    shutil.copy(REPO / "grimoire.example.json", tmp_path / "grimoire.example.json")
    return {**os.environ, "GRIMOIRE_SHELVES_ROOT": str(shelves)}


def test_regenerate_on_empty_catalog(tmp_path):
    env = _fake_empty_shelves(tmp_path)
    result = subprocess.run(
        ["python3", str(SCRIPTS / "regenerate.py")],
        capture_output=True,
        text=True,
        env=env,
    )
    assert result.returncode == 0, f"stderr:\n{result.stderr}\nstdout:\n{result.stdout}"


def test_lint_on_empty_catalog(tmp_path):
    env = _fake_empty_shelves(tmp_path)
    result = subprocess.run(
        ["python3", str(SCRIPTS / "lint.py")],
        capture_output=True,
        text=True,
        env=env,
    )
    assert result.returncode == 0, f"stderr:\n{result.stderr}\nstdout:\n{result.stdout}"
