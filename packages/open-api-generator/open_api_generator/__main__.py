import argparse
import json
from dataclasses import dataclass
from pathlib import Path

from open_api_generator.document import (
    download_document,
    get_document_version,
    get_input_only_schema_names,
    prune_document,
)
from open_api_generator.requests import generate_requests
from open_api_generator.schemas import generate_schemas
from open_api_generator.utils import ruff_fix

BUILD_DIR = Path(__file__).resolve().parent.parent / "build"


@dataclass(frozen=True)
class Arguments:
    hub_base_url: str


def _parse_args() -> Arguments:
    parser = argparse.ArgumentParser(description="Generate the py-allspice Hub API client")
    parser.add_argument("hub_base_url", help="Base URL of the Hub, e.g. http://localhost:3000")
    args = parser.parse_args()
    return Arguments(hub_base_url=args.hub_base_url)


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
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    document_path = BUILD_DIR / "openapi.json"
    schema_path = BUILD_DIR / "schemas.py"
    requests_path = BUILD_DIR / "requests.py"

    download_document(args.hub_base_url, document_path)
    document = json.loads(document_path.read_text())

    print(f"Generating from Hub {get_document_version(document)}")
    document = prune_document(document)
    document_path.write_text(json.dumps(document, indent=2))

    input_schemas = get_input_only_schema_names(document)

    # TODO: Get entities from entities.py in py-allspice when avaible
    entity_names = set()

    generate_schemas(document_path, schema_path, input_schemas, entity_names, _CURATED_TYPES)

    requests_path.write_text(generate_requests(document))
    ruff_fix(requests_path)


if __name__ == "__main__":
    main()
