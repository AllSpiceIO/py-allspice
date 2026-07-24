import argparse
import json
from dataclasses import dataclass
from pathlib import Path

from open_api_generator.document import (
    download_document,
    get_document_version,
    prune_document,
)

BUILD_DIR = Path(__file__).resolve().parent.parent / "build"


@dataclass(frozen=True)
class Arguments:
    hub_base_url: str


def _parse_args() -> Arguments:
    parser = argparse.ArgumentParser(description="Generate the py-allspice Hub API client")
    parser.add_argument("hub_base_url", help="Base URL of the Hub, e.g. http://localhost:3000")
    args = parser.parse_args()
    return Arguments(hub_base_url=args.hub_base_url)


def main() -> None:
    args = _parse_args()
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    spec_path = BUILD_DIR / "openapi.json"

    download_document(args.hub_base_url, spec_path)
    document = json.loads(spec_path.read_text())

    print(f"Generating from Hub {get_document_version(document)}")
    document = prune_document(document)

    # TODO: generate schemas + request objects from `document`


if __name__ == "__main__":
    main()
