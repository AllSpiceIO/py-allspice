# cspell:ignore jsons

import configparser
import functools
import pathlib
import re
import time
from enum import Enum
from logging import Logger
from typing import Optional

from ..allspice import AllSpice
from ..apiobject import Ref, Repository
from ..exceptions import NotYetGeneratedException

SLEEP_FOR_GENERATED_JSON = 0.5
"""The amount of time to sleep between attempts to fetch generated JSON files."""

PCB_FOOTPRINT_ATTR_NAME = "PCB Footprint"

PART_REFERENCE_ATTR_NAME = "Part Reference"
"""The name of the part reference attribute in OrCAD projects."""

REPETITIONS_REGEX = re.compile(r"Repeat\(\w+,(\d+),(\d+)\)")

DESIGNATOR_COLUMN_NAME = "Designator"
"""The name of the designator attribute in Altium projects."""

# Maps a sheet name to a list of tuples, where each tuple is a child sheet and
# the number of repetitions of that child sheet in the parent sheet.
SchdocHierarchy = dict[str, list[tuple[str, int]]]
ComponentAttributes = dict[str, str]


class SupportedTool(Enum):
    """
    ECAD tools supported by list_components.
    """

    ALTIUM = "altium"
    ORCAD = "orcad"
    SYSTEM_CAPTURE = "system_capture"


class VariationKind(Enum):
    FITTED_MOD_PARAMS = 0
    NOT_FITTED = 1
    ALT_COMP = 2


def list_components(
    allspice_client: AllSpice,
    repository: Repository,
    source_file: str,
    variant: Optional[str] = None,
    ref: Ref = "main",
    combine_multi_part: bool = False,
    design_reuse_repos: list[Repository] = [],
) -> list[ComponentAttributes]:
    """
    Get a list of all components in a schematic.


    Note that special attributes are added by this function depending on
    the project tool. For Altium projects, these are "_part_id",
    "_description", "_unique_id" and "_kind", which are the Library
    Reference, Description, Unique ID and Component Type respectively. For
    OrCAD and System Capture projects, "_name" is added, which is the name
    of the component, and "_reference" and "_logical_reference" may be
    added, which are the name of the component, and the logical reference
    of a multi-part component respectively.

    :param client: An AllSpice client instance.
    :param repository: The repository containing the schematic.
    :param source_file: The path to the schematic file from the repo root. The
        source file must be a PrjPcb file for Altium projects, a DSN file for
        OrCAD projects or an SDAX file for System Capture projects. For
        example, if the schematic is in the folder "Schematics" and the file is
        named "example.DSN", the path would be "Schematics/example.DSN".
    :param variant: The variant to apply to the components. If not None, the
        components will be filtered and modified according to the variant. Only
        applies to Altium projects.
    :param ref: Optional git ref to check. This can be a commit hash, branch
        name, or tag name. Default is "main", i.e. the main branch.
    :param combine_multi_part: If True, multi-part components will be combined
        into a single component.
    :return: A list of all components in the schematic. Each component is a
        dictionary with the keys being the attributes of the component and the
        values being the values of the attributes.
    """

    project_tool = infer_project_tool(source_file)
    match project_tool:
        case SupportedTool.ALTIUM:
            return list_components_for_altium(
                allspice_client,
                repository,
                source_file,
                variant=variant,
                ref=ref,
                combine_multi_part=combine_multi_part,
                design_reuse_repos=design_reuse_repos,
            )
        case SupportedTool.ORCAD:
            if variant:
                raise ValueError("Variant is not supported for OrCAD projects.")

            return list_components_for_orcad(
                allspice_client,
                repository,
                source_file,
                ref=ref,
                combine_multi_part=combine_multi_part,
            )
        case SupportedTool.SYSTEM_CAPTURE:
            if variant:
                raise ValueError("Variant is not supported for System Capture projects.")

            return list_components_for_system_capture(
                allspice_client,
                repository,
                source_file,
                ref=ref,
            )


