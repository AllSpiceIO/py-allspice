import shutil
from pathlib import Path

import pytest

BUILD_TEST_DIR = Path(__file__).resolve().parent.parent / "build" / "test"


@pytest.fixture
def build_test_dir() -> Path:
    """Clean, isolated output dir under build/ for generated test artifacts. Wiped before each test
    so assertions run against this run's output, and kept apart from the real build/ files."""
    shutil.rmtree(BUILD_TEST_DIR, ignore_errors=True)
    BUILD_TEST_DIR.mkdir(parents=True, exist_ok=True)
    return BUILD_TEST_DIR
