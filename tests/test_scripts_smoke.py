"""Smoke test: shelves scripts run end-to-end on an empty catalog.

No behavior asserted beyond exit code 0. The goal is path-correctness
after the port, not re-testing SBL's logic."""

import json
import shutil
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SHELVES = REPO / "shelves"
SCRIPTS = SHELVES / "scripts"


def test_regenerate_on_empty_catalog(tmp_path, monkeypatch):
    catalog = SHELVES / "catalog.json"
    if not catalog.exists():
        catalog.write_text("[]")
    result = subprocess.run(
        ["python3", str(SCRIPTS / "regenerate.py")],
        cwd=str(SHELVES),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"stderr:\n{result.stderr}\nstdout:\n{result.stdout}"


def test_lint_on_empty_catalog():
    result = subprocess.run(
        ["python3", str(SCRIPTS / "lint.py")],
        cwd=str(SHELVES),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"stderr:\n{result.stderr}\nstdout:\n{result.stdout}"
