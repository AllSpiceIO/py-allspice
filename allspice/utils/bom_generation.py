from __future__ import annotations

import configparser
from dataclasses import dataclass
import pathlib
import re
import sys
import time
from typing import Optional, Union

from ..allspice import AllSpice
from ..apiobject import Ref, Repository
from ..exceptions import NotYetGeneratedException

REPETITIONS_REGEX = re.compile(r"Repeat\(\w+,(\d+),(\d+)\)")


@dataclass
class SchematicComponent:
    description: Optional[str]
    manufacturer: Optional[str]
    part_number: Optional[str]
    designator: Optional[str]


@dataclass
class BomEntry:
    description: str
    manufacturer: str
    part_number: str
    designators: list[str]
    quantity: int


Bom = list[BomEntry]


@dataclass
class AttributesMapping:
    """
    Define how we map from attributes in the Altium SchDoc file to the fields of
    the BOM.

    For each field, we define a list of attribute names that we will check in
    the Altium SchDoc file. The *first* one found defined will be used.

    :param description: A list of attribute names in the Altium SchDoc file
        that contain the description of the part.
    :param manufacturer: A list of attribute names in the Altium SchDoc file
        that contain the manufacturer of the part.
    :param part_number: A list of attribute names in the Altium SchDoc file
        that contain the part number of the part.
    :param designator: A list of attribute names in the Altium SchDoc file
        that contain the designator of the part.
    """

    description: list[str]
    manufacturer: list[str]
    part_number: list[str]
    designator: list[str]

    @staticmethod
    def from_dict(dictionary: dict[str, list[str]]) -> AttributesMapping:
        """
        Create an AttributesMapping from a dictionary.

        Example Input::

            {
                "description": ["Description"],
                "manufacturer": ["Manufacturer", "MANUFACTURER"],
                "part_number": ["Part Number"],
                "designator": ["Designator"],
            }
        """
        return AttributesMapping(
            description=dictionary["description"],
            manufacturer=dictionary["manufacturer"],
            part_number=dictionary["part_number"],
            designator=dictionary["designator"],
        )


def generate_bom_for_altium(
    allspice_client: AllSpice,
    repository: Repository,
    prjpcb_file: str,
    attributes_mapping: AttributesMapping,
    ref: Ref = "main",
) -> Bom:
    """
    Generate a BOM for an Altium project.

    :param allspice_client: The AllSpice client to use.
    :param repository: The repository to generate the BOM for.
    :param prjpcb_file: The Altium project file. This can be a Content object
        returned by the AllSpice API, or a string containing the path to the
        file in the repo.
    :param attributes_mapping: A mapping of Altium attributes to BOM entry
        attributes. See the documentation for AttributesMapping for more
        information.
    :param ref: The ref, i.e. branch, commit or git ref from which to take the
        project files. Defaults to "main".
    :return: A list of BOM entries.
    """

    allspice_client.logger.info(
        f"Generating BOM for {repository.get_full_name()=} on {ref=} using {attributes_mapping=}"
    )
    allspice_client.logger.info(f"Fetching {prjpcb_file=}")

    # Altium adds the Byte Order Mark to UTF-8 files, so we need to decode the
    # file content with utf-8-sig to remove it.
    prjpcb_file_contents = repository.get_raw_file(prjpcb_file, ref=ref).decode("utf-8-sig")
    schdoc_files_in_proj = _extract_schdoc_list_from_prjpcb(prjpcb_file_contents)
    allspice_client.logger.info("Found %d SchDoc files", len(schdoc_files_in_proj))

    schdoc_jsons = {
        schdoc_file: _fetch_generated_json(
            repository,
            _resolve_prjpcb_relative_path(schdoc_file, prjpcb_file),
            ref,
        )
        for schdoc_file in schdoc_files_in_proj
    }
    schdoc_entries = {
        schdoc_file: [value for value in schdoc_json.values() if isinstance(value, dict)]
        for schdoc_file, schdoc_json in schdoc_jsons.items()
    }
    schdoc_refs = {
        schdoc_file: [entry for entry in entries if entry.get("type") == "SheetRef"]
        for schdoc_file, entries in schdoc_entries.items()
    }
    independent_sheets, hierarchy = _build_schdoc_hierarchy(schdoc_refs)

    components = []

    for independent_sheet in independent_sheets:
        components.extend(
            _extract_components(
                independent_sheet,
                schdoc_entries,
                hierarchy,
                attributes_mapping,
            )
        )

    bom = _group_components(components)

    return bom


