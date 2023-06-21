#! /usr/bin/env python3

# Generate a BOM from a PrjPcb file.
# For more information, read the README file in this directory.

import argparse
import base64
import csv
import os
import re
import sys
import time

from allspice import AllSpice
from allspice.exceptions import NotYetGeneratedException


def split_repo_name(name):
    """
    Split a repo name into a tuple of (owner, repo).
    """

    if "/" not in name:
        raise ValueError(f"Invalid repo name {name}")

    owner, repo = name.split("/")
    return owner, repo


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

    content = repo.get_file_content(file, ref=branch)
    return base64.b64decode(content).decode("utf-8")


def get_schdoc_list_from_prjpcb(prjpcb_file_content):
    """
    Get a list of SchDoc files from a PrjPcb file.
    """

    pattern = re.compile(r"DocumentPath=(.*?SchDoc)\r\n")
    return [match.group(1) for match in pattern.finditer(prjpcb_file_content)]


def extract_attributes_from_schdoc(schdoc_file_content, attributes_to_extract):
    """
    Extract all the components and their attributes from a schdoc file. You can
    edit this function to get the attributes you want from the SchDoc file. To
    see what attributes are available, print the schdoc_file_content variable.

    :param schdoc_file_content: The content of the SchDoc file. This should be
        a dictionary.

    :param attributes_to_extract: A list of attributes to extract. Note that if
        an attribute is not found for a component, its value will be None.
    """

    attributes_list = []

    for value in schdoc_file_content.values():
        try:
            if isinstance(value, dict):
                attributes = value["attributes"]

                current_attributes = []
                for attribute in attributes_to_extract:
                    current_attributes.append(attributes.get(attribute, {}).get("text"))

                attributes_list.append(current_attributes)

        except KeyError:
            continue

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

    if args.attributes_to_extract is not None:
        attributes_to_extract = args.attributes_to_extract.split(",")
    else:
        attributes_to_extract = ["Designator", "MANUFACTURER", "MANUFACTURER #"]

    source_repo_owner, source_repo_name = split_repo_name(args.source_repo)
    source_file = args.source_file
    if args.schdoc_repo is not None:
        schdoc_repo_owner, schdoc_repo_name = split_repo_name(args.schdoc_repo)
    else:
        schdoc_repo_owner = source_repo_owner
        schdoc_repo_name = source_repo_name
    source_branch = args.source_branch
    schdoc_branch = args.schdoc_branch if args.schdoc_branch else source_branch

    print("Generating BOM with the given arguements:")
    print(
        f"{source_repo_owner=} {source_repo_name=} {source_branch=} \
          {source_file=} {schdoc_repo_owner=} {schdoc_repo_name=} \
          {schdoc_branch=} {args.output_file=} {attributes_to_extract=}"
    )

    # Get the PrjPcb file from the source repo.
    prjpcb_repo = allspice.get_repository(source_repo_owner, source_repo_name)
    prjpcb_branch = prjpcb_repo.get_branch(source_branch)
    prjpcb_file = get_file_content(prjpcb_repo, source_file, prjpcb_branch)
    schdoc_files_in_proj = {x for x in get_schdoc_list_from_prjpcb(prjpcb_file)}

    print(f"{schdoc_files_in_proj=}")

    # Get the SchDoc files from the SchDoc repo.
    schdoc_repo = allspice.get_repository(schdoc_repo_owner, schdoc_repo_name)
    schdoc_branch = schdoc_repo.get_branch(schdoc_branch)
    schdoc_files_in_repo = schdoc_repo.get_git_content(ref=schdoc_branch)

    # Extract attributes from the SchDoc files. See thhe
    # `extract_attributes_from_schdoc` function for more information.
    bom_rows = []

    # Note: we're going through the files in the repo and checkin if they're
    # in the PrjPcb file. This may miss some files in the proj if they're
    # not in the repo. If you're seeing inconsistent or missing results,
    # check that all the SchDoc files are in the repo, or uncomment this line:

    # breakpoint()

    # And run the script. You'll be dropped into a debugger where you can
    # print() variables and see what's going on.
    for schdoc_file in schdoc_files_in_repo:
        if schdoc_file.path in schdoc_files_in_proj:
            # If the file is not yet generated, we'll retry a few times.
            retry_count = 0
            while True:
                retry_count += 1

                try:
                    schdoc_file_json = schdoc_repo.get_generated_json(
                        schdoc_file, ref=schdoc_branch
                    )
                    bom_rows.extend(
                        extract_attributes_from_schdoc(
                            schdoc_file_json, attributes_to_extract
                        )
                    )
                    break
                except NotYetGeneratedException:
                    if retry_count > 5:
                        print(f"Failed to get {schdoc_file.path}, skipping...")
                        break

                    print(f"Failed to get {schdoc_file.path}, retrying...")
                    time.sleep(1)
                    continue

    if args.output_file is not None:
        f = open(args.output_file, "w")
        writer = csv.writer(f)
    else:
        writer = csv.writer(sys.stdout)

    # If you're extracting more or fewer attributes, you can change the header
    # row here.
    writer.writerow(attributes_to_extract)
    writer.writerows(bom_rows)
