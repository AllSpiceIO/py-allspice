import pytest
import time
import uuid

from allspice import AllSpice, User, Organization, Team, Repository, Issue
from allspice import NotFoundException, AlreadyExistsException


# put a ".token" file into your directory containg only the token for AllSpice Hub
@pytest.fixture
def instance(scope="module"):
    try:
        g = AllSpice(
            allspice_hub_url="http://localhost:3000",
            token_text=open(".token", "r").read().strip(),
            ratelimiting=(10, 1),
        )
        print("AllSpice Hub Version: " + g.get_version())
        print("API-Token belongs to user: " + g.get_user().username)
        return g
    except:
        assert (
            False
        ), "AllSpice Hub could not load. \
                - Instance running at http://localhost:3000 \
                - Token at .token   \
                    ?"


def test_access_is_ratelimited(instance):
    start_time = time.time()

    for _ in range(11):
        instance.get_user()

    # Binding on both sides helps us be more confident this is due to rate
    # limiting, not the server being slow.
    assert 1 <= time.time() - start_time <= 1.2


def test_access_is_ratelimited_across_apis(instance):
    start_time = time.time()

    for _ in range(4):
        instance.get_user()
        instance.get_version()
        instance.get_orgs()

    assert 1 <= time.time() - start_time <= 1.2