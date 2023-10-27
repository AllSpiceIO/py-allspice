from __future__ import annotations

import time

from ..apiobject import Ref, Repository
from ..exceptions import NotYetGeneratedException


# TODO: We should strongly type the schema for PCB files
def get_all_pcb_components(
    repository: Repository,
    ref: Ref,
    pcb_file: str,
) -> dict:
    """
    Get all component data from a Pcb file.
    """

    retry_count = 0
    while retry_count < 60:
        retry_count += 1
        try:
            pcb_json = repository.get_generated_json(pcb_file, ref=ref)
            return pcb_json["component_instances"]
        except NotYetGeneratedException:
            # Wait a bit before retrying.
            time.sleep(0.25)
            continue
    raise Exception(f"Fetching file {pcb_file} in {repository} ref={ref} exceeded max retries.")
