#!/usr/bin/env python
"""Fixtures for testing py-allspice

Instructions
------------
put a ".token" file into your directory containg only the token for AllSpice Hub

"""

import os

import pytest

from allspice import AllSpice


def pytest_addoption(parser):
    """add option to specify localhost port and log level for tests"""
    parser.addoption("--port", action="store", default="3000")
    parser.addoption("--client-log-level", action="store", default="INFO")


@pytest.fixture
def instance(scope="module"):
    try:
        url = os.getenv("PY_ALLSPICE_URL")
        token = os.getenv("PY_ALLSPICE_TOKEN")
        auth = os.getenv("PY_ALLSPICE_AUTH")
        if not url:
            raise ValueError("No AllSpice Hub URL was provided")
        if token and auth:
            raise ValueError("Please provide auth or token_text, but not both")
        g = AllSpice(allspice_hub_url=url, token_text=token, auth=auth, verify=False)
        print("AllSpice Hub Version: " + g.get_version())
        print("API-Token belongs to user: " + g.get_user().username)
        return g
    except Exception:
        assert False, (
            "AllSpice Hub could not load. \
                - Instance running at http://localhost:3000 \
                - Token at .token   \
                    ?"
        )
