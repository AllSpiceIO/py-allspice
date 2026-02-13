import logging

from allspice.utils.list_components import (
    DESIGNATOR_COLUMN_NAME,
    LOGICAL_DESIGNATOR,
    _apply_annotation_file,
)


def test_apply_annotation_updates_logical_and_designator_when_different():
    logger = logging.getLogger(__name__)

    components = [
        {
            DESIGNATOR_COLUMN_NAME: "U1A",
            LOGICAL_DESIGNATOR: "U1",
            "_unique_id": "S1\\C1",
        }
    ]
    annotations_data = {
        "S1\\C1": {"from": "U1", "to": "R5"},
    }

    result = _apply_annotation_file(
        components,
        annotations_data,
        unique_ids_mapping={},
        logger=logger,
    )

    assert result[0][DESIGNATOR_COLUMN_NAME] == "R5"
    assert result[0][LOGICAL_DESIGNATOR] == "R5"
