from argparse import ArgumentParser
import os

from allspice import AllSpice, Repository

parser = ArgumentParser()
parser.add_argument("repo", help="The repo to backup")
parser.add_argument(
    "--ref",
    help="The ref to backup. This can be a branch name, a tag or a commit hash.",
    default="main",
)
parser.add_argument(
    "--output",
    help="The name of the output file. If not specified, the repo name will be used.",
)
parser.add_argument(
    "--format",
    help="The format of the output file. If not specified, the format will be zip.",
    choices=["zip", "tar.gz"],
    default="zip",
)

args = parser.parse_args()

allspice = AllSpice(os.environ["ALLSPICE_TOKEN"])
repo_owner, repo_name = args.repo.split("/")
repo = Repository.request(allspice, repo_owner, repo_name)

output_without_extension = args.output or f"{repo_owner}_{repo_name}_backup"
output = f"{output_without_extension}.{args.format}"

with open(output, "wb") as f:
    if args.format == "zip":
        archive_format = Repository.ArchiveFormat.ZIP
    elif args.format == "tar.gz":
        archive_format = Repository.ArchiveFormat.TAR
    data = repo.get_archive(args.ref, archive_format)
    f.write(data)

print(f"Successfully backed up {args.repo} to {output}")
