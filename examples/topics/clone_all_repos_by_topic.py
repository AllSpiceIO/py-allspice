#! /usr/bin/env python3

# Clone all repos by topic
# This script requires py-allspice v2.2.0 or later.

from argparse import ArgumentParser
import os
import subprocess

from allspice import AllSpice, Repository

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("topic", help="Topic to clone repos from")
    parser.add_argument("--allspice_url", help="URL of AllSpice server")

    args = parser.parse_args()

    token = os.environ.get("ALLSPICE_AUTH_TOKEN")
    if token is None:
        print("Please set the ALLSPICE_AUTH_TOKEN environment variable.")
        exit(1)

    if args.allspice_url is not None:
        allspice = AllSpice(allspice_hub_url=args.allspice_url, token_text=token)
    else:
        allspice = AllSpice(token_text=token)

    repos = Repository.search(allspice, args.topic, topic=True)

    if len(repos) == 0:
        print("No repos found with topic " + args.topic)
        exit(1)

    os.makedirs(args.topic, exist_ok=True)
    os.chdir(args.topic)

    for repo in repos:
        print("Cloning " + repo.name)
        subprocess.run(["git", "clone", repo.clone_url])
