# Check Parts in Schematic Documents
# This example fetches all branches in a repo, and checks if any of them contain
# a certain part. If it does, it prints the branch name.
# For more information, read the README file in this directory.

import os
from argparse import ArgumentParser

from allspice import AllSpice, Branch, Repository
from allspice.exceptions import NotYetGeneratedException


def contains_part(
    repo: Repository,
    branch: Branch,
    part: str,
    manufacturer: str,
    part_library: str,
) -> bool:
    """
    Checks if a part is contained in a schematic document.

    :param repo: The repository to check.
    :param branch: The branch to check.
    :param part: The name of the part, like R198.
    :param manufacturer: The name of the manufacturer, like Yageo.
    :param part_library: The name of the part library, like Main.SchDoc.
    """

    try:
        json = repo.get_generated_json(part_library, branch)
        for value in json.values():
            if isinstance(value, dict):
                try:
                    attributes = value["attributes"]
                    if (
                        attributes["Designator"]["text"] == part
                        and attributes["MANUFACTURER"]["text"] == manufacturer
                    ):
                        return True
                except KeyError:
                    continue
    except NotYetGeneratedException:
        print(
            f"Note: The JSON for {part_library} has not yet been generated for "
            f"branch {branch.name}. Try this script again in some time."
        )

    return False


def check_all_schdoc_files(
    repo: Repository,
    branch: Branch,
    part: str,
    manufacturer: str,
) -> list[str]:
    """
    Checks if a part is contained in any schematic document in a repository.

    :param repo: The repository to check.
    :param branch: The branch to check.
    :param part: The name of the part, like R198.
    :param manufacturer: The name of the manufacturer, like Yageo.
    """

    files = repo.get_git_content(branch)
    schdoc_files = [file for file in files if file.path.endswith(".SchDoc")]

    matches = []
    for schdoc_file in schdoc_files:
        if contains_part(repo, branch, part, manufacturer, schdoc_file.path):
            matches.append(schdoc_file.path)

    return matches


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("repo", help="The name of the repo, like orgname/reponame")
    parser.add_argument("part", help="The name of the part, like R198")
    parser.add_argument("manufacturer", help="The name of the manufacturer, like Yageo")
    parser.add_argument(
        "--schdoc_file",
        help="The name of the schematic document, like Main.SchDoc.",
        default="Main.SchDoc",
    )
    parser.add_argument(
        "--all",
        help=(
            "Check all schematic documents in the repo. If both --schdoc_file "
            "and --all are specified, --schdoc_file will be ignored."
        ),
        action="store_true",
    )

    args = parser.parse_args()

    # Use Environment Variables to store your auth token. This keeps your token
    # secure when sharing code.
    auth_token = os.environ.get("ALLSPICE_AUTH_TOKEN")
    if auth_token is None:
        print("Please set the environment variable ALLSPICE_AUTH_TOKEN")
        exit(1)

    allspice = AllSpice(token_text=auth_token)
    repo_owner, repo_name = args.repo.split("/")
    repo = Repository.request(allspice, repo_owner, repo_name)

    found_at_least_one = False

    for branch in repo.get_branches():
        if args.all:
            matching_files = check_all_schdoc_files(
                repo,
                branch,
                args.part,
                args.manufacturer,
            )
            for file in matching_files:
                print(
                    f"Found {args.part} by Manufacturer {args.manufacturer} in "
                    f"{file} in Branch {branch.name}"
                )
                found_at_least_one = True
        else:
            if contains_part(
                repo,
                branch,
                args.part,
                args.manufacturer,
                args.part_library,
            ):
                print(
                    f"Found {args.part} by Manufacturer {args.manufacturer} in "
                    f"{args.part_library} in Branch {branch.name}"
                )
                found_at_least_one = True

    if found_at_least_one is not True:
        print("No matches found.")
    print("Done.")