def _find_first_matching_key(
    alternatives: Union[list[str], str],
    attributes: dict,
) -> Optional[str]:
    """
    Search for a series of alternative keys in a dictionary, and return the
    value of the first one found.
    """

    if isinstance(alternatives, str):
        alternatives = [alternatives]

    for alternative in alternatives:
        if alternative in attributes:
            return attributes[alternative]["text"]

    return None


def _extract_schdoc_list_from_prjpcb(prjpcb_file_content) -> set[str]:
    """
    Get a list of SchDoc files from a PrjPcb file.
    """

    prjcpb_data = configparser.ConfigParser()
    prjcpb_data.read_string(prjpcb_file_content)

    return {
        section["DocumentPath"]
        for (_, section) in prjcpb_data.items()
        if "DocumentPath" in section and section["DocumentPath"].endswith(".SchDoc")
    }


def _resolve_prjpcb_relative_path(schdoc_path: str, prjpcb_path: str) -> str:
    """
    Convert a relative path to the SchDoc file to an absolute path from the git
    root based on the path to the PrjPcb file.
    """

    # The paths in the PrjPcb file are Windows paths, and ASH will store the
    # paths as Posix paths. We need to resolve the SchDoc path relative to the
    # PrjPcb path (which is a Posix Path, since it is from ASH), and then
    # convert the result into a posix path as a string for use in ASH.
    schdoc = pathlib.PureWindowsPath(schdoc_path)
    prjpcb = pathlib.PurePosixPath(prjpcb_path)
    return (prjpcb.parent / schdoc).as_posix()


def _fetch_generated_json(repo: Repository, file_path: str, ref: Ref) -> dict:
    attempts = 0
    while attempts < 5:
        try:
            return repo.get_generated_json(file_path, ref=ref)
        except NotYetGeneratedException:
            print(
                f"JSON for {file_path} is not yet generated. Retrying in 0.5s.",
                file=sys.stderr,
            )
            time.sleep(0.5)

    print(
        f"Failed to fetch JSON for {file_path} after 5 attempts; quitting.",
        file=sys.stderr,
    )
    sys.exit(1)


def _build_schdoc_hierarchy(
    sheets_to_refs: dict[str, list[dict]],
) -> tuple[set[str], dict[str, list[tuple[str, int]]]]:
    """
    Build a hierarchy of sheets from a mapping of sheet names to the references
    of their children.

    The output of this function is a tuple of two values:

    1. A set of "independent" sheets, which can be taken to be roots of the
    hierarchy.

    2. A mapping of each sheet that has children to a list of tuples, where each
    tuple is a child sheet and the number of repetitions of that child sheet in
    the parent sheet. If a sheet has no children and is not a child of any other
    sheet, it will be mapped to an empty list.
    """

    hierarchy = {}

    # We start by assuming all sheets are independent.
    independent_sheets = set(sheets_to_refs.keys())
    # This is what we'll use to compare with the sheet names in repetitions.
    sheet_names_downcased = {sheet.lower(): sheet for sheet in independent_sheets}

    for parent_sheet, refs in sheets_to_refs.items():
        if not refs or len(refs) == 0:
            continue

        repetitions = _extract_repetitions(refs)
        for child_sheet, count in repetitions.items():
            child_path = _resolve_child_relative_path(child_sheet, parent_sheet)
            child_name = sheet_names_downcased[child_path.lower()]
            if parent_sheet in hierarchy:
                hierarchy[parent_sheet].append((child_name, count))
            else:
                hierarchy[parent_sheet] = [(child_name, count)]
            independent_sheets.discard(child_name)

    return (independent_sheets, hierarchy)


