import subprocess
from pathlib import Path

def ruff_fix(*paths: Path) -> None:
    """Apply ruff's safe autofixes to the generated files — sorts imports and strips ones left
    unused by the rewrites, along with the project's other fixable rules."""
    subprocess.run(["ruff", "check", "--fix", *(str(p) for p in paths)], check=True)
