"""Generate the request classes in allspice/api_requests.py from an OpenAPI document."""

import keyword
import re
from dataclasses import dataclass, field
from typing import Any

from open_api_generator.utils import GENERATED_HEADER, HTTP_METHODS


@dataclass
class _ImportContext:
    """For keeping track of necessary imports across a generation"""
    base: set[str] = field(default_factory=set)    # allspice.base names used
    schemas: set[str] = field(default_factory=set) # allspice.schemas names referenced


def generate_requests(document: dict[str, Any]) -> str:
    """The generated allspice/api_requests.py source: one request class per operation in `document`."""
    request_classes: list[str] = []
    components = document.get("components", {})
    imports = _ImportContext()

    for path, path_methods in document.get("paths", {}).items():
        for method in [key for key in path_methods if key in HTTP_METHODS]:
            operation = path_methods[method]

            request_classes.append(_generate_request_for_operation(path, method, operation, components, imports))

    header = _generate_header(imports)

    return "\n\n\n".join([header, *request_classes]) + "\n"


def _generate_header(imports: _ImportContext) -> str:
    lines = [GENERATED_HEADER, "", "from typing import Annotated", ""]

    if imports.base:
        lines += _generate_import("allspice.base", imports.base)

    if imports.schemas:
        lines += _generate_import("allspice.schemas", imports.schemas, always_wrap=True)

    return "\n".join(lines)


# The line length ruff is configured with, so generated imports come out already formatted
_LINE_LENGTH = 100


def _generate_import(module: str, names: set[str], always_wrap: bool = False) -> list[str]:
    """An import of `names` from `module`, wrapped across lines when it wouldn't fit on one."""
    sorted_names = sorted(names)
    single_line = f"from {module} import {', '.join(sorted_names)}"

    if not always_wrap and len(single_line) <= _LINE_LENGTH:
        return [single_line]

    return [f"from {module} import (", *[f"    {name}," for name in sorted_names], ")"]


@dataclass
class _RequestField:
    """For parsing different field-level properties an operation needs on its request"""
    name: str
    py_type: str
    marker: str  # the Annotated marker, already rendered: 'QueryParam(name="not")', "JSONBody()"
    required: bool
    description: str | None


@dataclass
class _ResponseTypeInfo:
    """For holding information related to the return type and pagination details for a request"""
    response_type: str
    page_item_type: str | None
    page_item_response_key: str | None


def _generate_request_for_operation(path: str, method: str, operation: dict[str, Any], components: dict[str, Any], imports: _ImportContext) -> str:
    # Parse operation information
    operation_id = operation.get("operationId")
    if not operation_id:
        raise ValueError(f"{method.upper()} {path} has no operationId")

    class_name = _class_name_from_operation_id(operation_id)
    response_type_info = _response_type_from_operation(operation, components, imports)
    fields = _fields_from_operation(operation, components, imports)

    # Generate request code
    request_lines: list[str] = [
        _generate_request_class_definition(class_name, response_type_info, imports),
        _generate_doc_string(operation_id, operation.get("summary"), operation.get("tags"), fields),
        f'    method = "{method.upper()}"',
        f'    request_path = "{path}"',
        f"    response_model = {response_type_info.response_type}",
    ]

    if response_type_info.page_item_response_key:
        request_lines.append(f'    _page_items_attr = "{response_type_info.page_item_response_key}"')

    if fields:
        request_lines.append("")
        request_lines += [_generate_field(request_field) for request_field in fields]

    return "\n".join(request_lines)


def _generate_request_class_definition(class_name: str, response_type_info: _ResponseTypeInfo, imports: _ImportContext) -> str:
    if response_type_info.page_item_type:
        imports.base.add("PaginatedRequest")
        return f"class {class_name}(PaginatedRequest[{response_type_info.response_type}, {response_type_info.page_item_type}]):"
    else:
        imports.base.add("ApiRequest")
        return f"class {class_name}(ApiRequest[{response_type_info.response_type}]):"
    

# Base of the Hub swagger-UI URL; operation links are "{base}#/{tag}/{operationId}".
SWAGGER_BASE = "https://hub.allspice.io/api/swagger"


