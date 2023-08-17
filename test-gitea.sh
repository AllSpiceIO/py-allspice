#! /usr/bin/env sh

# Deselect only those tests that require AllSpice Hub. The rest should run on
# vanilla Gitea.
python -m pytest --deselect=tests/test_utils.py \
    --deselect=tests/test_api_longtests.py::test_list_team_members \
    --deselect=tests/test_api.py::test_get_json_before_generated \
    --deselect=tests/test_api.py::test_get_svg_before_generated \
    --deselect=tests/test_api.py::test_get_generated_json\
    --deselect=tests/test_api.py::test_get_generated_svg
