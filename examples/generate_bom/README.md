# Examples: Generate a BOM and Compute COGS from a PrjDoc file

These script examples show you how to use the AllSpice client to generate a BOM
and then compute the COGS from an Altium PrjPcb file. 

## BOM Generation

To use the script, start by running:

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

### Customizing the Attributes Extracted by the BOM Script

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

## COGS Calculation

The COGS script depends on the BOM script. It takes a BOM CSV file and computes
the COGS at various quantities of PCBs made. The COGS is computed by looking up 
the part number using an API you define in the script via the
`fetch_price_for_part` method. An example is implemented using the cofactr API.

To use the script, start by running:

```bash
python3 compute_cogs.py -h
```

Which prints the following help text:

```
usage: compute_cogs.py [-h] [--quantities QUANTITIES]
                       [--output-file OUTPUT_FILE]
                       bom_file

positional arguments:
  bom_file              The path to the BOM file.

options:
  -h, --help            show this help message and exit
  --quantities QUANTITIES
                        A comma-separated list of quantities of PCBs to
                        compute the COGS for. E.g. 1,10,100,1000. Defaults to
                        the example.
  --output-file OUTPUT_FILE
                        The path to the output file. Defaults to stdout, i.e.
                        printing to the console.
```

If you have generated a BOM using `generate_bom.py`, you should first take a
look at the bom and remove rows for testpoints and other parts which don't need
to be in the COGS computation. This step is not strictly necessary, but will
make the COGS computation faster and more accurate, as the price lookup may get
confused by testpoints and other parts.

Once that is done, you can run:

```bash
python3 compute_cogs.py bom.csv --quantities 1,10,100,1000 --output-file cogs.csv
```

