import json
import os

from open_api_generator.document import (
    get_document_version,
    get_input_only_schema_names,
    prune_document,
)


def load_document():
    path = os.path.join(os.path.dirname(__file__), "data", "sample_document.json")
    with open(path) as f:
        return json.load(f)


def test_prune_document():
    full_document = load_document()
    pruned = prune_document(full_document)

    # prune_document removes paths (/without-samples) that have only unused endpoints
    # but keeps the paths that have any with py-allspice examples
    assert set(full_document["paths"]) == {"/with-samples", "/mixed-samples", "/without-samples"}
    assert set(pruned["paths"]) == {"/with-samples", "/mixed-samples"}

    # All operations without py-allspice are removed
    assert set(pruned["paths"]["/with-samples"]) == {"get", "post", "put", "patch", "delete"}
    assert set(pruned["paths"]["/mixed-samples"]) == {"get"}
    assert set(full_document["paths"]["/mixed-samples"]) == {"get", "put", "delete"}

    # Any schemas not reachable by remaining paths are trimmed out
    assert set(pruned["components"]["schemas"]) == {
        "getResponseSchema",
        "postResponseSchema",
        "putResponseSchema",
        "patchResponseSchema",
        "deleteResponseSchema",
        "postRequestBodySchema",
        "patchRequestBodySchema",
        "sharedNestedSchema",
        "mixedGetResponseSchema",
    }

    # The full document defines every schema, reachable or not
    assert set(full_document["components"]["schemas"]) == {
        "getResponseSchema",
        "postResponseSchema",
        "putResponseSchema",
        "patchResponseSchema",
        "deleteResponseSchema",
        "postRequestBodySchema",
        "patchRequestBodySchema",
        "sharedNestedSchema",
        "mixedGetResponseSchema",
        # In pruned operations
        "mixedPutResponseSchema",
        "mixedDeleteResponseSchema",
        "getResponseSchemaWithoutSample",
        "postResponseSchemaWithoutSample",
        "putResponseSchemaWithoutSample",
        "patchResponseSchemaWithoutSample",
        "deleteResponseSchemaWithoutSample",
        "postRequestBodySchemaWithoutSample",
        "patchRequestBodySchemaWithoutSample",
        # Originally orphaned, not pruned but never relevant
        "orphanSchema",
    }

    # The document version survives pruning
    assert full_document["info"]["version"] == "1.23.456"
    assert pruned["info"]["version"] == full_document["info"]["version"]


def test_prune_document_does_not_mutate_input():
    document = load_document()
    original = load_document()

    prune_document(document)

    assert document == original


def test_get_input_only_schema_names():
    full_document = load_document()
    all_names = set(full_document["components"]["schemas"])
    input_only_names = get_input_only_schema_names(full_document)

    # A schema is input-only when a request reaches it but no response does. Request-body
    # schemas qualify; sharedNestedSchema does not (a response reaches it too), and
    # orphanSchema does not (no request reaches it).
    assert input_only_names == {
        "postRequestBodySchema",
        "patchRequestBodySchema",
        "postRequestBodySchemaWithoutSample",
        "patchRequestBodySchemaWithoutSample",
    }

    # Every schema the document defines; input-only is a subset of these.
    assert all_names == {
        "getResponseSchema",
        "postResponseSchema",
        "putResponseSchema",
        "patchResponseSchema",
        "deleteResponseSchema",
        "postRequestBodySchema",
        "patchRequestBodySchema",
        "sharedNestedSchema",
        "mixedGetResponseSchema",
        "mixedPutResponseSchema",
        "mixedDeleteResponseSchema",
        "getResponseSchemaWithoutSample",
        "postResponseSchemaWithoutSample",
        "putResponseSchemaWithoutSample",
        "patchResponseSchemaWithoutSample",
        "deleteResponseSchemaWithoutSample",
        "postRequestBodySchemaWithoutSample",
        "patchRequestBodySchemaWithoutSample",
        "orphanSchema",
    }


def test_get_document_version():
    # The version is info.version, returned verbatim
    assert get_document_version(load_document()) == "1.23.456"