def list_components_for_altium(
    allspice_client: AllSpice,
    repository: Repository,
    prjpcb_file: str,
    variant: Optional[str] = None,
    ref: Ref = "main",
    combine_multi_part: bool = False,
    design_reuse_repos: list[Repository] = [],
) -> list[ComponentAttributes]:
    """
    Get a list of all components in an Altium project.

    :param client: An AllSpice client instance.
    :param repository: The repository containing the Altium project.
    :param prjpcb_file: The path to the PrjPcb file from the repo root. For
        example, if the PrjPcb file is in the folder "Project" and the file
        is named "example.prjpcb", the path would be "Project/example.prjpcb".
    :param variant: The variant to apply to the components. If not None, the
        components will be filtered and modified according to the variant.
    :param ref: Optional git ref to check. This can be a commit hash, branch
        name, or tag name. Default is "main", i.e. the main branch.
    :param combine_multi_part: If True, multi-part components will be combined
        into a single component.
    :return: A list of all components in the Altium project. Each component is
        a dictionary with the keys being the attributes of the component and the
        values being the values of the attributes. Additionally, `_part_id`,
        `_description`, `_unique_id`, and `_kind` attributes are added to each
        component to store the Library Reference, Description, Unique ID, and
        Component Type respectively.
    """

    allspice_client.logger.info(f"Fetching {prjpcb_file=}")

    # Altium adds the Byte Order Mark to UTF-8 files, so we need to decode the
    # file content with utf-8-sig to remove it.
    prjpcb_file_contents = repository.get_raw_file(prjpcb_file, ref=ref).decode("utf-8-sig")

    prjpcb_ini = configparser.ConfigParser()
    prjpcb_ini.read_string(prjpcb_file_contents)

    if variant is not None:
        try:
            variant_details = _extract_variations(variant, prjpcb_ini)
        except ValueError:
            raise ValueError(
                f"Variant {variant} not found in PrjPcb file. "
                "Please check the name of the variant."
            )
    else:
        # Ensuring variant_details is always bound, even if it is not used.
        variant_details = None

    project_documents, device_sheets = _extract_schdoc_list_from_prjpcb(prjpcb_ini)
    allspice_client.logger.info("Found %d SchDoc files", len(project_documents))
    allspice_client.logger.info("Found %d Device Sheet files", len(device_sheets))

    # Mapping of schdoc file paths from the project file to their JSON
    schdoc_jsons: dict[str, dict] = {}
    # Mapping of device sheet *names* to their JSON.
    device_sheet_jsons: dict[str, dict] = {}

    # When working with Device Sheets, there are three different paths to keep
    # in mind:
    #
    # 1. The path as given in the PrjPcb file: Used to find a possible match in
    #    the current repo, e.g. if it is a monorepo. If not found, we get the
    #    basename and use that to match in the design reuse repos, yielding (2)
    #    after which this is no longer used.
    # 2. The path of the file in the design reuse repository: Used for fetching
    #    the JSON, after which this is no longer used.
    # 3. The name stored in the `filename` property of the SheetRef: This is the
    #    stem of the path. We need to match a SheetRef to the device sheet it is
    #    referring to using this, which is why `device_sheet_jsons` uses these
    #    as the keys.

    for schdoc_file in project_documents:
        schdoc_path_from_repo_root = _resolve_prjpcb_relative_path(schdoc_file, prjpcb_file)

        schdoc_json = _fetch_generated_json(
            repository,
            schdoc_path_from_repo_root,
            ref,
        )
        schdoc_jsons[schdoc_path_from_repo_root] = schdoc_json

    for device_sheet in device_sheets:
        device_sheet_repo, device_sheet_path = _find_device_sheet(
            device_sheet,
            repository,
            prjpcb_file,
            design_reuse_repos,
            allspice_client.logger,
        )
        device_sheet_json = _fetch_generated_json(
            device_sheet_repo,
            device_sheet_path.as_posix(),
            # Note the default branch here - we can't assume the same ref is
            # available.
            device_sheet_repo.default_branch,
        )
        device_sheet_jsons[device_sheet_path.stem] = device_sheet_json

    independent_sheets, hierarchy = _build_schdoc_hierarchy(schdoc_jsons, device_sheet_jsons)

    allspice_client.logger.debug("Independent sheets: %s", independent_sheets)
    allspice_client.logger.debug("Hierarchy: %s", hierarchy)

    # Now we can build a combined mapping of documents and device sheets:
    sheets_to_components = {}
    for schdoc_file, schdoc_json in schdoc_jsons.items():
        schdoc_components = [
            value
            for value in schdoc_json.values()
            if isinstance(value, dict) and value.get("type") == "Component"
        ]
        sheets_to_components[schdoc_file] = schdoc_components
    for device_sheet_name, device_sheet_json in device_sheet_jsons.items():
        device_sheet_components = [
            value
            for value in device_sheet_json.values()
            if isinstance(value, dict) and value.get("type") == "Component"
        ]
        sheets_to_components[device_sheet_name] = device_sheet_components

    components = []

    for independent_sheet in independent_sheets:
        components.extend(
            _extract_components(
                independent_sheet,
                sheets_to_components,
                hierarchy,
            )
        )

    if combine_multi_part:
        # Multi part components must be combined *after* we've processed
        # repetitions and before we apply variations. This is because each
        # repetition of a multi-part component is treated as a separate
        # component, and they can be present across sheets. We need to combine
        # them into a single component before applying variations, as Altium
        # variations will apply to the combined component.
        components = _combine_multi_part_components_for_altium(components)

    if variant is not None:
        if variant_details is None:
            # This should never happen, but mypy doesn't know that.
            raise ValueError(f"Variant {variant} not found in PrjPcb file.")

        components = _apply_variations(components, variant_details, allspice_client.logger)

    return _filter_blank_components(components, allspice_client.logger)