def _generate_doc_string(op_id: str, summary: str | None, tags: list[str] | None, fields: list[_RequestField]) -> str:
    lines: list[str] = []
    if summary:
        lines.append(summary)
    if tag := (tags or [None])[0]:
        if lines:
            lines.append("")
        lines.append(f"{SWAGGER_BASE}#/{tag.lower()}/{op_id}")

    documented_fields = [request_field for request_field in fields if request_field.description]
    if documented_fields:
        if lines:
            lines.append("")
        lines += [f":param {request_field.name}: {request_field.description}" for request_field in documented_fields]

    # Format based on number of available lines
    if not lines:
        return ""

    if len(lines) == 1:
        return f'    """{lines[0]}"""'

    return "\n".join(['    """', *[f"    {line}".rstrip() for line in lines], '    """'])


def _generate_field(request_field: _RequestField) -> str:
    optional = "" if request_field.required else " | None"
    default = "" if request_field.required else " = None"
    return f"    {request_field.name}: Annotated[{request_field.py_type}{optional}, {request_field.marker}]{default}"


def _class_name_from_operation_id(op_id: str) -> str:
    """The PascalCase request-class name for an operationId (suffixed with `Request`)."""
    non_alphanumeric_regex = r"[^0-9a-zA-Z]+"
    # Split up operation ID by any non-alphanumeric value, uppercase the first letter for each and join
    # them back together. These should be mostly camel cased, which already has the right casing for all
    # but first character. Being a little over defensive here and protecting against
    # any snake_case or kabob-case ones that sneak in
    chunks = [chunk for chunk in re.split(non_alphanumeric_regex, op_id) if chunk]
    return "".join(chunk[:1].upper() + chunk[1:] for chunk in chunks) + "Request"


def _response_type_from_operation(operation: dict[str, Any], components: dict[str, Any], imports: _ImportContext) -> _ResponseTypeInfo:
    """The operation's success response as a Python type, plus paging information if the request supports pagination"""
    schema = _response_schema_from_operation(operation, components)
    if schema is None:
        return _ResponseTypeInfo("None", None, None)

    if schema.get("format") == "binary":
        return _ResponseTypeInfo("bytes", None, None)

    response_type = _py_type_from_schema(schema, imports)

    # Paging needs both halves: a page param to send and a list in the response to collect.
    if not _has_page_param(operation):
        return _ResponseTypeInfo(response_type, None, None)

    if schema.get("type") == "array":
        return _ResponseTypeInfo(response_type, _py_type_from_schema(schema["items"], imports), None)

    if "$ref" in schema:
        wrapper = components.get("schemas", {}).get(schema["$ref"].split("/")[-1], {})
        # Only an unambiguous wrapper pages: exactly one of its properties holds the items, and that
        # property is the one send_paginated() reads pages out of.
        item_arrays = {
            name: property_schema
            for name, property_schema in wrapper.get("properties", {}).items()
            if property_schema.get("type") == "array" and "items" in property_schema
        }
        if len(item_arrays) == 1:
            ((items_key, array_schema),) = item_arrays.items()
            return _ResponseTypeInfo(response_type, _py_type_from_schema(array_schema["items"], imports), items_key)

    return _ResponseTypeInfo(response_type, None, None)


def _response_schema_from_operation(operation: dict[str, Any], components: dict[str, Any]) -> dict[str, Any] | None:
    """The schema of the operation's success (2xx) response, or None when it answers with an empty
    body.
    """
    responses = operation.get("responses", {})

    for code in sorted(code for code in responses if code.startswith("2")):
        response = responses[code]

        if "$ref" in response:
            response = components.get("responses", {}).get(response["$ref"].split("/")[-1], {})

        for media_type, media in response.get("content", {}).items():
            # Every JSON response is paired with a text/html error page there's nothing to generate from
            if media_type == "text/html":
                continue

            schema = media.get("schema", {})
            if _is_parseable_response_schema(schema):
                return schema

        return None

    return None


def _is_parseable_response_schema(schema: dict[str, Any]) -> bool:
    """Whether `_response_type_from_operation` has a type for this schema shape."""
    return (
        "$ref" in schema
        or schema.get("format") == "binary"
        or (schema.get("type") == "array" and "items" in schema)
    )


def _has_page_param(operation: dict[str, Any]) -> bool:
    return any(
        parameter.get("name") == "page" and parameter.get("in") == "query"
        for parameter in operation.get("parameters", [])
    )


