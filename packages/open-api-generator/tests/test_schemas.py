import importlib.util
import os
import sys
from pathlib import Path

from open_api_generator.schemas import GENERATED_HEADER, _generate_initial_schemas, generate_schemas


def test_generate_initial_schemas(build_test_dir: Path) -> None:
    # separate test for the initial schema generation, this is the base that we work from after the
    # datamodel-code-gen pass, so making sure its format stays consistent is important for understanding
    # where any failures may be coming from
    sample_document = os.path.join(os.path.dirname(__file__), "data", "schema_sample_document.json")
    output_path = build_test_dir / "sample_schemas.py"

    _generate_initial_schemas(Path(sample_document), output_path)
    source = output_path.read_text()

    # The generated-by header is the first line, marking the file as regenerated, not hand-edited.
    assert source.splitlines()[0] == GENERATED_HEADER

    # A trivial scalar schema renders as a RootModel[...] alias
    assert "SampleUserId = RootModel[int]" in source
    assert "id: SampleUserId" in source

    # A oneOf schema renders as a RootModel[...] union alias
    assert "SampleUserSelection = RootModel[SampleUserId | list[SampleUserId]]" in source

    # Object schemas subclass ReadOnlyModel (base_class)
    assert "from allspice.base import ReadOnlyModel" in source
    assert "class SampleUser(ReadOnlyModel):" in source
    assert "class SampleUserOptions(ReadOnlyModel):" in source

    # An enum schema renders as a closed Enum carrying its spec values
    assert "class SampleUserState(Enum):" in source
    assert "active = 'active'" in source
    assert "invited = 'invited'" in source
    assert "suspended = 'suspended'" in source
    assert "deactivated = 'deactivated'" in source

    # PascalCase spec fields become snake_case attributes that keep the original name as an alias
    # (snake_case_field), so the api name still round-trips.
    assert "login: Annotated[str, Field(alias='Login')]" in source
    assert "source_id: Annotated[int | None, Field(alias='SourceID')] = None" in source

    # A format: email field maps to plain str (type_mappings), never EmailStr — keeps the
    # email-validator dependency out of the generated models.
    assert "email: str | None = None" in source
    assert "EmailStr" not in source

    # String length constraints render as Field metadata inside Annotated (field_constraints).
    assert "login: Annotated[str, Field(max_length=40, min_length=1)]" in source

    # Non-required fields render as `X | None = None`
    assert "full_name: str | None = None" in source
    assert "roles: list[str] | None = None" in source

    # Required fields carry no `= None` default.
    assert "id: SampleUserId\n" in source
    assert "state: SampleUserState\n" in source

    # An integer-keyed map renders with a constr(pattern=...) string key at this step
    assert "logins_by_year: dict[constr(pattern=r'^(0|[1-9][0-9]*)$'), int] | None = None" in source

    # The module imports cleanly: `from allspice.base import ...` resolves and pydantic builds every
    # model, so the output is valid, wired-up Python — not just the right text.
    spec = importlib.util.spec_from_file_location("sample_schemas", output_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert "SampleUser" in vars(module)


def test_generate_schemas(build_test_dir: Path) -> None:
    # The full flow: initial generation plus every post-pass, written out and ruff-fixed. This pins
    # the processed output — what the passes turn the raw models into — as the counterpart to
    # test_generate_initial_schemas above, which pins the raw output.
    sample_document = os.path.join(os.path.dirname(__file__), "data", "schema_sample_document.json")
    output_path = build_test_dir / "processed_sample_schemas.py"

    footer = '''
def is_active(user: SampleUser) -> bool:
    """Return whether the user account is currently active."""
    return user.state is SampleUserState.active
'''

    generate_schemas(
        Path(sample_document),
        output_path,
        input_schemas={"SampleUserOptions"},
        entities={"SampleUser"},
        footer=footer,
    )
    source = output_path.read_text()

    # Root model aliases for scalars transformed into NewType 
    # and fields still reference the alias by name.
    assert 'SampleUserId = NewType("SampleUserId", int)' in source
    assert "id: SampleUserId" in source

    # A oneOf union is stripped to a bare union, not a NewType
    assert "SampleUserSelection = SampleUserId | list[SampleUserId]" in source

    # No root models should be left
    assert "RootModel" not in source

    # integer string keys in dicts are changed back to ints
    assert "logins_by_year: dict[int, int] | None = None" in source
    assert "constr(" not in source

    # Enum bases changed to OpenEnum with an injected UNKNOWN sentinel.
    assert "class SampleUserState(OpenEnum):" in source
    assert "UNKNOWN = 'unknown'" in source

    # Input-only schema bases changed to InputModel.
    assert "class SampleUserOptions(InputModel):" in source

    # Entity bases changed to the corresponding Entity name
    assert "from allspice.entities import SampleUserEntity" in source
    assert "class SampleUser(SampleUserEntity):" in source

    # Non-entity, non-input, non-enum, non-aliases remain as ReadOnlyModels
    assert "class SampleUserProfile(ReadOnlyModel):" in source

    # The footer is appended, after the generated classes it may reference.
    assert "def is_active(user: SampleUser) -> bool:" in source

    # The sample file uses sample entities, so swap the asserted import for
    # sample_entities.py, then import the file to prove the processed schema document is valid Python:
    # SampleUser resolves its entity base and pydantic builds every model.
    source = source.replace(
        "from allspice.entities import SampleUserEntity",
        "from open_api_generator.sample_entities import SampleUserEntity",
    )
    output_path.write_text(source)

    spec = importlib.util.spec_from_file_location("processed_schemas", output_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    user = module.SampleUser(id=1, login="octocat", state=module.SampleUserState.active)
    assert module.is_active(user) is True
    assert module.SampleUserState("unrecognized") is module.SampleUserState.UNKNOWN
