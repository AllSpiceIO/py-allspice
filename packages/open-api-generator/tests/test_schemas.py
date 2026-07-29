"""Tests for the schema generation.

Each phase is generated once, then asserted a schema at a time against the exact source it produced,
so a field that goes missing or arrives unasked for fails rather than slipping past a fragment match.
"""

from pathlib import Path

from open_api_generator.schemas import GENERATED_HEADER, _generate_initial_schemas, generate_schemas
from schemas_helpers import (
    FOOTER,
    SAMPLE_DOCUMENT,
    definition,
    import_generated,
    use_sample_entities,
)


def test_generate_initial_schemas(build_test_dir: Path) -> None:
    # Separate test for the initial schema generation, this is the base that we work from after the
    # datamodel-code-gen pass, so making sure its format stays consistent is important for
    # understanding where any failures may be coming from.
    output_path = build_test_dir / "sample_schemas.py"

    _generate_initial_schemas(SAMPLE_DOCUMENT, output_path)
    source = output_path.read_text()

    # The generated-by header is the first line, marking the file as regenerated, not hand-edited,
    # and every object schema subclasses the base we asked datamodel-codegen for.
    assert source.splitlines()[0] == GENERATED_HEADER
    assert "from allspice.base import ReadOnlyModel" in source

    # A trivial scalar schema and a oneOf both render as RootModel[...] aliases at this stage.
    assert definition(source, "SampleUserId") == "SampleUserId = RootModel[int]"
    assert (
        definition(source, "SampleUserSelection")
        == "SampleUserSelection = RootModel[SampleUserId | list[SampleUserId]]"
    )

    # An enum schema renders as a closed Enum carrying its spec values.
    assert definition(source, "SampleUserState") == """class SampleUserState(Enum):
    active = 'active'
    invited = 'invited'
    suspended = 'suspended'
    deactivated = 'deactivated'"""

    # The main object schema: required fields carry no default and optional ones are `X | None =
    # None`; a string's length constraints ride inside Annotated (field_constraints); a format: email
    # field is a plain str (type_mappings) rather than EmailStr, keeping email-validator out of the
    # generated models; and an integer-keyed map still has its constr(pattern=...) string key here.
    assert definition(source, "SampleUser") == """class SampleUser(ReadOnlyModel):
    id: SampleUserId
    login: Annotated[str, Field(max_length=40, min_length=1)]
    email: str | None = None
    full_name: str | None = None
    state: SampleUserState
    roles: list[str] | None = None
    logins_by_year: dict[constr(pattern=r'^(0|[1-9][0-9]*)$'), int] | None = None
    profile: SampleUserProfile | None = None"""
    assert "EmailStr" not in source

    # PascalCase spec fields become snake_case attributes that keep the original name as an alias
    # (snake_case_field), so the api name still round-trips.
    assert definition(source, "SampleUserOptions") == """class SampleUserOptions(ReadOnlyModel):
    login: Annotated[str, Field(alias='Login')]
    full_name: Annotated[str | None, Field(alias='FullName')] = None
    source_id: Annotated[int | None, Field(alias='SourceID')] = None"""

    # A schema only reachable as another's field is generated the same way, at the top level.
    # descriptions on fields are added as part of Field
    assert definition(source, "SampleUserProfile") == """class SampleUserProfile(ReadOnlyModel):
    bio: Annotated[str | None, Field(description='A short user biography.')] = None
    company: str | None = None"""

    # The module imports cleanly: `from allspice.base import ...` resolves and pydantic builds every
    # model, so the output is valid, wired-up Python — not just the right text.
    module = import_generated(output_path, "sample_schemas")
    assert "SampleUser" in vars(module)


def test_generate_schemas(build_test_dir: Path) -> None:
    # The full flow: initial generation plus every post-pass, written out and ruff-fixed. This pins
    # the processed output — what the passes turn the raw models into — as the counterpart to
    # test_generate_initial_schemas above, which pins the raw output.
    output_path = build_test_dir / "processed_sample_schemas.py"

    generate_schemas(
        SAMPLE_DOCUMENT,
        output_path,
        input_schemas={"SampleUserOptions"},
        entities={"SampleUser"},
        footer=FOOTER,
    )
    source = output_path.read_text()

    # Every RootModel is gone: a scalar alias is branded as a distinct NewType, while a union is left
    # as a bare alias, so neither needs a `.root` at its call sites.
    assert definition(source, "SampleUserId") == 'SampleUserId = NewType("SampleUserId", int)'
    assert (
        definition(source, "SampleUserSelection")
        == "SampleUserSelection = SampleUserId | list[SampleUserId]"
    )
    assert "RootModel" not in source

    # Enum bases become OpenEnum with an injected UNKNOWN sentinel, so a value added on the server
    # later degrades instead of failing the parse.
    assert definition(source, "SampleUserState") == """class SampleUserState(OpenEnum):
    UNKNOWN = 'unknown'
    active = 'active'
    invited = 'invited'
    suspended = 'suspended'
    deactivated = 'deactivated'"""

    # An entity schema is reparented onto its hand-written entity class, and the integer-keyed map is
    # retyped from its constr(pattern=...) string key back to int.
    assert definition(source, "SampleUser") == """class SampleUser(SampleUserEntity):
    id: SampleUserId
    login: Annotated[str, Field(max_length=40, min_length=1)]
    email: str | None = None
    full_name: str | None = None
    state: SampleUserState
    roles: list[str] | None = None
    logins_by_year: dict[int, int] | None = None
    profile: SampleUserProfile | None = None"""
    assert "from allspice.entities import SampleUserEntity" in source
    assert "constr(" not in source

    # An input-only schema is reparented onto InputModel so callers can build one field by field.
    assert definition(source, "SampleUserOptions") == """class SampleUserOptions(InputModel):
    login: Annotated[str, Field(alias='Login')]
    full_name: Annotated[str | None, Field(alias='FullName')] = None
    source_id: Annotated[int | None, Field(alias='SourceID')] = None"""

    # Anything that is neither an entity, an input, an enum, nor an alias stays a ReadOnlyModel.
    assert definition(source, "SampleUserProfile") == """class SampleUserProfile(ReadOnlyModel):
    bio: Annotated[str | None, Field(description='A short user biography.')] = None
    company: str | None = None"""

    # The footer is appended verbatim, after the generated classes it references.
    assert definition(source, "is_active") == '''def is_active(user: SampleUser) -> bool:
    """Return whether the user account is currently active."""
    return user.state is SampleUserState.active'''

    # The sample file uses sample entities, so swap the asserted import for sample_entities.py, then
    # import the file to prove the processed schema document is valid Python: SampleUser resolves its
    # entity base and pydantic builds every model.
    use_sample_entities(output_path)
    module = import_generated(output_path, "processed_schemas")

    user = module.SampleUser(id=1, login="octocat", state=module.SampleUserState.active)
    assert module.is_active(user) is True
    assert module.SampleUserState("unrecognized") is module.SampleUserState.UNKNOWN
