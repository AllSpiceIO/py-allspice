# Example: Generate a BOM from a PrjDoc file

This script example shows you how you can use the AllSpice client to generate
a BOM from an Altium PrjPcb file. To use the script, start by running:

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
                    source_repo source_file pcb_file

Generate a BOM from a PrjPcb file.

positional arguments:
  source_repo           The repo containing the PrjPcb file.
  source_file           The path to the PrjPcb file in the source repo.
  pcb_file              The path to the PCB file in the source repo.

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
                        the same branch as PrjPcb.
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

python3 generate_bom.py "test/test" "test.PrjPcb" "test.PcbDoc" 
# Note that the options are not required!

python3 generate_bom.py "test/test" "test.PrjPcb" --schdoc_repo "test/test_schdoc" --allspice_hub_url "https://my.selfhosted.example.org" --output_file bom.csv

python3 generate_bom.py "test/test" "test.PrjPcb" --attribute_list "Designator,Manufacturer" # Will only extract these two attributes
```

## Customizing the Attributes Extracted by this Script

This script relies on the presence of an `attributes_mapping.json` file next to
it. This file maps the Component Attributes in the SchDoc files to the columns
of the BOM. The example version of `attributes_mapping.json` is:

```json
{
    "description": ["PART DESCRIPTION"],
    "designator": ["Designator"],
    "manufacturer": ["Manufacturer", "MANUFACTURER"],
    "part_number": ["PART", "MANUFACTURER #"]
}
```

In this file, the keys are the names of the columns in the BOM, and the values
are a list of the names of the attributes in the SchDoc files that should be
mapped to that column. For example, if your part number is stored either in the
`PART` or `MANUFACTURER #` attribute, you would add both of those to the list.
If there is only one attribute, you can omit the list and just use a string. The
script checks these attributes in order, and uses the _first_ one it finds. So
if both `PART` and `MANUFACTURER #` are defined, it will use `PART`.

If you need to customize the attributes further or have more complex logic,
customize the `map_json_to_component` function in the script. Note that the
AllSpice generated JSON may change at any time, so everything except the
component attributes may change!

You can also import this python file in another file to use the methods defined
in it. If you want the BOM in a different format, or have other requirements,
you can read and adapt this code, or use it as a reference for your own code.
