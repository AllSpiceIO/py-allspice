"""Tests for reading the hand-written entity classes."""

from pathlib import Path

from open_api_generator import sample_entities
from open_api_generator.entities import get_entity_schema_names


def test_get_entity_schema_names(build_test_dir: Path) -> None:
    # Tests that:
    #   - `class XEntity(...)` yields X — the schema the generator will reparent onto it
    #   - a class that isn't an entity is ignored, however it's named
    #   - only module-level classes count, so a nested class can't be taken for an entity
    entities_path = build_test_dir / "entities.py"
    entities_path.write_text(
        '''"""Sample entity module."""

from allspice.base import AllSpiceEntity, Committable, Deletable


class HasRepositoryParent(AllSpiceEntity):
    """A mixin, not an entity."""


class RepositoryEntity(Committable, Deletable):
    """An entity."""


class ReleaseEntity(Committable, Deletable, HasRepositoryParent):
    """An entity with a mixin."""

    class NestedEntity(AllSpiceEntity):
        """Indented, so not a module-level entity."""
''',
        encoding="utf-8",
    )

    assert get_entity_schema_names(entities_path) == {"Repository", "Release"}


def test_get_entity_schema_names_of_sample_entities() -> None:
    # The stand-in entity module the schema tests generate against, read as a real file.
    assert get_entity_schema_names(Path(sample_entities.__file__)) == {"SampleUser"}
