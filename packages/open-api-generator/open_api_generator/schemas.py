"""Generate the Pydantic models in allspice/schemas.py from an OpenAPI document's schemas."""

import re
from pathlib import Path

from datamodel_code_generator import generate
from datamodel_code_generator.enums import DataModelType, InputFileType
from datamodel_code_generator.format import Formatter

from open_api_generator.utils import GENERATED_HEADER, ruff_fix


def generate_schemas(spec_path: Path, output_path: Path, input_schemas: set[str], entities: set[str], footer: str | None) -> None:
    _generate_initial_schemas(spec_path, output_path)

    # Post processing transformations on the generated schemas
    source = output_path.read_text()
    source = _rewrite_integer_map_keys(source)
    source = _rewrite_root_model_aliases(source)
    source = _apply_open_enums(source)

    if entities:
        source = _apply_entity_bases(source, entities)

    if input_schemas:
        source = _apply_input_bases(source, input_schemas)

    if footer:
        source = _append_footer(source, footer)

    output_path.write_text(source)
    ruff_fix(output_path)


def _generate_initial_schemas(spec_path: Path, output_path: Path) -> None:
    """Run datamodel-codegen over spec_path, writing Pydantic v2 models to output_path. Generated
    models subclass allspice.base.ReadOnlyModel."""
    generate(
        spec_path,
        input_file_type=InputFileType.OpenAPI,
        output=output_path,
        output_model_type=DataModelType.PydanticV2BaseModel,
        use_annotated=True,
        field_constraints=True,
        # Emit trivial (non-object) schemas as `Name = RootModel[T]` assignments rather than
        # RootModel subclasses, so rewrite_root_model_aliases can reduce them to bare aliases.
        use_root_model_type_alias=True,
        type_mappings=["string+email=string"],
        # Render every field snake_case, keeping the spec name as an alias — needed because
        # MergePullRequestOption has PascalCase keys (Do, MergeCommitID, ...) that must still be
        # constructible by their original name.
        snake_case_field=True,
        base_class="allspice.base.ReadOnlyModel",
        custom_file_header=GENERATED_HEADER,
        # Pin the formatters (datamodel-codegen is making black/isort opt-in) so the generated
        # layout stays stable.
        formatters=[Formatter.BLACK, Formatter.ISORT],
    )


def _rewrite_integer_map_keys(source: str) -> str:
    """Retype integer-valued map keys that datamodel-codegen renders as a constrained str back to
    int (pydantic round-trips the JSON string keys)."""
    integer_key_constr = "constr(pattern=r'^(0|[1-9][0-9]*)$')"
    return source.replace(integer_key_constr, "int")


def _find_matching_bracket_index(source: str, open_index: int) -> int:
    """Index of the `]` that matches the `[` at open_index, balancing nested brackets."""
    depth = 0
    for index in range(open_index, len(source)):
        if source[index] == "[":
            depth += 1
        elif source[index] == "]":
            depth -= 1
            if depth == 0:
                return index
    raise ValueError(f"no matching bracket for the '[' at index {open_index}")


def _rewrite_root_model_aliases(source: str) -> str:
    """Rewrite `Name = RootModel[T]` to the bare alias `Name = T` (so call sites need no `.root`),
    then brand scalar aliases as distinct NewTypes."""

    # Pass 1: strip the RootModel[...] wrapper, leaving only the alias `Name = <alias_target>`.
    root_model_start_regex = re.compile(r"^(\w+) = RootModel\[", re.MULTILINE)
    output_fragments: list[str] = []
    next_copy_start = 0
    unwrapped_count = 0

    for match in root_model_start_regex.finditer(source):
        alias_name = match.group(1)
        open_bracket = match.end() - 1  # the '[' of RootModel[
        close_bracket = _find_matching_bracket_index(source, open_bracket)

        # Everything between the RootModel's outer generic brackets
        alias_target = " ".join(source[open_bracket + 1 : close_bracket].split())

        # Pull in all code from the end of the last RootModel up until this one
        output_fragments.append(source[next_copy_start : match.start()])

        # Replace the root model with the plain alias
        output_fragments.append(f"{alias_name} = {alias_target}")

        next_copy_start = close_bracket + 1
        unwrapped_count += 1

    output_fragments.append(source[next_copy_start:])

    # combine all fragments to rebuild the source
    source = "".join(output_fragments)

    # Pass 2: brand the bare scalar aliases (str/int/float) as distinct NewTypes.
    scalar_alias_regex = re.compile(r"^(\w+) = (str|int|float)$", re.MULTILINE)
    newtyped_aliases = [name for name, _ in scalar_alias_regex.findall(source)]
    source = scalar_alias_regex.sub(
        lambda match: f'{match.group(1)} = NewType("{match.group(1)}", {match.group(2)})', source
    )

    if newtyped_aliases:
        future_import = "from __future__ import annotations\n"
        source = source.replace(future_import, future_import + "from typing import NewType\n", 1)

    print(f"root-model aliases: {unwrapped_count} unwrapped, {len(newtyped_aliases)} branded as NewType")
    return source