def list_components_for_orcad(
    allspice_client: AllSpice,
    repository: Repository,
    dsn_path: str,
    ref: Ref = "main",
    combine_multi_part: bool = False,
) -> list[ComponentAttributes]:
    """
    Get a list of all components in an OrCAD DSN schematic.

    :param client: An AllSpice client instance.
    :param repository: The repository containing the OrCAD schematic.
    :param dsn_path: The path to the OrCAD DSN file from the repo root. For
        example, if the schematic is in the folder "Schematics" and the file
        is named "example.dsn", the path would be "Schematics/example.dsn".
    :param ref: Optional git ref to check. This can be a commit hash, branch
        name, or tag name. Default is "main", i.e. the main branch.
    :param combine_multi_part: If True, multi-part components will be combined
        into a single component.
    :return: A list of all components in the OrCAD schematic. Each component is
        a dictionary with the keys being the attributes of the component and the
        values being the values of the attributes. A `_name` attribute is added
        to each component to store the name of the component.
    """

    components = _list_components_multi_page_schematic(allspice_client, repository, dsn_path, ref)

    if combine_multi_part:
        components = _combine_multi_part_components_for_orcad(components)

    return components


def list_components_for_system_capture(
    allspice_client: AllSpice,
    repository: Repository,
    sdax_path: str,
    ref: Ref = "main",
) -> list[ComponentAttributes]:
    """
    Get a list of all components in a System Capture SDAX schematic.

    :param client: An AllSpice client instance.
    :param repository: The repository containing the System Capture schematic.
    :param sdax_path: The path to the System Capture SDAX file from the repo
        root. For example, if the schematic is in the folder "Schematics" and
        the file is named "example.sdax", the path would be
        "Schematics/example.sdax".
    :param ref: Optional git ref to check. This can be a commit hash, branch
        name, or tag name. Default is "main", i.e. the main branch.
    """

    return _list_components_multi_page_schematic(allspice_client, repository, sdax_path, ref)


def infer_project_tool(source_file: str) -> SupportedTool:
    """
    Infer the ECAD tool used in a project from the file extension.
    """

    if source_file.lower().endswith(".prjpcb"):
        return SupportedTool.ALTIUM
    elif source_file.lower().endswith(".dsn"):
        return SupportedTool.ORCAD
    elif source_file.lower().endswith(".sdax"):
        return SupportedTool.SYSTEM_CAPTURE
    else:
        raise ValueError("""
The source file for generate_bom must be:

- A PrjPcb file for Altium projects; or
- A DSN file for OrCAD projects; or
- An SDAX file for System Capture projects.
        """)


