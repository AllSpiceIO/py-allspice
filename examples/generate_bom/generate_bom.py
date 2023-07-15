#! /usr/bin/env python3

# Generate a BOM from a PrjPcb file for an Altium Project.
# For more information, read the README file in this directory.

from __future__ import annotations

import argparse
import base64
from collections import defaultdict
from contextlib import ExitStack
import csv
import dataclasses
from dataclasses import dataclass
import json
import os
import re
import sys
import time
from typing import Optional, Union

from allspice import AllSpice
from allspice.exceptions import NotYetGeneratedException

global attributes_mapper

with open("attributes_mapping.json", "r") as f:
    attributes_mapper = json.loads(f.read())


@dataclass
class Component:
    """
    A Component in the Project.

    :param description: A description for the component. This is optional.
    :param designator: The designator of the component. This is mandatory.
    :param manufacturer: The manufacturer of the component. This is optional.
    :param part_number: The part number of the component. This is like a SKU
        that you can use to look up the part, say on DigiKey or Mouser. If not
        present, you may not be able to calculate COGS, and each designator
        will be treated as a separate component.
    """

    description: Optional[str]
    designator: str
    manufacturer: Optional[str]
    part_number: Optional[str]


def find_first_matching_key(
    alternatives: Union[list[str], str],
    attributes: dict,
) -> Optional[str]:
    """
    Search for a key in the JSON. If it's not found, try the alternatives.
    """

    if isinstance(alternatives, str):
        alternatives = [alternatives]

    for alternative in alternatives:
        if alternative in attributes:
            return attributes[alternative]["text"]

    return None


def map_json_to_component(attributes: dict, mapper: dict) -> Component:
    """
    Make a Component object out of the JSON for it in the SchDoc file.

    :param json: The JSON for a component.
    :param mapper: A dictionary that maps keys in the JSON to fields of
        Component.
    :returns: A Component object representing that component.
    """

    return Component(
        description=find_first_matching_key(mapper["description"], attributes),
        designator=find_first_matching_key(mapper["designator"], attributes) or "",
        manufacturer=find_first_matching_key(mapper["manufacturer"], attributes),
        part_number=find_first_matching_key(mapper["part_number"], attributes),
    )


def split_repo_name(name) -> tuple[str, str]:
    """
    Split a repo name into a tuple of (owner, repo).
    """

    if "/" not in name:
        raise ValueError(f"Invalid repo name {name}")

    owner, repo = name.split("/")
    return owner, repo


def get_file_content(repo, file_path, branch) -> str:
    """
    Get the content of a file in a repo on a branch.
    """

    files_in_repo = repo.get_git_content(ref=branch)
    file = next((x for x in files_in_repo if x.path == file_path), None)
    if not file:
        raise ValueError(
            f"File {file_path} not found in repo {repo.name} on branch {branch.name}"
        )

    content = repo.get_file_content(file, ref=branch)
    return base64.b64decode(content).decode("utf-8")


def get_schdoc_list_from_prjpcb(prjpcb_file_content) -> list[str]:
    """
    Get a list of SchDoc files from a PrjPcb file.
    """

    pattern = re.compile(r"DocumentPath=(.*?SchDoc)\r\n")
    return [match.group(1) for match in pattern.finditer(prjpcb_file_content)]


def extract_components_from_schdoc(schdoc_file_content) -> list[Component]:
    """
    Extract all the components from a schdoc file. To see what attributes are
    available, print the schdoc_file_content variable.

    :param schdoc_file_content: The content of the SchDoc file. This should be a
    dictionary.
    """

    components_list = []

    for value in schdoc_file_content.values():
        if isinstance(value, dict):
            if value.get("type") == "Component":
                attributes = value["attributes"]
                components_list.append(
                    map_json_to_component(
                        attributes,
                        attributes_mapper,
                    )
                )

    return components_list


def link_pcb_components(
    pcb_file_content: dict,
    designator_to_components: dict[str, Component],
) -> list[Component]:
    """
    Link the components in the PCB file to the components in the SchDoc file.
    """

    component_instances = pcb_file_content["component_instances"]
    pcb_components = []

    for component in component_instances.values():
        try:
            schematic_link = component["schematic_link"]
            linked_component = designator_to_components[schematic_link]
            pcb_components.append(
                dataclasses.replace(
                    linked_component, designator=component["designator"]
                )
            )
        except KeyError as e:
            designator = component["designator"]
            schematic_link = component["schematic_link"]
            print(
                f"Warning: Found component {designator} linked to schematic "
                + f"designator {schematic_link} in PCB but not in SchDoc.",
                file=sys.stderr,
            )
            continue

    return pcb_components


