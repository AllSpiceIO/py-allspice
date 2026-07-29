"""Tests for the schemas.pyi generation — the type checker's stricter view of the generated models.

Asserted a schema at a time against the exact source produced, so a field that loses or gains a
Final fails rather than slipping past a fragment match.
"""

from pathlib import Path

from open_api_generator.schema_interface import generate_schema_interface
from open_api_generator.schemas import generate_schemas
from schemas_helpers import FOOTER, SAMPLE_DOCUMENT, definition, use_sample_entities


def test_generate_schema_interface(build_test_dir: Path) -> None:
    schemas_path = build_test_dir / "sample_schemas.py"
    interface_path = build_test_dir / "sample_schemas.pyi"

    generate_schemas(
        SAMPLE_DOCUMENT,
        schemas_path,
        input_schemas={"SampleUserOptions"},
        entities={"SampleUser"},
        footer=FOOTER,
    )
    use_sample_entities(schemas_path)

    generate_schema_interface(schemas_path, interface_path)
    source = interface_path.read_text()

    # Final is added to the existing typing import, since the interface leans on it throughout.
    assert "Final" in source.split("from typing import ")[1].split("\n")[0]

    # An entity keeps its entity base, and only the fields on its patch Option stay writable —
    # SampleUserPatchOptions covers login and full_name, so everything else is Final. Each field also
    # loses its Annotated wrapper, leaving the bare type the annotation carried.
    assert definition(source, "SampleUser") == """class SampleUser(SampleUserEntity):
    id: Final[SampleUserId]
    login: str
    email: Final[str | None] = None
    full_name: str | None = None
    state: Final[SampleUserState]
    roles: Final[list[str] | None] = None
    logins_by_year: Final[dict[int, int] | None] = None
    profile: Final[SampleUserProfile | None] = None"""

    # A ReadOnlyModel has no patchable fields at all, so every one of them is Final. A field's
    # description also becomes an attribute docstring here, so it shows on hover.
    assert definition(source, "SampleUserProfile") == """class SampleUserProfile(ReadOnlyModel):
    bio: Final[str | None] = None
    'A short user biography.'
    company: Final[str | None] = None"""

    # An InputModel is left mutable, so callers can still build one field by field.
    assert definition(source, "SampleUserOptions") == """class SampleUserOptions(InputModel):
    login: str
    full_name: str | None = None
    source_id: int | None = None"""

    # Enums and aliases are copied through untouched (ast.unparse normalizes to single quotes).
    assert definition(source, "SampleUserState") == """class SampleUserState(OpenEnum):
    UNKNOWN = 'unknown'
    active = 'active'
    invited = 'invited'
    suspended = 'suspended'
    deactivated = 'deactivated'"""
    assert definition(source, "SampleUserId") == "SampleUserId = NewType('SampleUserId', int)"
    assert (
        definition(source, "SampleUserSelection")
        == "SampleUserSelection = SampleUserId | list[SampleUserId]"
    )

    # A stub carries signatures only, so a function keeps its signature and loses its body.
    assert definition(source, "is_active") == "def is_active(user: SampleUser) -> bool:\n    ..."

    # The result is valid Python for a type checker to parse.
    compile(source, str(interface_path), "exec")