def _list_components_multi_page_schematic(
    allspice_client: AllSpice,
    repository: Repository,
    schematic_path: str,
    ref: Ref,
) -> list[dict[str, str]]:
    """
    Internal function for getting all components from a multi-page schematic.

    This pattern is followed by OrCAD and System Capture, and potentially other
    formats in the future.
    """

    allspice_client.logger.debug(
        f"Listing components in {schematic_path=} from {repository.get_full_name()} on {ref=}"
    )

    # Get the generated JSON for the schematic.
    schematic_json = _fetch_generated_json(repository, schematic_path, ref)
    pages = schematic_json["pages"]
    components = []

    for page in pages:
        for component in page["components"].values():
            component_attributes = _component_attributes_multi_page(component)
            components.append(component_attributes)

    return _filter_blank_components(components, allspice_client.logger)


def _fetch_generated_json(repo: Repository, file_path: str, ref: Ref) -> dict:
    attempts = 0
    while attempts < 5:
        try:
            return repo.get_generated_json(file_path, ref=ref)
        except NotYetGeneratedException:
            time.sleep(SLEEP_FOR_GENERATED_JSON)

    raise TimeoutError(f"Failed to fetch JSON for {file_path} after 5 attempts.")


@functools.cache
def _fetch_all_files_in_repo(repo: Repository) -> list[str]:
    """
    Fetch a list of all files in a repository at the default branch.

    :param repo: The repository.
    :returns: A list of all file paths in the repo.
    """

    tree = repo.get_tree(recursive=True)

    return [file.path for file in tree]


def _extract_schdoc_list_from_prjpcb(
    prjpcb_ini: configparser.ConfigParser,
) -> tuple[set[str], set[str]]:
    """
    Extract sets of all schematic files used in this project.

    :param prjpcb_ini: The contents of the PrjPcb file as a ConfigParser.
    :returns: two sets. The first set is of relative paths from the project
        file to all the Schematic Documents in this project, and the second is
        of relative paths to device sheets from the project file.
    """

    schdoc_files = set()
    device_sheets = set()

    for section in prjpcb_ini.sections():
        if section.casefold().startswith("document"):
            document_path = prjpcb_ini[section].get("DocumentPath")
            if document_path and document_path.casefold().endswith(".schdoc"):
                schdoc_files.add(document_path)
        elif section.casefold().startswith("devicesheet"):
            document_path = prjpcb_ini[section].get("DocumentPath")
            if document_path and document_path.casefold().endswith(".schdoc"):
                device_sheets.add(document_path)

    return (schdoc_files, device_sheets)


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