def _fields_from_operation(operation: dict[str, Any], components: dict[str, Any], imports: _ImportContext) -> list[_RequestField]:
    fields: list[_RequestField] = []

    # Get fields for each parameter
    for parameter in operation.get("parameters", []):
        parameter_field = _field_from_parameter(parameter, imports)
        if parameter_field:
            fields.append(parameter_field)

    # Get a field for a request body if present
    request_body = operation.get("requestBody", {})
    if "$ref" in request_body:
        # A shared body component ($ref to requestBodies/X): resolve it before creating field
        request_body = components.get("requestBodies", {}).get(
            request_body["$ref"].split("/")[-1], {}
        )

    body_field = _field_from_request_body(request_body, imports)
    if body_field:
        fields.append(body_field)

    return fields


_PARAM_MARKERS = {"path": "PathParam", "query": "QueryParam", "header": "HeaderParam"}


def _field_from_parameter(parameter: dict[str, Any], imports: _ImportContext) -> _RequestField | None:
    marker = _PARAM_MARKERS.get(parameter.get("in", ""))
    if marker is None:
        return None

    imports.base.add(marker)
    parameter_name = parameter["name"]
    field_name = _safe_request_field_name(parameter_name)

    return _RequestField(
        name=field_name,
        py_type=_py_type_from_schema(parameter.get("schema", {}), imports),
        # The marker only needs the parameter name when sanitizing changed it
        marker=f'{marker}(api_name="{parameter_name}")' if field_name != parameter_name else f"{marker}()",
        required=bool(parameter.get("required")),
        description=parameter.get("description"),
    )


def _field_from_request_body(resolved_body: dict[str, Any], imports: _ImportContext) -> _RequestField | None:
    content = resolved_body.get("content", {})
    if not content:
        return None

    json_schema = content.get("application/json", {}).get("schema")
    if json_schema:
        imports.base.add("JSONBody")
        return _RequestField(
            name="body",
            py_type=_py_type_from_schema(json_schema, imports),
            marker="JSONBody()",
            required=True,
            description=None,
        )

    multipart_schema = content.get("multipart/form-data", {}).get("schema")
    if multipart_schema:
        return _file_field_from_multipart_schema(multipart_schema, imports)

    raise ValueError(f"no request body mapping for content types {sorted(content)}")


def _file_field_from_multipart_schema(schema: dict[str, Any], imports: _ImportContext) -> _RequestField:
    """The upload field for a multipart body. Only a lone binary property is supported — the request
    framework sends one file and carries no other form fields alongside it."""
    properties = schema.get("properties", {})
    binary_names = [name for name, property_schema in properties.items() if property_schema.get("format") == "binary"]

    if len(properties) != 1 or len(binary_names) != 1:
        raise ValueError(f"multipart body is not a single binary property: {sorted(properties)}")

    imports.base.add("FileBody")
    return _RequestField(
        name="file",
        py_type="bytes",
        marker=f'FileBody(api_name="{binary_names[0]}")',
        required=True,
        description=None,
    )


_SCALARS = {"integer": "int", "string": "str", "boolean": "bool", "number": "float"}


def _py_type_from_schema(schema: dict[str, Any], imports: _ImportContext) -> str:
    """An OpenAPI schema node as a Python type string, recording any schema it references as an
    import."""
    if "$ref" in schema:
        name = schema["$ref"].split("/")[-1]
        imports.schemas.add(name)
        return name

    if schema.get("type") == "array":
        return f"list[{_py_type_from_schema(schema.get('items', {}), imports)}]"

    scalar = _SCALARS.get(schema.get("type", ""))
    if scalar is None:
        raise ValueError(f"no Python type mapping for schema {schema!r}")

    return scalar


# ApiRequest's own attributes — a param field can't shadow these.
_RESERVED = {"method", "request_path", "response_model", "to_request"}


def _safe_request_field_name(original: str) -> str:
    """A Python-safe request field name for a parameter name from the spec — handles keywords,
    invalid identifiers, and collisions with ApiRequest's own attributes."""
    field_name = re.sub(r"\W", "_", original)
    if not field_name or field_name[0].isdigit():
        field_name = "_" + field_name
    if keyword.iskeyword(field_name) or field_name in _RESERVED:
        field_name += "_"
    return field_name
