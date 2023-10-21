from __future__ import annotations

from dataclasses import dataclass
import time
from typing import Union

from ..allspice import AllSpice
from ..apiobject import Content, Ref, Repository
from ..exceptions import NotYetGeneratedException


@dataclass
class PcbComponent:
    designator: str
    pins: list[ComponentPin]


@dataclass
class ComponentPin:
    designator: str
    net: str


@dataclass
class NetlistEntry:
    net: str
    pins: list[str]


Netlist = list[str]


def generate_netlist_for_altium(
    allspice_client: AllSpice,
    repository: Repository,
    pcbdoc_file: Union[Content, str],
    ref: Ref = "main",
) -> Netlist:
    """
    Generate a netlist for an Altium project.

    :param allspice_client: The AllSpice client to use.
    :param repository: The repository to generate the netlist for.
    :param pcbdoc_file: The Altium PCB document file. This can be a Content
        object returned by the AllSpice API, or a string containing the path to
        the file in the repo.
    :param ref: The ref, i.e. branch, commit or git ref from which to take the
        project files. Defaults to "main".
    :return: A list of netlist entries.
    """

    allspice_client.logger.info(
        f"Generating netlist for {repository.name=} on {ref=}"
    )
    allspice_client.logger.info(f"Fetching {pcbdoc_file=}")

    pcbdoc_components = _extract_all_pcbdoc_components(repository, ref, pcbdoc_file)

    return _group_netlist_entries(pcbdoc_components)


def _extract_all_pcbdoc_components(
    repository: Repository,
    ref: Ref,
    pcbdoc_file: str,
) -> list[PcbComponent]:
    """
    Extract all the components from a PcbDoc file in the repo.
    """

    components = []

    retry_count = 0
    while True:
        retry_count += 1
        try:
            pcb_json = repository.get_generated_json(pcbdoc_file, ref=ref)
            break
        except NotYetGeneratedException:
            if retry_count > 20:
                break
            # Wait a bit before retrying.
            time.sleep(0.5)
            continue

    for component in pcb_json["component_instances"].values():
        pins = []
        for pin in component["pads"].values():
            try:
                pins.append(ComponentPin(
                    designator=pin["designator"],
                    net=pin["net_name"]
                ))
            except KeyError:
                continue
        components.append(
            PcbComponent(
                designator=component["designator"],
                pins=pins)
        )

    return components


def _group_netlist_entries(components: list[PcbComponent]) -> dict[NetlistEntry]:
    """
    Group connected pins by the net
    """

    netlist_entries_by_net = {}

    for component in components:
        for pin in component.pins:
            if pin.net:
                netlist_entries_by_net.setdefault(pin.net, []).append(
                    component.designator + "." + str(pin.designator))
    return netlist_entries_by_net
