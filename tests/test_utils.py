import csv
import io
import os
import uuid

import pytest

from allspice import AllSpice
from allspice.utils.bom_generation import AttributesMapping, BomEntry, generate_bom_for_altium
from allspice.utils.netlist_generation import generate_netlist

test_repo = "repo_" + uuid.uuid4().hex[:8]

accept_outputs = bool(os.getenv('ACCEPT'))


@pytest.fixture(scope="session")
def port(pytestconfig):
    '''Load --port command-line arg if set'''
    return pytestconfig.getoption("port")


@pytest.fixture
def instance(port):
    try:
        g = AllSpice(
            f"http://localhost:{port}",
            open(".token", "r").read().strip(),
            ratelimiting=None,
        )
        print("AllSpice Hub Version: " + g.get_version())
        print("API-Token belongs to user: " + g.get_user().username)

        return g
    except Exception:
        assert (
            False
        ), f"AllSpice Hub could not load. Is there: \
                - an Instance running at http://localhost:{port} \
                - a Token at .token \
                    ?"


def _setup_for_generation(instance, test_name):
    # TODO: we should commit a smaller set of files in this repo so we don't depend on external data
    instance.requests_post(
        "/repos/migrate",
        data={
            "clone_addr": "https://hub.allspice.io/ProductDevelopmentFirm/ArchimajorDemo.git",
            "mirror": False,
            "repo_name": "-".join([test_repo, test_name]),
            "service": "git",
        },
    )


def _sort_function(x: BomEntry) -> str:
    ''' sort BOM list by this criteria'''
    if len(x.designators):
        return sorted(x.designators)[0]
    return "_" + x.part_number


def test_bom_generation(request, instance):
    _setup_for_generation(instance, request.node.name)
    repo = instance.get_repository(instance.get_user().username,
                                   "-".join([test_repo, request.node.name]))
    attributes_mapping = AttributesMapping(
        description=["PART DESCRIPTION"],
        designator=["Designator"],
        manufacturer=["Manufacturer", "MANUFACTURER"],
        part_number=["PART", "MANUFACTURER #"],
    )
    bom = generate_bom_for_altium(
        instance,
        repo,
        "Archimajor.PrjPcb",
        "Archimajor.PcbDoc",
        attributes_mapping,
        # We hard-code a ref so that this test is reproducible.
        ref="95719adde8107958bf40467ee092c45b6ddaba00",
    )
    assert len(bom) == 107

    output = io.StringIO()

    bom = [
        [
            bom_row.description,
            ", ".join(sorted(bom_row.designators)),
            bom_row.quantity,
            bom_row.manufacturer,
            bom_row.part_number,
        ]
        # Sort by designator
        for bom_row in sorted(bom, key=_sort_function)
    ]

    writer = csv.writer(output, lineterminator="/n")
    writer.writerows(bom)

    if accept_outputs:
        with open("tests/data/archimajor_bom_expected.csv", "w") as f:
            f.write(output.getvalue())

    with open("tests/data/archimajor_bom_expected.csv", "r") as f:
        assert output.getvalue() == f.read()


def test_netlist_generation(request, instance):
    _setup_for_generation(instance, request.node.name)
    repo = instance.get_repository(instance.get_user().username,
                                   "-".join([test_repo, request.node.name]))
    netlist = generate_netlist(
        instance,
        repo,
        "Archimajor.PcbDoc",
        # We hard-code a ref so that this test is reproducible.
        ref="95719adde8107958bf40467ee092c45b6ddaba00",
    )
    assert len(netlist) == 682

    nets = list(netlist.keys())

    nets.sort()

    with open("tests/data/archimajor_netlist_expected.net", "r") as f:
        for net in nets:
            assert (net + "\n") == f.readline()
            pins_on_net = netlist[net]
            pins_on_net.sort()
            assert (" " + " ".join(pins_on_net) + "\n") == f.readline()
