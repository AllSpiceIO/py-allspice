# Example: Generate a BOM from a PrjDoc file

This script example shows you how you can use the AllSpice client to generate
a BOM from a PrjDoc file. To use the script, start by running:

```bash
python3 generate_bom.py -h
```

As of writing, this generates the following help text:


```
usage: generate_bom [-h] [--schdoc_repo SCHDOC_REPO]
                    [--source_branch SOURCE_BRANCH]
                    [--schdoc_branch SCHDOC_BRANCH]
                    [--allspice_hub_url ALLSPICE_HUB_URL]
                    [--output_file OUTPUT_FILE]
                    source_repo source_file

Generate a BOM from a PrjPcb file.

positional arguments:
  source_repo           The repo containing the PrjPcb file.
  source_file           The path to the PrjPcb file in the source repo.

options:
  -h, --help            show this help message and exit
  --schdoc_repo SCHDOC_REPO
                        The repo containing the SchDoc files. Defaults to the
                        same repo as the PrjPcb file.
  --source_branch SOURCE_BRANCH
                        The branch containing the PrjPcb file. Defaults to
                        main.
  --schdoc_branch SCHDOC_BRANCH
                        The branch containing the SchDoc files. Defaults to
                        main.
  --allspice_hub_url ALLSPICE_HUB_URL
                        The URL of your AllSpice Hub instance. Defaults to
                        https://hub.allspice.io.
  --output_file OUTPUT_FILE
                        The path to the output file. If absent, the CSV will
                        be output to the command line.
```

Some examples of how you could run this are:

```bash
export ALLSPICE_AUTH_TOKEN= # some token

python3 generate_bom.py "test/test" "test.PrjPcb" # Note that the options are not required!

python3 generate_bom.py "test/test" "test.PrjPcb" --schdoc_repo "test/test_schdoc" --allspice_hub_url "https://my.selfhosted.example.org" --output_file bom.csv
```

You can also import this python file in another file to use the methods defined
in it. If you want the BOM in a different format, or have other requirements,
you can read and adapt this code, or use it as a reference for your own code.