def _add_import(source: str, import_line: str) -> str:
    """Add import_line just after the generated `from allspice.base import ReadOnlyModel` line.
    Raises if that anchor is missing, since every generated file imports the base."""
    anchor = "from allspice.base import ReadOnlyModel\n"
    if anchor not in source:
        raise SystemExit(f"can't add `{import_line.strip()}`: `{anchor.strip()}` not found in source")
    return source.replace(anchor, anchor + import_line, 1)


def _apply_entity_bases(source: str, entities: set[str]) -> str:
    """Change each schema named in entities from `class X(ReadOnlyModel)` to `class X(XEntity)` and
    import those entity classes from allspice.entities. Raises, listing them, if any named entity has
    no matching `class X(ReadOnlyModel)` in the source — so a missing or misnamed schema is easy to
    find."""
    sorted_entities = sorted(entities)

    missing = [e for e in sorted_entities if f"class {e}(ReadOnlyModel):" not in source]
    if missing:
        detail = "\n".join(f"- {e}: expected `class {e}(ReadOnlyModel):`" for e in missing)
        raise SystemExit(
            f"apply_entity_bases: {len(missing)} entity/schema mismatch(es) in source — "
            f"schema class missing or misnamed:\n{detail}"
        )

    for e in sorted_entities:
        source = source.replace(f"class {e}(ReadOnlyModel):", f"class {e}({e}Entity):")

    if sorted_entities:
        entity_imports = ", ".join(f"{e}Entity" for e in sorted_entities)
        source = _add_import(source, f"from allspice.entities import {entity_imports}\n")
        print(f"updated {len(sorted_entities)} to *Entity")

    return source


def _apply_input_bases(source: str, input_schemas: set[str]) -> str:
    """Change each schema named in input_schemas from `class X(ReadOnlyModel)` to
    `class X(InputModel)` and import InputModel. A name that isn't a
    `class X(ReadOnlyModel)` — an enum or a bare alias — has no base to change and is skipped."""
    changed: list[str] = []
    skipped: list[str] = []
    for schema in sorted(input_schemas):
        target = f"class {schema}(ReadOnlyModel):"
        if target in source:
            source = source.replace(target, f"class {schema}(InputModel):")
            changed.append(schema)
        else:
            skipped.append(schema)

    if changed:
        source = _add_import(source, "from allspice.base import InputModel\n")

    print(f"updated {len(changed)} to InputModel", end="")
    print(f"; {len(skipped)} not a ReadOnlyModel class (skipped): {skipped}" if skipped else "")

    return source


def _apply_open_enums(source: str) -> str:
    """Change every generated `class X(Enum)` to `class X(OpenEnum)` with an injected UNKNOWN member,
    so an unrecognized value degrades to UNKNOWN instead of raising, and import OpenEnum."""
    enum_class_regex = re.compile(r"^class (\w+)\(Enum\):$", re.MULTILINE)
    names = enum_class_regex.findall(source)
    if not names:
        return source

    source = enum_class_regex.sub(
        lambda match: f"class {match.group(1)}(OpenEnum):\n    UNKNOWN = 'unknown'", source
    )

    source = _add_import(source, "from allspice.base import OpenEnum\n")

    print(f"updated {len(names)} to OpenEnum")
    
    return source


def _append_footer(source: str, footer: str) -> str:
    """Append custom footer definitions to the end of the file."""
    return source.rstrip() + "\n\n\n" + footer.strip() + "\n"
