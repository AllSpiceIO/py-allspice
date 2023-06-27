# Example: Check if a Part is in a Schematic Library

This is an advanced example that checks every branch of a repository to see if:

1. It has a Schematic Document called "Main.SchDoc"
2. That Schematic Document contains a part with a given name

You can change the name of the SchDoc file it looks for via CLI args. This
example only works with py-allspice v2.0.0 and above.

One use case here could be to see if a repository is using a part that has since been
deprecated, or to find out which repositories are using a part that you want to update.

The example is in [this python script](./check_parts_in_libraries.py). To get started,
run:

```bash
python check_parts_in_libraries.py --help
```

As of writing, this produces the following output:

```
usage: check_parts_in_schematics.py [-h] [--schdoc_file SCHDOC_FILE] [--all]
                                    repo part manufacturer

positional arguments:
  repo                  The name of the repo, like orgname/reponame
  part                  The name of the part, like R198
  manufacturer          The name of the manufacturer, like Yageo

options:
  -h, --help            show this help message and exit
  --schdoc_file SCHDOC_FILE
                        The name of the schematic document, like Main.SchDoc.
  --all                 Check all schematic documents in the repo. If both
                        --schdoc_file and --allare specified, --schdoc_file
                        will be ignored.
```

Some examples of using it are:

```bash
python check_parts_in_schematics.py --all "AllSpiceUser/ArchimajorFork" "R198" "Yageo
```
