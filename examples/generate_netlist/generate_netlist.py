#! /usr/bin/env python3

# Generate a Netlist from a PcbDoc file.
# For more information, read the README file in this directory.

import argparse
import os
import sys
from contextlib import ExitStack

from allspice import AllSpice
from allspice.utils.netlist_generation import generate_netlist


if __name__ == "__main__":
    # Parse command line arguments. If you're writing a special purpose script,
    # you can hardcode these values instead of using command line arguments.
    parser = argparse.ArgumentParser(
        prog="generate_pcb_netlist", description="Generate a netlist from a PCB file."
    )
    parser.add_argument("repository", help="The repo containing the project")
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
        help="The path to the output file. If absent, the output will direct to the command line.",
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
    pcb_file = args.pcb_file

    print("Generating PCB Netlist...", file=sys.stderr)

    netlist_rows = generate_netlist(
        allspice,
        repository,
        pcb_file,
        args.source_ref,
    )

    with ExitStack() as stack:
        if args.output_file is not None:
            writer = stack.enter_context(open(args.output_file, "w"))
        else:
            writer = sys.stdout

        nets = list(netlist_rows.keys())

        # It's helpful to sort here to generate repeatable netlist files
        nets.sort()

        # You can change formatting here
        for net in nets:
            writer.write(net + "\n")
            pins_on_net = netlist_rows[net]
            pins_on_net.sort()
            writer.write(" " + " ".join(pins_on_net) + "\n")

    print("Generated PCB netlist.", file=sys.stderr)