if __name__ == "__main__":
    # Parse command line arguments. If you're writing a special purpose script,
    # you can hardcode these values instead of using command line arguments.
    parser = argparse.ArgumentParser(
        prog="generate_bom", description="Generate a BOM from a PrjPcb file."
    )
    parser.add_argument("source_repo", help="The repo containing the PrjPcb file.")
    parser.add_argument(
        "source_file", help="The path to the PrjPcb file in the source repo."
    )
    parser.add_argument(
        "pcb_file",
        help="The path to the PCB file in the source repo.",
    )
    parser.add_argument(
        "--schdoc_repo",
        help="The repo containing the SchDoc files. Defaults to the same repo as the PrjPcb file.",
    )
    parser.add_argument(
        "--source_branch",
        help="The branch containing the PrjPcb file. Defaults to main.",
        default="main",
    )
    parser.add_argument(
        "--schdoc_branch",
        help="The branch containing the SchDoc files. Defaults to the same branch as PrjPcb.",
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

    args = parser.parse_args()

    # Use Environment Variables to store your auth token. This keeps your token
    # secure when sharing code.
    auth_token = os.environ.get("ALLSPICE_AUTH_TOKEN")
    if auth_token is None:
        print(
            "Please set the environment variable ALLSPICE_AUTH_TOKEN",
            file=sys.stderr,
        )
        exit(1)

    if args.allspice_hub_url is None:
        allspice = AllSpice(token_text=auth_token)
    else:
        allspice = AllSpice(
            token_text=auth_token, allspice_hub_url=args.allspice_hub_url
        )

    source_repo_owner, source_repo_name = split_repo_name(args.source_repo)
    source_file = args.source_file
    if args.schdoc_repo is not None:
        schdoc_repo_owner, schdoc_repo_name = split_repo_name(args.schdoc_repo)
    else:
        schdoc_repo_owner = source_repo_owner
        schdoc_repo_name = source_repo_name
    source_branch = args.source_branch
    schdoc_branch = args.schdoc_branch if args.schdoc_branch else source_branch
    pcb_file = args.pcb_file

    print("Generating BOM with the given arguements:", file=sys.stderr)
    print(
        f"{source_repo_owner=} {source_repo_name=} {source_branch=}"
        + f"{source_file=} {schdoc_repo_owner=} {schdoc_repo_name=}"
        + f"{schdoc_branch=} {args.output_file=} {pcb_file=}",
        file=sys.stderr,
    )

    # Get the PrjPcb file from the source repo.
    prjpcb_repo = allspice.get_repository(source_repo_owner, source_repo_name)
    prjpcb_branch = prjpcb_repo.get_branch(source_branch)
    prjpcb_file = get_file_content(prjpcb_repo, source_file, prjpcb_branch)
    schdoc_files_in_proj = {x for x in get_schdoc_list_from_prjpcb(prjpcb_file)}

    print(f"{schdoc_files_in_proj=}", file=sys.stderr)

    # Get the SchDoc files from the SchDoc repo.
    schdoc_repo = allspice.get_repository(schdoc_repo_owner, schdoc_repo_name)
    schdoc_branch = schdoc_repo.get_branch(schdoc_branch)
    schdoc_files_in_repo = schdoc_repo.get_git_content(ref=schdoc_branch)

    # Extract components from the SchDoc files. See the
    # `extract_components_from_schdoc` function for more information.
    all_components: list[Component] = []

    # Note: we're going through the files in the repo and checking if they're
    # in the PrjPcb file. This may miss some files in the proj if they're
    # not in the repo. If you're seeing inconsistent or missing results,
    # check that all the SchDoc files are in the repo, or uncomment this line:

    # breakpoint()

    # And run the script. You'll be dropped into a debugger where you can
    # print() variables and see what's going on.

    for schdoc_file in schdoc_files_in_repo:
        schdoc_path = schdoc_file.path
        if schdoc_path in schdoc_files_in_proj:
            # If the file is not yet generated, we'll retry a few times.
            retry_count = 0
            while True:
                retry_count += 1

                try:
                    schdoc_file_json = schdoc_repo.get_generated_json(
                        schdoc_file, ref=schdoc_branch
                    )
                    all_components.extend(
                        extract_components_from_schdoc(schdoc_file_json)
                    )

                    break
                except NotYetGeneratedException:
                    if retry_count > 5:
                        print(
                            f"Failed to get {schdoc_path}, skipping...",
                            file=sys.stderr,
                        )
                        break

                    print(f"Failed to get {schdoc_path}, retrying...", file=sys.stderr)
                    time.sleep(1)
                    continue

    # Next, we'll need to map the designator in the SchDoc to the components we
    # have, as the PCB can have multiple components linked to a single
    # designator of the SchDoc.
    designator_to_component_map: dict[str, Component] = {
        component.designator: component for component in all_components
    }

    pcb_json = prjpcb_repo.get_generated_json(pcb_file, ref=prjpcb_branch)
    all_components = link_pcb_components(pcb_json, designator_to_component_map)

    # Components may or may not have part numbers. If they do, we consider all
    # designators with the same part number to be the sampe component. If they
    # don't, each component object is treated as a separate component.

    components_with_part_numbers = filter(
        lambda component: component.part_number is not None,
        all_components,
    )
    components_without_part_numbers = filter(
        lambda component: component.part_number is None,
        all_components,
    )

    components_by_part_number = defaultdict(list)
    for component in components_with_part_numbers:
        components_by_part_number[component.part_number].append(component)

    # Now, we'll generate the BOM rows. Each row is a list of strings, which
    # will be written to the CSV file.
    bom_rows = []
    for part_number, components in components_by_part_number.items():
        bom_rows.append(
            [
                components[0].description,
                ", ".join([component.designator for component in components]),
                len(components),
                components[0].manufacturer,
                part_number,
            ]
        )

    for component in components_without_part_numbers:
        bom_rows.append(
            [
                component.description,
                component.designator,
                1,
                component.manufacturer,
                None,
            ]
        )

    with ExitStack() as stack:
        if args.output_file is not None:
            f = stack.enter_context(open(args.output_file, "w"))
            writer = csv.writer(f)
        else:
            writer = csv.writer(sys.stdout)

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