def _build_schdoc_hierarchy(
    schematic_document_jsons: dict[str, dict],
    device_sheet_jsons: dict[str, dict],
) -> tuple[set[str], SchdocHierarchy]:
    """
    Build a hierarchy of sheets from a mapping of sheet names to the references
    of their children.

    :param document_jsons: A mapping of document sheet paths from project root
        to their JSON.
    :param device_sheet_jsons: A mapping of device sheet *names* to their JSON.
    :returns: The output of this function is a tuple of two values:

    1. A set of "independent" sheets, which can be taken to be roots of the
       hierarchy.
    2. A mapping of each sheet that has children to a list of tuples, where
       each tuple is a child sheet and the number of repetitions of that child
       sheet in the parent sheet. If a sheet has no children and is not a child
       of any other sheet, it will be mapped to an empty list.
    """

    hierarchy = {}

    schematic_document_entries = {
        schdoc_file: [value for value in schdoc_json.values() if isinstance(value, dict)]
        for schdoc_file, schdoc_json in schematic_document_jsons.items()
    }
    schematic_document_refs = {
        schdoc_file: [entry for entry in entries if entry.get("type") == "SheetRef"]
        for schdoc_file, entries in schematic_document_entries.items()
    }

    device_sheet_entries = {
        device_sheet_name: [
            value for value in device_sheet_json.values() if isinstance(value, dict)
        ]
        for device_sheet_name, device_sheet_json in device_sheet_jsons.items()
    }
    device_sheet_refs = {
        device_sheet_name: [entry for entry in entries if entry.get("type") == "SheetRef"]
        for device_sheet_name, entries in device_sheet_entries.items()
    }

    # We start by assuming all the document sheets are independent. Device
    # sheets cannot be independent, as they must be referred to by a document
    # sheet or another device sheet.
    independent_sheets = set(schematic_document_refs.keys())
    # This is what we'll use to compare with the sheet names in repetitions.
    schematic_document_names_downcased = {sheet.casefold(): sheet for sheet in independent_sheets}
    device_sheet_names_downcased = {sheet.casefold(): sheet for sheet in device_sheet_refs.keys()}

    # First, we'll build the hierarchy for device sheets, since they cannot
    # point to document sheets.
    for device_sheet_name, device_sheet_refs in device_sheet_refs.items():
        if not device_sheet_refs:
            continue

        repetitions = _extract_repetitions(device_sheet_refs)
        for child_sheet, count in repetitions.items():
            # child_sheet should just be a filename
            child_name = device_sheet_names_downcased[child_sheet.casefold()]
            if device_sheet_name in hierarchy:
                hierarchy[device_sheet_name].append((child_name, count))
            else:
                hierarchy[device_sheet_name] = [(child_name, count)]

    # Now for the document sheets, which can point to both other document
    # sheets and device sheets
    for schematic_document_sheet, refs in schematic_document_refs.items():
        if not refs or len(refs) == 0:
            continue

        repetitions = _extract_repetitions(refs)

        for child_sheet, count in repetitions.items():
            child_path = _resolve_child_relative_path(
                child_sheet, schematic_document_sheet
            ).casefold()
            if child_path in schematic_document_names_downcased:
                child_name = schematic_document_names_downcased[child_path]
            else:
                # Note the `child_sheet` below - we use the bare text without
                # any path resolution for device sheets.
                child_name = device_sheet_names_downcased[child_sheet.casefold()]
            if schematic_document_sheet in hierarchy:
                hierarchy[schematic_document_sheet].append((child_name, count))
            else:
                hierarchy[schematic_document_sheet] = [(child_name, count)]
            independent_sheets.discard(child_name)

    return (independent_sheets, hierarchy)


def _resolve_child_relative_path(child_path: str, parent_path: str) -> str:
    """
    Converts a relative path in a sheet ref to a POSIX relative path from the
    prjpcb file.

    The returned path is POSIX as we convert them to POSIX paths when fetching
    JSONs.
    """

    child = pathlib.PureWindowsPath(child_path)
    parent = pathlib.PureWindowsPath(parent_path)

    return (parent.parent / child).as_posix()


def _extract_repetitions(sheet_refs: list[dict]) -> dict[str, int]:
    """
    Takes a list of sheet references and returns a dictionary of each child
    sheet to the number of repetitions of that sheet in the parent sheet.
    """

    repetitions = {}
    for sheet_ref in sheet_refs:
        sheet_name = (sheet_ref.get("sheet_name", {}) or {}).get("name", "") or ""
        try:
            sheet_file_name = sheet_ref["filename"]
        except Exception:
            raise ValueError(f"Could not find sheet filename in {sheet_ref=}")
        if sheet_file_name is None:
            raise ValueError(
                "Sheet filename is null in for a sheet. Please check sheet references in this "
                "project for an empty file path."
            )
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


def _component_attributes_altium(component: dict) -> ComponentAttributes:
    """
    Extract the attributes of a component into a dict.

    This also adds some top-level properties of the component that are not
    attributes into the dict.
    """

    attributes = {}

    for key, value in component["attributes"].items():
        attributes[key] = value["text"]

    # The designator attribute has a `value` key which contains the unchanged
    # designator from the schematic file. This is useful when combining multi-
    # part components.
    attributes["_logical_designator"] = component["attributes"][DESIGNATOR_COLUMN_NAME]["value"]

    if "part_id" in component:
        attributes["_part_id"] = component["part_id"]
    if "name" in component:
        attributes["_name"] = component["name"]
    if "description" in component:
        attributes["_description"] = component["description"]
    if "unique_id" in component:
        attributes["_unique_id"] = component["unique_id"]
    if "kind" in component:
        attributes["_kind"] = component["kind"]
    if "part_count" in component:
        attributes["_part_count"] = component["part_count"]
        attributes["_current_part_id"] = component["current_part_id"]
    if "pins" in component:
        attributes["_pins"] = component["pins"]

    return attributes


