"""Generate schemas.pyi from the generated schemas.py — the type checker's stricter view of the
same classes."""

import ast
import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import NamedTuple

from open_api_generator.utils import GENERATED_HEADER, ruff_fix


def generate_schema_interface(schemas_path: Path, interface_path: Path) -> None:
    """Emit schemas.pyi, which adds the compile-time read-only enforcement the runtime models can't
    (pyright ignores a model_config of frozen). Per class:
      - entity classes: non-patchable fields -> Final[...]; patch Option fields stay writable
      - ReadOnlyModel classes: every field -> Final[...]
      - InputModel classes: fields left mutable
      - enums / RootModels / anything else: copied through unchanged
    Each Field(description=...) becomes an attribute docstring so it shows on hover."""
    schemas = _load_generated_schemas(schemas_path)
    tree = ast.parse(schemas_path.read_text(encoding="utf-8"))

    # Rewrite all top level Classes
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            _rewrite_class_node(node, schemas)

    # A .pyi carries signatures, not implementations — stub every function body to `...`
    # This must walk the full tree for methods on classes, etc
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            node.body = [ast.Expr(value=ast.Constant(value=...))]

    # Add Final to typing import
    _ensure_typing_import(tree, "Final")

    ast.fix_missing_locations(tree)
    interface_path.write_text(
        GENERATED_HEADER + "\n\n" + ast.unparse(tree) + "\n", encoding="utf-8"
    )
    ruff_fix(interface_path)

    print(f"generated schemas interface -> {interface_path.name}")


def _load_generated_schemas(schemas_path: Path) -> ModuleType:
    """Import the schemas.py just written, so which fields to freeze can be read off the live
    classes."""

    # The name the generated schemas are imported under. Deliberately not `allspice.schemas`: the name
    # isn't meaningful to anything here, and using the real one would replace the installed module for
    # the rest of the process.
    loaded_schemas_module = "_generated_schemas"

    spec = importlib.util.spec_from_file_location(loaded_schemas_module, schemas_path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"can't load generated schemas from {schemas_path}")

    module = importlib.util.module_from_spec(spec)
    # The generated schemas use `from __future__ import annotations`, so every annotation is a
    # string that pydantic resolves against `sys.modules[cls.__module__]` when it builds each model.
    sys.modules[loaded_schemas_module] = module
    spec.loader.exec_module(module)
    return module


def _rewrite_class_node(node: ast.ClassDef, schemas: ModuleType) -> None:
    """Rewrite the class's field declarations into their interface form: the Annotated[...] wrapper is
    dropped, a read-only field's type is wrapped in Final[...], and any description the wrapper
    carried becomes an attribute docstring."""

    # Base type determines which fields, if any, get frozen
    from allspice.base import AllSpiceEntity, Committable, InputModel, ReadOnlyModel

    # Make sure we can load the schema class
    schema_class = getattr(schemas, node.name, None)
    if not isinstance(schema_class, type):
        raise SystemExit(f"Unable to load {node.name} from schemas file")

    # If Committable, freeze all non-patchable fields
    if issubclass(schema_class, Committable):
        return _rewrite_class_fields(
            node, freeze_fields=True, writable=schema_class._compute_patchable_fields()
        )
    # If non-committable entity, or ReadOnly Model freeze all fields
    elif issubclass(schema_class, AllSpiceEntity):
        return _rewrite_class_fields(node, freeze_fields=True)
    elif issubclass(schema_class, ReadOnlyModel):
        return _rewrite_class_fields(node, freeze_fields=True)
    # If InputModel, don't freeze fields, but do rewrite to get Descriptions as doc strings
    elif issubclass(schema_class, InputModel):
        return _rewrite_class_fields(node, freeze_fields=False)
    # If not one of our base classes, just skip it (either enum, or custom added footer class)
    else:
        return


def _rewrite_class_fields(
    node: ast.ClassDef, freeze_fields: bool, writable: set[str] = set()
) -> None:
    """Wrap the class's frozen fields in Final[...], and turn each field's description into an
    attribute docstring."""
    body: list[ast.stmt] = []
    for statement in node.body:
        if not (isinstance(statement, ast.AnnAssign) and isinstance(statement.target, ast.Name)):
            body.append(statement)
            continue

        bare_type, description = _parse_annotation(statement.annotation)
        freeze = freeze_fields and (statement.target.id not in writable)
        statement.annotation = (
            ast.Subscript(
                value=ast.Name(id="Final", ctx=ast.Load()), slice=bare_type, ctx=ast.Load()
            )
            if freeze
            else bare_type
        )
        body.append(statement)

        if description:
            body.append(ast.Expr(value=ast.Constant(value=description)))

    node.body = body


class _AnnotationInfo(NamedTuple):
    bare_type: ast.expr
    description: str | None


def _parse_annotation(annotation: ast.expr) -> _AnnotationInfo:
    """Get bare_type and description from an annotation expression"""
    # If not "Annotated" just return the bare_type
    if not (
        isinstance(annotation, ast.Subscript)
        and isinstance(annotation.value, ast.Name)
        and annotation.value.id == "Annotated"
        and isinstance(annotation.slice, ast.Tuple)
    ):
        return _AnnotationInfo(bare_type=annotation, description=None)

    bare_type, *metadata = annotation.slice.elts
    description = _find_description_from_annotation_metadata(metadata)

    return _AnnotationInfo(bare_type, description)


def _find_description_from_annotation_metadata(metadata: list[ast.expr]) -> str | None:
    """Look for a pydantic Field's description and return it if present"""
    for entry in metadata:
        if isinstance(entry, ast.Call) and _is_field_call(entry.func):
            for keyword in entry.keywords:
                # A Constant holds any literal; only a string is usable as a docstring.
                if (
                    keyword.arg == "description"
                    and isinstance(keyword.value, ast.Constant)
                    and isinstance(keyword.value.value, str)
                ):
                    return keyword.value.value

    return None


def _is_field_call(func: ast.expr) -> bool:
    """Whether a call is pydantic's `Field(...)`, imported directly or used as `pydantic.Field`."""
    return (isinstance(func, ast.Name) and func.id == "Field") or (
        isinstance(func, ast.Attribute) and func.attr == "Field"
    )


def _ensure_typing_import(tree: ast.Module, name: str) -> None:
    """Add `name` to the module's `from typing import ...` so the interface can reference it."""
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module == "typing":
            if not any(alias.name == name for alias in node.names):
                node.names.append(ast.alias(name=name))
            return

    raise SystemExit(f"can't add `{name}`: no `from typing import ...` found in the schemas")
