import time

from allspice.exceptions import NotYetGeneratedException
from ..allspice import AllSpice
from ..apiobject import Repository

PCB_FOOTPRINT_ATTR_NAME = "PCB Footprint"
PART_REFERENCE_ATTR_NAME = "Part Reference"


def list_components_for_orcad(
    allspice_client: AllSpice,
    repository: Repository,
    dsn_path: str,
    ref: str = "main",
) -> list[dict[str, str]]:
    """
    Get a list of all components in an OrCAD DSN schematic.

    :param client: An AllSpice client instance.
    :param repository: The repository containing the OrCAD schematic.
    :param dsn_path: The path to the OrCAD DSN file from the repo root. For
        example, if the schematic is in the folder "Schematics" and the file
        is named "example.dsn", the path would be "Schematics/example.dsn".
    :param ref: Optional git ref to check. This can be a commit hash, branch
        name, or tag name. Default is "main", i.e. the main branch.
    :return: A list of all components in the OrCAD schematic. Each component is
        a dictionary with the keys being the attributes of the component and the
        values being the values of the attributes. A `_name` attribute is added
        to each component to store the name of the component.
    """

    allspice_client.logger.debug(
        f"Listing components in {dsn_path=} from {repository.get_full_name()} on {ref=}"
    )

    # Get the generated JSON for the schematic.
    dsn_json = _fetch_generated_json(repository, dsn_path, ref)
    pages = dsn_json["pages"]
    components = []

    for page in pages:
        for component in page["components"].values():
            component["_name"] = component["name"]
            for attribute in component["attributes"].values():
                component[attribute["name"]] = attribute["value"]
            components.append(component)

    components = _combine_multi_symbol_components(components)

    return components


def _combine_multi_symbol_components(components: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Combine all symbols of a multi-symbol component into a single component.

    :param components: A list of components from an OrCAD schematic.
    :return: A list of components with multi-symbol components combined. If a
        component is not a multi-symbol component, it is not modified.
    """

    combined_components = []
    components_by_footprint = {}

    for component in components:
        footprint = component.get(PCB_FOOTPRINT_ATTR_NAME)
        if footprint is None:
            combined_components.append(component)

        if footprint not in components_by_footprint:
            components_by_footprint[footprint] = [component]
        else:
            components_by_footprint[footprint].append(component)

    for footprint, components in components_by_footprint.items():
        if len(components) == 1:
            combined_components.append(components[0])
            continue

        multi_symbol_components = {}
        for component in components:
            part_reference = component.get(PART_REFERENCE_ATTR_NAME)
            if not part_reference:
                continue

            # If the designator ends with a letter, that indicates a
            # multi-symbol component, and we need to remove the letter to get
            # the part reference.
            if part_reference[-1].isalpha():
                part_reference = part_reference[:-1]

            if part_reference not in multi_symbol_components:
                multi_symbol_components[part_reference] = [component]
            else:
                multi_symbol_components[part_reference].append(component)

        for part_reference, components in multi_symbol_components.items():
            combined_component = components[0].copy()
            combined_component[PART_REFERENCE_ATTR_NAME] = part_reference
            combined_components.append(combined_component)

    return combined_components


def _fetch_generated_json(repo: Repository, file_path: str, ref: str) -> dict:
    attempts = 0
    while attempts < 5:
        try:
            return repo.get_generated_json(file_path, ref=ref)
        except NotYetGeneratedException:
            time.sleep(0.5)

    raise TimeoutError(f"Failed to fetch JSON for {file_path} after 5 attempts.")