def _component_attributes_multi_page(component: dict) -> ComponentAttributes:
    """
    Extract attributes of components from a multi-page document into a dict.

    This also adds some of the top-level properties of the component that
    are not attributes into the dict.
    """

    component_attributes = {}

    component_attributes["_name"] = component["name"]
    if "reference" in component:
        component_attributes["_reference"] = component.get("reference")
    if "logical_reference" in component:
        component_attributes["_logical_reference"] = component.get("logical_reference")
    if "pins" in component:
        # Multi-sheet documents have pins as an object of ids to pin objects.
        # The id is also inside the pin object, so we can flatten this into an
        # array, which is also compatible with how Altium outputs them.
        component_attributes["_pins"] = list(component["pins"].values())

    for attribute in component["attributes"].values():
        component_attributes[attribute["name"]] = attribute["value"]

    return component_attributes


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
    component_attributes: ComponentAttributes,
    repetitions: int,
) -> list[ComponentAttributes]:
    """
    Append a letter to the designator of each component in a list of components
    based on the number of repetitions of each component in the parent sheet.
    """

    if repetitions == 1:
        return [component_attributes]

    try:
        designator = component_attributes[DESIGNATOR_COLUMN_NAME]
        logical_designator = component_attributes["_logical_designator"]
    except KeyError:
        raise ValueError(f"Designator not found in {component_attributes=}")

    if designator is None:
        return [component_attributes] * repetitions

    return [
        {
            **component_attributes,
            DESIGNATOR_COLUMN_NAME: f"{designator}{_letters_for_repetition(i)}",
            # The designator value should also get the page ordinal, because
            # each time the page is repeated we're dealing with a different
            # component.
            "_logical_designator": f"{logical_designator}{_letters_for_repetition(i)}",
        }
        for i in range(1, repetitions + 1)
    ]


def _extract_components(
    sheet_name: str,
    sheets_to_entries: dict[str, list[dict]],
    hierarchy: SchdocHierarchy,
) -> list[ComponentAttributes]:
    components = []
    if sheet_name not in sheets_to_entries:
        return components

    for entry in sheets_to_entries[sheet_name]:
        if entry["type"] != "Component":
            continue

        component = _component_attributes_altium(entry)
        components.append(component)

    if sheet_name not in hierarchy:
        return components

    for child_sheet, count in hierarchy[sheet_name]:
        child_components = _extract_components(child_sheet, sheets_to_entries, hierarchy)
        if count > 1:
            for component in child_components:
                components.extend(_append_designator_letters(component, count))
        else:
            components.extend(child_components)

    return components


def _combine_multi_part_components_for_altium(
    components: list[dict[str, str]],
) -> list[dict[str, str]]:
    """
    Combine multi-part Altium components into a single component.

    Altium multi-part components can be distinguished by the `_part_count` and
    `_current_part_id` attributes being present, which respectively store the
    total number of parts and the current part number. If that is the case, the
    `_logical_designator` attribute ties together the different parts of the
    component.
    """

    combined_components = []
    multi_part_components_by_designator = {}

    for component in components:
        if "_part_count" in component and "_current_part_id" in component:
            designator = component["_logical_designator"]
            multi_part_components_by_designator.setdefault(designator, []).append(component)
        else:
            combined_components.append(component)

    for designator, multi_part_components in multi_part_components_by_designator.items():
        combined_component = multi_part_components[0].copy()
        combined_component[DESIGNATOR_COLUMN_NAME] = designator
        # The combined component shouldn't have the current part id, as it is
        # not any of the parts.
        del combined_component["_current_part_id"]
        combined_components.append(combined_component)

    return combined_components


