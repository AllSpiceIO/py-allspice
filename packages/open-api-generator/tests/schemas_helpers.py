"""Shared setup for the schema and schema-interface tests, so both assert against the same sample.

Deliberately does not own the `generate_schemas` call — which schemas are treated as entities or
inputs is what those tests are pinning, so it stays visible at each call site.
"""

import ast
import importlib.util
import os
import sys
from pathlib import Path
from types import ModuleType

SAMPLE_DOCUMENT = Path(os.path.dirname(__file__)) / "data" / "schema_sample_document.json"

# Stands in for the curated types appended to the real schemas, and references generated classes so
# it can only work once appended after them.
FOOTER = '''
def is_active(user: SampleUser) -> bool:
    """Return whether the user account is currently active."""
    return user.state is SampleUserState.active
'''


def definition(source: str, name: str) -> str:
    """The generated source of one top-level definition — a class, an alias assignment, or a
    function — so a test can assert against a whole schema rather than fragments of the file."""
    for node in ast.parse(source).body:
        named = (isinstance(node, (ast.ClassDef, ast.FunctionDef)) and node.name == name) or (
            isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == name for target in node.targets)
        )
        if named:
            segment = ast.get_source_segment(source, node)
            assert segment is not None
            return segment

    raise AssertionError(f"no top-level definition of {name!r} in the generated source")


def use_sample_entities(schemas_path: Path) -> None:
    """Repoint generated schemas at sample_entities, which stands in for py-allspice's real
    entities module, so the generated file can be imported."""
    schemas_path.write_text(
        schemas_path.read_text().replace(
            "from allspice.entities import SampleUserEntity",
            "from open_api_generator.sample_entities import SampleUserEntity",
        )
    )


def import_generated(schemas_path: Path, module_name: str) -> ModuleType:
    """Import generated schemas, proving they're valid, wired-up Python and not just the right text —
    the base imports resolve and pydantic builds every model."""
    spec = importlib.util.spec_from_file_location(module_name, schemas_path)
    assert spec and spec.loader

    module = importlib.util.module_from_spec(spec)
    # The generated schemas use `from __future__ import annotations`, so every annotation is a string
    # pydantic resolves against `sys.modules[cls.__module__]` as it builds each model.
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
