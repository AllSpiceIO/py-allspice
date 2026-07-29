"""Read the hand-written entity classes in allspice/entities.py, the other input the generated
code is built against."""

import re
from pathlib import Path

_ENTITY_CLASS_REGEX = re.compile(r"^class (\w+)Entity\b", re.MULTILINE)


def get_entity_schema_names(entities_path: Path) -> set[str]:
    """The schemas that have a hand-written entity class. By convention
    `class RepositoryEntity(...)` makes the generated `Repository` inherit it, so the schema name is
    the class name with its `Entity` suffix stripped."""
    return set(_ENTITY_CLASS_REGEX.findall(entities_path.read_text(encoding="utf-8")))