def _combine_multi_part_components_for_orcad(
    components: list[dict[str, str]],
) -> list[dict[str, str]]:
    """
    Combine multi-part OrCAD components into a single component.

    Multi-part OrCAD components can be distinguished by the "logical_reference"
    attribute, which ties together the different parts of the component.
    """

    combined_components = []
    multi_part_components_by_designator = {}

    for component in components:
        if "_logical_reference" in component:
            designator = component["_logical_reference"]
            multi_part_components_by_designator.setdefault(designator, []).append(component)
        else:
            combined_components.append(component)

    for designator, multi_part_components in multi_part_components_by_designator.items():
        combined_component = multi_part_components[0].copy()
        combined_component[PART_REFERENCE_ATTR_NAME] = designator
        combined_component["_reference"] = designator
        combined_components.append(combined_component)

    return combined_components


def _extract_variations(
    variant: str,
    prjpcb_ini: configparser.ConfigParser,
) -> configparser.SectionProxy:
    """
    Extract the details of a variant from a PrjPcb file.
    """

    available_variants = set()

    for section in prjpcb_ini.sections():
        if section.startswith("ProjectVariant"):
            if prjpcb_ini[section].get("Description") == variant:
                return prjpcb_ini[section]
            else:
                available_variants.add(prjpcb_ini[section].get("Description"))
    raise ValueError(
        f"Variant {variant} not found in PrjPcb file.\n"
        f"Available variants: {', '.join(available_variants)}"
    )


def _apply_variations(
    components: list[dict[str, str]],
    variant_details: configparser.SectionProxy,
    logger: Logger,
) -> list[dict[str, str]]:
    """
    Apply the variations of a specific variant to the components. This should be
    done before the components are mapped to columns or grouped.

    :param components: The components to apply the variations to.
    :param variant_details: The section of the config file dealing with a
        specific variant.

    :returns: The components with the variations applied.
    """

    # Each item in the list is a pairing of (unique_id, designator), as both are
    # required to identify a component.
    components_to_remove: list[tuple[str, str]] = []
    # When patching components, the ParamVariation doesn't have the unique ID,
    # only a designator. However, ParamVariations follow the Variation entry, so
    # if we note down the last unique id we saw for a designator when going
    # through the variations, we can use that unique id when handling a param
    # variation. This dict holds that information.
    patch_component_unique_id: dict[str, str] = {}
    # The keys are the same as above, and the values are a key-value of the
    # parameter to patch and the value to patch it to.
    components_to_patch: dict[tuple[str, str], list[tuple[str, str]]] = {}

    for key, value in variant_details.items():
        # Note that this is in lowercase, as configparser stores all keys in
        # lowercase.
        if re.match(r"variation[\d+]", key):
            variation_details = dict(details.split("=", 1) for details in value.split("|"))
            try:
                designator = variation_details["Designator"]
                # The unique ID field is a "path" separated by backslashes, and
                # the the unique id we want is the last entry in that path.
                unique_id = variation_details["UniqueId"].split("\\")[-1]
                kind = variation_details["Kind"]
            except KeyError:
                logger.warning(
                    "Designator, UniqueId, or Kind not found in details of variation "
                    f"{variation_details}; skipping this variation."
                )
                continue
            try:
                kind = VariationKind(int(variation_details["Kind"]))
            except ValueError:
                logger.warning(
                    f"Kind {variation_details['Kind']} of variation {variation_details} must be "
                    "either 0, 1 or 2; skipping this variation."
                )
                continue

            if kind == VariationKind.NOT_FITTED:
                components_to_remove.append((unique_id, designator))
            else:
                patch_component_unique_id[designator] = unique_id
        elif re.match(r"paramvariation[\d]+", key):
            variation_id = key.split("paramvariation")[-1]
            designator = variant_details[f"ParamDesignator{variation_id}"]
            variation_details = dict(details.split("=", 1) for details in value.split("|"))
            try:
                unique_id = patch_component_unique_id[designator]
            except KeyError:
                # This can happen sometimes - Altium allows param variations
                # even when the component is not fitted, so we just log and
                # ignore.
                logger.warning(
                    f"ParamVariation{variation_id} found for component {designator} either before "
                    "the corresponding Variation or for a component that is not fitted.\n"
                    "Ignoring this ParamVariation."
                )
                continue

            try:
                parameter_patch = (
                    variation_details["ParameterName"],
                    variation_details["VariantValue"],
                )
            except KeyError:
                logger.warning(
                    f"ParameterName or VariantValue not found in ParamVariation{variation_id} "
                    "details."
                )
                continue

            if (unique_id, designator) in components_to_patch:
                components_to_patch[(unique_id, designator)].append(parameter_patch)
            else:
                components_to_patch[(unique_id, designator)] = [parameter_patch]

    final_components = []

    for component in components:
        identifying_pair = (component["_unique_id"], component[DESIGNATOR_COLUMN_NAME])
        if identifying_pair in components_to_remove:
            continue

        if identifying_pair in components_to_patch:
            new_component = component.copy()
            for parameter, value in components_to_patch[identifying_pair]:
                new_component[parameter] = value
            final_components.append(new_component)
        else:
            final_components.append(component)

    return final_components


