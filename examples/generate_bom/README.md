# Example: Generate a BOM from a PrjDoc file

These scripts are examples of how you can use py-allspices BOM generation
utilities to generate a BOM and then compute the Cost of Goods Sold from that.
These scripts are just examples and may need to be adapted to your specific use
case.

## BOM Generation

The `generate_bom.py` script wraps the BOM generation utilities in py-allspice
with a command line interface. It takes a repository, the path to the PrjPcb
file in that repository and JSON file for the columns to generate a BOM CSV
file.

To use the script, start by running:

```bash
python3 generate_bom.py -h
```

As of writing, this generates the following help text:

```
usage: generate_bom [-h] [--columns COLUMNS] [--source_ref SOURCE_REF]
                    [--allspice_hub_url ALLSPICE_HUB_URL] [--output_file OUTPUT_FILE]
                    [--group_by GROUP_BY]
                    repository prjpcb_file

Generate a BOM from a PrjPcb file.

positional arguments:
  repository            The repo containing the project in the form 'owner/repo'
  prjpcb_file           The path to the PrjPcb file in the source repo.

options:
  -h, --help            show this help message and exit
  --columns COLUMNS     A path to a JSON file mapping columns to the attributes they are from.
                        See the README for more details. Defaults to 'columns.json'.
  --source_ref SOURCE_REF
                        The git reference the BOM should be generated for (eg. branch name, tag
                        name, commit SHA). Defaults to the main branch.
  --allspice_hub_url ALLSPICE_HUB_URL
                        The URL of your AllSpice Hub instance. Defaults to
                        https://hub.allspice.io.
  --output_file OUTPUT_FILE
                        The path to the output file. If absent, the CSV will be output to the
                        command line.
  --group_by GROUP_BY   A comma-separated list of columns to group the BOM by. If not present,
                        the BOM will be flat.
```

Some examples of how you could run this are:

```bash
export ALLSPICE_AUTH_TOKEN= # some token

python3 generate_bom.py "test/test" "test.PrjPcb" # Note that the options are not required!

python3 generate_bom.py "test/test" "test.PrjPcb" --allspice_hub_url "https://my.selfhosted.example.org" --output_file bom.csv
```

### Customizing the Attributes Extracted by the BOM Script

This script relies on a `columns.json` file. This file maps the Component
Attributes in the SchDoc files to the columns of the BOM. An example for
`columns.json` is:

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

Note that py-allspice also adds two attributes: `_part_id` and `_description`.
These correspond to the Library Reference and description fields of the
component. The underscore is added ahead of the name to prevent these additional
attributes from overriding any of your own. You can use these like:

```json
{
  "Description": ["PART DESCRIPTION", "_description"],
  "Part Number": ["PART", "_part_id"]
}
```

By default, the script picks up a `columns.json` file from the working
directory. If you want to keep it in a different place, or rename it, you can
pass the `--columns` argument to the script to specify where it is.

## Cost of Goods Sold

The `compute_cogs.py` script takes a BOM, fetches prices for the components
using the cofactr API and computes the Cost of Goods Sold for the project. It
requires a cofactr API key. You can use this script as an example for your own
script to compute COGS based on your own API or other data source.
