import json
from unittest.mock import MagicMock

import pytest
from vcr.filters import replace_post_data_parameters
from vcr.request import Request

from .test_utils import setup_for_generation, vcr_config


def test_migration_credentials_are_removed_from_cassettes():
    request = Request(
        "POST",
        "http://localhost:3000/api/v1/repos/migrate",
        json.dumps(
            {
                "clone_addr": "https://github.com/AllSpiceIO/test-example",
                "auth_password": "secret",
                "auth_token": "other-secret",
            }
        ),
        {"Content-Type": "application/json"},
    )
    config = vcr_config.__wrapped__()
    replace_post_data_parameters(
        request, [(key, None) for key in config["filter_post_data_parameters"]]
    )
    assert json.loads(request.body) == {"clone_addr": "https://github.com/AllSpiceIO/test-example"}


def test_migration_failure_does_not_log_credentials(monkeypatch, caplog):
    monkeypatch.setenv("TEST_FIXTURES_TOKEN", "fixture-secret")
    instance = MagicMock()
    instance.url = "http://localhost:3000"
    instance.headers = {"Authorization": "token hub-secret"}
    instance.requests.post.return_value.status_code = 403
    fixture = setup_for_generation.__wrapped__(instance)
    migrate = next(fixture)
    with pytest.raises(RuntimeError, match=r"Fixture migration failed \(HTTP 403\)") as error:
        migrate("example", "https://github.com/AllSpiceIO/test-example")
    assert instance.requests.post.call_args.kwargs["json"]["auth_password"] == "fixture-secret"
    assert "fixture-secret" not in str(error.value) + caplog.text
    instance.requests_post.assert_not_called()
    fixture.close()