def _filter_blank_components(
    components: list[ComponentAttributes],
    logger: Logger,
) -> list[ComponentAttributes]:
    """
    Remove components that have no attributes, or components for which all
    attributes are empty strings.

    This funtion also debug logs a warning for components that have no attributes.
    """

    final_components = []

    for component in components:
        if not any(component.values()):
            logger.debug(f"Component {component} has no attributes; skipping.")
            continue
        final_components.append(component)

    return final_components


def _find_device_sheet(
    device_sheet: str,
    project_repository: Repository,
    project_file_path: str,
    design_reuse_repos: list[Repository],
    logger: Logger,
) -> tuple[Repository, pathlib.PurePosixPath]:
    """
    Find a device sheet by name in the design reuse repositories.

    This currently does not use the directory structure of the device sheet
    path from the PrjPcb file, and instead only matches on the filename. If
    multiple matches are found, they are logged.

    :param design_reuse_repos: The design reuse repositories to search.
    :param device_sheet: The path of the device sheet as given in the PrjPcb.
    :returns: The first matching repository and the path to the device sheet in
        that repository.
    """

    matches: list[tuple[Repository, pathlib.PurePosixPath]] = []

    # Paths stored in the PrjPcb are Windows paths
    device_sheet_path = pathlib.PureWindowsPath(device_sheet)
    # Note that this will include the .SchDoc extension.
    device_sheet_name = device_sheet_path.name.casefold()

    # First, we'll resolve the actual path of the device sheet in the project
    # repo, and if that's a real file then we use that.
    device_sheet_path_from_repo_root = _resolve_prjpcb_relative_path(
        device_sheet,
        project_file_path,
    ).casefold()
    project_repo_tree = _fetch_all_files_in_repo(project_repository)
    for filepath in project_repo_tree:
        if device_sheet_path_from_repo_root == filepath.casefold():
            logger.info("Found device sheet %s in project repository; using that.", device_sheet)
            return (
                project_repository,
                pathlib.PurePosixPath(filepath),
            )

    for repo in design_reuse_repos:
        files_in_repo = _fetch_all_files_in_repo(repo)
        for file_in_repo in files_in_repo:
            # Paths as reported by ASH are Unix paths
            file_path = pathlib.PurePosixPath(file_in_repo)
            if device_sheet_name == file_path.name.casefold():
                matches.append((repo, file_path))

    if len(matches) == 0:
        raise ValueError(
            f"No matching device sheet found for {device_sheet_path} in the design reuse "
            "repositories.",
        )

    if len(matches) > 1:
        logger.info(
            "Multiple matches found for device sheet %s in design reuse repositories; set log "
            "level to debug to see all matches.",
            device_sheet,
        )
        for match in matches:
            logger.debug("Matching repository: %s, matching file path: %s", match[0].url, match[1])

        first_match = matches[0]
        logger.info(
            "Picking first match, i.e. Repository: %s, File Path: %s",
            first_match[0].url,
            first_match[1],
        )

    return matches[0]
