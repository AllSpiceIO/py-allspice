# Example: Generate a BOM from a PrjDoc file

These scripts are examples of how you can use py-allspices BOM generation
utilities to generate a BOM and then compute the Cost of Goods Sold from that.
These scripts are just examples and may need to be adapted to your specific use
case.

## BOM Generation

The `generate_bom.py` script wraps the BOM generation utilities in py-allspice
with a command line interface. It takes a PrjPcb file and a PcbDoc file and
generates a BOM CSV file.

To use the script, start by running:

```bash
python3 generate_bom.py -h
```

As of writing, this generates the following help text:

```
usage: generate_bom [-h] [--source_ref SOURCE_REF]
                    [--allspice_hub_url ALLSPICE_HUB_URL]
                    [--output_file OUTPUT_FILE]
                    repository prjpcb_file pcb_file

Generate a BOM from a PrjPcb file.

positional arguments:
  repository            The repo containing the project
  prjpcb_file           The path to the PrjPcb file in the source repo.
  pcb_file              The path to the PCB file in the source repo.

options:
  -h, --help            show this help message and exit
  --source_ref SOURCE_ref
                        The git reference the netlist should be generated for (eg. branch name, tag name, commit SHA). Defaults to main.
  --allspice_hub_url ALLSPICE_HUB_URL
                        The URL of your AllSpice Hub instance. Defaults to
                        https://hub.allspice.io.
  --output_file OUTPUT_FILE
                        The path to the output file. If absent, the CSV will be
                        output to the command line.
```

Some examples of how you could run this are:

```bash
export ALLSPICE_AUTH_TOKEN= # some token

python3 generate_bom.py "test/test" "test.PrjPcb" # Note that the options are not required!

python3 generate_bom.py "test/test" "test.PrjPcb" "test.PcbDoc" --allspice_hub_url "https://my.selfhosted.example.org" --output_file bom.csv
```

### Customizing the Attributes Extracted by the BOM Script

This script relies on the presence of an `attributes_mapping.json` file in the
working directory. This file maps the Component Attributes in the SchDoc files
to the columns of the BOM. The example version of `attributes_mapping.json` is:

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

## Cost of Goods Sold

The `compute_cogs.py` script takes a BOM, fetches prices for the components
using the cofactr API and computes the Cost of Goods Sold for the project. It
requires a cofactr API key. You can use this script as an example for your own
script to compute COGS based on your own API or other data source.
