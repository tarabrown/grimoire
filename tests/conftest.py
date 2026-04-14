import sys
from pathlib import Path

# Make scripts/ importable for tests that want direct imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "shelves" / "scripts"))
