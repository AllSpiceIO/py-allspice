import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

import allspice
from open_api_generator.document import (
    download_document,
    get_document_version,
    get_input_only_schema_names,
    prune_document,
)
from open_api_generator.entities import get_entity_schema_names
from open_api_generator.requests import generate_requests
from open_api_generator.schema_interface import generate_schema_interface
from open_api_generator.schemas import generate_schemas
from open_api_generator.utils import ruff_fix

BUILD_DIR = Path(__file__).resolve().parent.parent / "build"
# The py-allspice package the generated modules are built for and installed into.
PACKAGE_DIR = Path(allspice.__file__).resolve().parent


@dataclass(frozen=True)
class Arguments:
    hub_base_url: str
    install: bool


def _parse_args() -> Arguments:
    parser = argparse.ArgumentParser(description="Generate the py-allspice Hub API client")
    parser.add_argument("hub_base_url", help="Base URL of the Hub, e.g. http://localhost:3000")
    parser.add_argument(
        "--install",
        action="store_true",
        help="Replace py-allspice's generated modules with this run's output",
    )
    args = parser.parse_args()
    return Arguments(hub_base_url=args.hub_base_url, install=args.install)


# TODO: Find a better place for this: custom types / conveniences to append to the end of schemas
_CURATED_TYPES = '''
# py-allspice types that are not part of the OpenAPI spec, defined here because they compose the
# generated Branch, Commit, and ContentsResponse classes above.

# A git ref: a Branch or Commit object, or a branch / tag / commit name.
Ref = Branch | Commit | str

# Public alias for the spec's file / directory entry type.
Content = ContentsResponse


def normalize_ref(ref: Ref) -> str:
    """Reduce a Ref to the branch name or commit sha the API's `ref` parameters expect."""
    if isinstance(ref, Branch):
        return ref.name
    if isinstance(ref, Commit):
        return ref.sha
    return ref
'''


def main() -> None:
    args = _parse_args()

    shutil.rmtree(BUILD_DIR, ignore_errors=True)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    
    document_path = BUILD_DIR / "openapi.json"
    schema_path = BUILD_DIR / "schemas.py"
    schema_interface_path = BUILD_DIR / "schemas.pyi"
    requests_path = BUILD_DIR / "api_requests.py"

    # The hand-written entity classes the generated schemas inherit from.
    package_entities_path = PACKAGE_DIR / "entities.py"

    download_document(args.hub_base_url, document_path)
    document = json.loads(document_path.read_text())

    print(f"Generating from Hub {get_document_version(document)}")
    document = prune_document(document)
    document_path.write_text(json.dumps(document, indent=2))

    input_schemas = get_input_only_schema_names(document)

    entity_names = get_entity_schema_names(package_entities_path)

    generate_schemas(document_path, schema_path, input_schemas, entity_names, _CURATED_TYPES)
    generate_schema_interface(schema_path, schema_interface_path)

    requests_path.write_text(generate_requests(document))
    ruff_fix(requests_path)

    if args.install:
        _install(requests_path, schema_path, schema_interface_path)


def _install(*paths: Path) -> None:
    """Replace py-allspice's generated modules with the ones just built. Only the generated files are
    copied — the hand-written base.py and entities.py they build on are left alone."""
    for path in paths:
        destination = PACKAGE_DIR / path.name
        shutil.copyfile(path, destination)
        print(f"Installed {path.name} -> {destination}")


if __name__ == "__main__":
    main()
