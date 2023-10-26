#! /usr/bin/env python3

# Generate a BOM from a PrjPcb file.
# For more information, read the README file in this directory.

import argparse
import csv
import json
import os
import sys
from contextlib import ExitStack

from allspice import AllSpice
from allspice.utils.bom_generation import AttributesMapping, BomEntry, generate_bom_for_altium


with open("attributes_mapping.json", "r") as f:
    attributes_mapper = AttributesMapping.from_dict(json.loads(f.read()))


def sort_function(x: BomEntry) -> str:
    ''' sort BOM list by this criteria'''
    if len(x.designators):
        return sorted(x.designators)[0]
    return "_" + x.part_number


if __name__ == "__main__":
    # Parse command line arguments. If you're writing a special purpose script,
    # you can hardcode these values instead of using command line arguments.
    parser = argparse.ArgumentParser(
        prog="generate_bom", description="Generate a BOM from a PrjPcb file."
    )
    parser.add_argument("repository", help="The repo containing the project")
    parser.add_argument(
        "prjpcb_file", help="The path to the PrjPcb file in the source repo."
    )
    parser.add_argument(
        "pcb_file",
        help="The path to the PCB file in the source repo.",
    )
    parser.add_argument(
        "--source_ref",
        help="The git reference the netlist should be generated for (eg. branch name, tag name, commit SHA). Defaults to main.",
        default="main",
    )
    parser.add_argument(
        "--allspice_hub_url",
        help="The URL of your AllSpice Hub instance. Defaults to https://hub.allspice.io.",
    )
    parser.add_argument(
        "--output_file",
        help="The path to the output file. If absent, the CSV will be output to the command line.",
    )
    parser.add_argument(
        "--attributes_to_extract",
        help="A comma-seperated list of attributes to extract.",
    )

    args = parser.parse_args()

    # Use Environment Variables to store your auth token. This keeps your token
    # secure when sharing code.
    auth_token = os.environ.get("ALLSPICE_AUTH_TOKEN")
    if auth_token is None:
        print("Please set the environment variable ALLSPICE_AUTH_TOKEN")
        exit(1)

    if args.allspice_hub_url is None:
        allspice = AllSpice(token_text=auth_token)
    else:
        allspice = AllSpice(
            token_text=auth_token, allspice_hub_url=args.allspice_hub_url
        )

    repo_owner, repo_name = args.repository.split("/")
    repository = allspice.get_repository(repo_owner, repo_name)
    prjpcb_file = args.prjpcb_file
    pcb_file = args.pcb_file

    print("Generating BOM...", file=sys.stderr)

    bom_rows = generate_bom_for_altium(
        allspice,
        repository,
        prjpcb_file,
        pcb_file,
        attributes_mapper,
        args.source_ref,
    )
    bom_rows = [
        [
            bom_row.description,
            ", ".join(sorted(bom_row.designators)),
            bom_row.quantity,
            bom_row.manufacturer,
            bom_row.part_number,
        ]
        # Sort by designator
        for bom_row in sorted(bom_rows, key=sort_function)
    ]

    with ExitStack() as stack:
        if args.output_file is not None:
            f = stack.enter_context(open(args.output_file, "w"))
            writer = csv.writer(f, lineterminator="\n")
        else:
            writer = csv.writer(sys.stdout, lineterminator="\n")

        header = [
            "Description",
            "Designator",
            "Quantity",
            "Manufacturer",
            "Part Number",
        ]

        writer.writerow(header)
        writer.writerows(bom_rows)

    print("Generated bom.", file=sys.stderr)