def _resolve_child_relative_path(child_path: str, parent_path: str) -> str:
    """
    Converts a relative path in a sheet ref to a relative path from the prjpcb
    file.
    """

    child = pathlib.PureWindowsPath(child_path)
    parent = pathlib.PureWindowsPath(parent_path)

    return str(parent.parent / child)


def _extract_repetitions(sheet_refs: list[dict]) -> dict[str, int]:
    repetitions = {}
    for sheet_ref in sheet_refs:
        sheet_name = sheet_ref["sheet_name"]["name"]
        sheet_file_name = sheet_ref["filename"]
        if match := REPETITIONS_REGEX.search(sheet_name):
            count = int(match.group(2)) - int(match.group(1)) + 1
            if sheet_file_name in repetitions:
                repetitions[sheet_file_name] += count
            else:
                repetitions[sheet_file_name] = count
        else:
            if sheet_file_name in repetitions:
                repetitions[sheet_file_name] += 1
            else:
                repetitions[sheet_file_name] = 1
    return repetitions


def _schdoc_component_from_attributes(
    attributes: dict,
    mapper: AttributesMapping,
) -> SchematicComponent:
    """
    Make a SchDoc Component object out of the JSON for it in the SchDoc file.

    :param attributes: The attributes for the component in the SchDoc
    :param mapper: An AttributesMapping object, see the documentation for
        AttributesMapping for more information.
    :returns: A SchodocComponent object representing that component.
    """

    return SchematicComponent(
        description=_find_first_matching_key(mapper.description, attributes),
        designator=_find_first_matching_key(mapper.designator, attributes) or "",
        manufacturer=_find_first_matching_key(mapper.manufacturer, attributes),
        part_number=_find_first_matching_key(mapper.part_number, attributes),
    )


def _letters_for_repetition(rep: int) -> str:
    """
    Generate the letter suffix for a repetition number. If the repetition is
    more than 26, the suffix will be a combination of letters.
    """

    first = ord("A")
    suffix = ""

    while rep > 0:
        u = (rep - 1) % 26
        letter = chr(u + first)
        suffix = letter + suffix
        rep = (rep - u) // 26

    return suffix


def _append_designator_letters(
    component: SchematicComponent,
    repetitions: int,
) -> list[SchematicComponent]:
    """
    Append a letter to the designator of each component in a list of components
    based on the number of repetitions of each component in the parent sheet.
    """

    if repetitions == 1:
        return [component]

    return [
        SchematicComponent(
            description=component.description,
            manufacturer=component.manufacturer,
            part_number=component.part_number,
            designator=f"{component.designator}{_letters_for_repetition(i)}",
        )
        for i in range(1, repetitions + 1)
    ]


def _extract_components(
    sheet_name: str,
    sheets_to_entries: dict[str, list[dict]],
    hierarchy: dict[str, list[tuple[str, int]]],
    attributes_mapping: AttributesMapping,
) -> list[SchematicComponent]:
    components = []
    if sheet_name not in sheets_to_entries:
        return components

    for entry in sheets_to_entries[sheet_name]:
        if entry["type"] != "Component":
            continue

        component = _schdoc_component_from_attributes(
            entry["attributes"],
            attributes_mapping,
        )
        components.append(component)

    if sheet_name not in hierarchy:
        return components

    for child_sheet, count in hierarchy[sheet_name]:
        child_components = _extract_components(
            child_sheet,
            sheets_to_entries,
            hierarchy,
            attributes_mapping,
        )
        if count > 1:
            for component in child_components:
                components.extend(_append_designator_letters(component, count))
        else:
            components.extend(child_components)

    return components


def _group_components(components: list[SchematicComponent]) -> Bom:
    grouped_components = {}

    for component in components:
        key = component.part_number
        if key in grouped_components:
            grouped_components[key].append(component)
        else:
            grouped_components[key] = [component]

    rows = []

    for part_number, components in grouped_components.items():
        row = BomEntry(
            description=str(components[0].description),
            manufacturer=str(components[0].manufacturer),
            designators=[str(component.designator) for component in components],
            part_number=part_number,
            quantity=len(components),
        )
        rows.append(row)

    return rows
