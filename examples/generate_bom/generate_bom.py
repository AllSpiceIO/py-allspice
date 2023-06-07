#! /usr/bin/env python3

# Generate a BOM from a PrjPcb file.
# For more information, read the README file in this directory.

import argparse
import csv
import os
import re
import sys

from allspice import AllSpice


def get_file_content(repo, file_path, branch):
    """
    Get the content of a file in a repo on a branch.
    """

    files_in_repo = repo.get_git_content(ref=branch)
    file = next((x for x in files_in_repo if x.path == file_path), None)
    if not file:
        raise ValueError(
            f"File {file_path} not found in repo {repo.name} on branch {branch.name}"
        )

    return repo.get_file_content(file, ref=branch)


def get_schdoc_list_from_prjpcb(prjpcb_file_content):
    """
    Get a list of SchDoc files from a PrjPcb file.
    """

    pattern = re.compile(r"DocumentPath=(.*?SchDoc)\r\n")
    return [match.group(1) for match in pattern.finditer(prjpcb_file_content)]


def extract_attributes_from_schdoc(schdoc_file_content):
    """
    Extract the attributes from a schdoc file. You can edit this function to get
    the attributes you want from the SchDoc file. To see what attributes are
    available, print the schdoc_file_content variable.
    """

    attributes_list = []

    for value in schdoc_file_content.values():
        attributes = value["attributes"]

        attributes_list.push(
            [
                attributes.get("Designator", {}).get("text"),
                attributes.get("MANUFACTURER", {}).get("text"),
                attributes.get("MANUFACTURER #", {}).get("text"),
            ]
        )

    return attributes_list


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
        help="The branch containing the SchDoc files. Defaults to main.",
        default="main",
    )
    parser.add_argument(
        "--allspice_hub_url",
        help="The URL of your AllSpice Hub instance. Defaults to https://hub.allspice.io.",
    )
    parser.add_argument(
        "--output_file",
        help="The path to the output file. If absent, the CSV will be output to the command line.",
        default=None,
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

    source_repo = args.source_repo
    source_file = args.source_file
    schdoc_repo = args.schdoc_repo if args.schdoc_repo is not None else source_repo
    source_branch = args.source_branch
    schdoc_branch = args.schdoc_branch

    # Get the PrjPcb file from the source repo.
    prjpcb_repo = allspice.get_repo(source_repo)
    prjpcb_branch = prjpcb_repo.get_branch(source_branch)
    prjpcb_file = get_file_content(prjpcb_repo, source_file, prjpcb_branch)
    schdoc_files_in_proj = {x for x in get_schdoc_list_from_prjpcb(prjpcb_file)}

    # Get the SchDoc files from the SchDoc repo.
    schdoc_repo = allspice.get_repo(schdoc_repo)
    schdoc_branch = schdoc_repo.get_branch(schdoc_branch)
    schdoc_files_in_repo = schdoc_repo.get_git_content(ref=schdoc_branch)

    bom_rows = []

    for schdoc_file in schdoc_files_in_repo:
        if schdoc_file.path in schdoc_files_in_proj:
            schdoc_file_json = schdoc_repo.get_generated_json(
                schdoc_file, ref=schdoc_branch
            )
            bom_rows.extend(extract_attributes_from_schdoc(schdoc_file_json))

    if args.output_file is not None:
        f = open(args.output_file, "w")
        writer = csv.writer(f)
    else:
        writer = csv.writer(sys.stdout)

    # If you're extracting more or fewer attributes, you can change the header
    # row here.
    writer.writerow(["Designator", "Manufacturer", "Manufacturer Part Number"])
    writer.writerows(bom_rows)
