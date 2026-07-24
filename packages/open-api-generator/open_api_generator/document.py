"""Operations on the OpenAPI document: download it, and prune it down to
the operations and components py-allspice generates from."""

import copy
from pathlib import Path
from typing import Any, NamedTuple

import requests

HTTP_METHODS = {"get", "put", "post", "delete", "patch"}


def download_document(hub_base_url: str, output_path: Path) -> None:
    url = hub_base_url.rstrip("/") + "/swagger.v1.json"
    response = requests.get(url)
    response.raise_for_status()
    output_path.write_bytes(response.content)


def get_document_version(document: dict[str, Any]) -> str:
    return document["info"]["version"]


class _ComponentRef(NamedTuple):
    component_type: str
    name: str


def _parse_component_ref(ref: str) -> _ComponentRef | None:
    """All refs start with #/components followed by a component type and then a name.

    For example:
        #/components/schemas/ResponseBody
        #/components/requestBodies/SomeRequestsBody
    """
    if not ref.startswith("#/components"):
        return None

    parts = ref.split("/")
    if len(parts) < 4:
        return None

    return _ComponentRef(component_type=parts[2], name=parts[3])


def _reachable_component_refs(
    from_nodes: list[object], components: dict[str, Any]
) -> set[_ComponentRef]:
    """Every component transitively referenced from from_nodes, following $refs
    through components to a fixpoint."""
    reached: set[_ComponentRef] = set()
    to_visit = list(from_nodes)

    while to_visit:
        node = to_visit.pop()

        if isinstance(node, list):
            to_visit.extend(node)
        elif isinstance(node, dict):
            # Need to add all values, even if a ref string as OpenAPI 3.1 can have siblings
            # on ref objects
            to_visit.extend(node.values())
            ref_str = node.get("$ref")

            if isinstance(ref_str, str):
                ref = _parse_component_ref(ref_str)
                # Ignore invalid refs and ones we've already reached and traversed
                if ref is not None and ref not in reached:
                    reached.add(ref)

                    # Get its definition to follow and capture any nested references
                    definition = components.get(ref.component_type, {}).get(ref.name)
                    if definition is not None:
                        to_visit.append(definition)

    return reached


def prune_document(document: dict[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(document)
    components = document.get("components", {})

    # Drop operations with no py-allspice code sample, then any emptied path.
    for path, item in list(document.get("paths", {}).items()):
        for method in [m for m in item if m in HTTP_METHODS]:
            if "x-codeSamples" not in item[method]:
                del item[method]
        if not any(m in item for m in HTTP_METHODS):
            del document["paths"][path]

    # Get a list of all components reachable from paths
    reachable = _reachable_component_refs([document.get("paths", {})], components)

    # Prune every $ref-addressable component type to what's reachable.
    for component_type, entries in list(components.items()):
        components[component_type] = {
            name: node for name, node in entries.items() if (component_type, name) in reachable
        }

    return document


def get_input_only_schema_names(document: dict[str, Any]) -> set[str]:
    """Schema names reachable only from requests, not responses."""
    components = document.get("components", {})

    operations: list[object] = []
    responses: list[object] = []
    for item in document.get("paths", {}).values():
        for method in [m for m in item if m in HTTP_METHODS]:
            operation = item[method]
            operations.append(operation)
            responses.append(operation.get("responses"))

    operation_reachable = _reachable_component_refs(operations, components)
    response_reachable = _reachable_component_refs(responses, components)

    input_only = operation_reachable - response_reachable
    return {ref.name for ref in input_only if ref.component_type == "schemas"}
