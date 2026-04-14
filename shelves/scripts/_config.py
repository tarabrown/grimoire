"""Shared config loader for Grimoire Shelves scripts.

Resolves grimoire.json at the Grimoire root, which is one directory up
from shelves/. Falls back to grimoire.example.json if grimoire.json is
missing (useful for CI / smoke tests)."""

import json
from pathlib import Path

SHELVES_ROOT = Path(__file__).resolve().parent.parent  # shelves/
GRIMOIRE_ROOT = SHELVES_ROOT.parent

def load_config() -> dict:
    personal = GRIMOIRE_ROOT / "grimoire.json"
    example = GRIMOIRE_ROOT / "grimoire.example.json"
    path = personal if personal.exists() else example
    with path.open() as f:
        return json.load(f)

def catalog_path() -> Path:
    return SHELVES_ROOT / "catalog.json"

def context_paths() -> dict:
    return {
        "overview": SHELVES_ROOT / "CONTEXT_OVERVIEW.md",
        "compact": SHELVES_ROOT / "CONTEXT_COMPACT.md",
        "full": SHELVES_ROOT / "CONTEXT.md",
    }
