import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import ClassVar

import pytest
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from allspice import AllSpice, NotFoundException
from allspice.allspice import DEFAULT_RETRY
from allspice.exceptions import InternalServerException, NotYetGeneratedException


def make_instance(url="https://example.com", **kwargs):
    return AllSpice(allspice_hub_url=url, token_text="test", **kwargs)


def mounted_retries(instance):
    return instance.requests.get_adapter("https://example.com").max_retries


def test_default_retry_is_mounted():
    assert mounted_retries(make_instance()) is DEFAULT_RETRY


def test_custom_retry_is_mounted():
    retry = Retry(total=2)
    assert mounted_retries(make_instance(retry=retry)) is retry


def test_int_retry_is_mounted():
    assert mounted_retries(make_instance(retry=3)).total == 3


def test_none_opts_out():
    assert mounted_retries(make_instance(retry=None)).total == HTTPAdapter().max_retries.total


@pytest.fixture
def stub_server():
    class Handler(BaseHTTPRequestHandler):
        scripted_responses: ClassVar[list[tuple[int, str]]] = []
        requests_received: ClassVar[list[str]] = []

        def do_GET(self):
            self._respond()

        def do_POST(self):
            self.rfile.read(int(self.headers.get("Content-Length", 0)))
            self._respond()

        def _respond(self):
            self.requests_received.append(self.path)
            status, body = self.scripted_responses[
                min(len(self.requests_received) - 1, len(self.scripted_responses) - 1)
            ]
            self.send_response(status)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(body.encode())

        def log_message(self, format, *args):
            pass

    server = HTTPServer(("localhost", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield Handler, f"http://localhost:{server.server_port}"
    server.shutdown()


@pytest.mark.parametrize("status", [429, 502])
def test_retries_by_default_then_succeeds(stub_server, status):
    handler, url = stub_server
    handler.scripted_responses = [(status, "{}"), (200, json.dumps({"version": "1.0.0"}))]

    instance = make_instance(url=url, ratelimiting=None)
    assert instance.get_version() == "1.0.0"
    assert len(handler.requests_received) == 2


def test_retries_post_by_default(stub_server):
    handler, url = stub_server
    handler.scripted_responses = [(429, "{}"), (200, json.dumps({"id": 1}))]

    instance = make_instance(url=url, ratelimiting=None)
    assert instance.requests_post("/repos/o/r/issues", data={"title": "t"}) == {"id": 1}
    assert len(handler.requests_received) == 2


@pytest.mark.parametrize(
    "status,exception",
    [(503, NotYetGeneratedException), (500, InternalServerException)],
)
def test_semantic_statuses_are_not_retried(stub_server, status, exception):
    handler, url = stub_server
    handler.scripted_responses = [(status, "{}")]

    instance = make_instance(url=url, ratelimiting=None)
    with pytest.raises(exception):
        instance.requests_get("/repos/o/r/allspice_generated/json/file")
    assert len(handler.requests_received) == 1


def test_exhausted_retries_raise_typed_exception(stub_server):
    handler, url = stub_server
    handler.scripted_responses = [(404, "{}")]

    instance = make_instance(url=url, ratelimiting=None)
    with pytest.raises(NotFoundException):
        instance.requests_get("/repos/nobody/nothing")
    assert len(handler.requests_received) == 1


def test_exhausted_retries_return_final_response(stub_server):
    handler, url = stub_server
    handler.scripted_responses = [(429, "{}")]

    retry = DEFAULT_RETRY.new(total=2, backoff_factor=0, backoff_jitter=0)
    instance = make_instance(url=url, ratelimiting=None, retry=retry)
    with pytest.raises(Exception, match="429"):
        instance.requests_get("/version")
    assert len(handler.requests_received) == 3
