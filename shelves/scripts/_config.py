"""Shared config loader for Grimoire Shelves scripts.

Resolves grimoire.json at the Grimoire root, which is one directory up
from shelves/. Falls back to grimoire.example.json if grimoire.json is
missing (useful for CI / smoke tests).

SHELVES_ROOT defaults to the directory containing this script's parent,
but can be overridden via the GRIMOIRE_SHELVES_ROOT env var — used by
smoke tests to redirect scripts at a tmp directory."""

import json
import os
from pathlib import Path

_ENV_ROOT = os.environ.get("GRIMOIRE_SHELVES_ROOT")
SHELVES_ROOT = Path(_ENV_ROOT).resolve() if _ENV_ROOT else Path(__file__).resolve().parent.parent
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
