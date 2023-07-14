#! /usr/bin/env python3

# Add topics to repos.
# See the README file in this directory for details on how to run this script.

from argparse import ArgumentParser
import os
import sys

import yaml

from allspice import AllSpice, Repository

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "input_yaml",
        help="A YAML file as input. Read the README for more details.",
    )
    parser.add_argument(
        "--allspice_hub_url",
        help="The URL to AllSpice Hub. Defaults to hub.allspice.io",
        default="https://hub.allspice.io",
    )
    args = parser.parse_args()

    token = os.environ.get("ALLSPICE_AUTH_TOKEN")
    if token is None or token == "":
        print("Please set the ALLSPICE_AUTH_TOKEN environment variable.")
        sys.exit(1)

    with open(args.input_yaml, "r") as yaml_file:
        topics_to_repos = yaml.load(yaml_file.read(), yaml.SafeLoader)

    allspice_client = AllSpice(
        allspice_hub_url=args.allspice_hub_url,
        token_text=token,
    )

    for topic, repos in topics_to_repos.items():
        for repo in repos:
            print(f"Adding topic {topic} to repo {repo}:")
            try:
                owner, name = repo.split("/")
                repo_object = Repository.request(allspice_client, owner, name)
                repo_object.add_topic(topic)
                print("Added.")
            except Exception as e:
                print(f"Warning: topic add on {topic} for {repo} because {e}")

    print("Added all topics.")
