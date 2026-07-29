"""Stand-in for py-allspice's real allspice.entities module, used by the entity-base test. It
mirrors how the generated schemas will import their entity classes — pulling AllSpiceEntity out of
the real base; tests can swap its allspice.entities import to this module."""

from typing import Annotated

from allspice.base import ApiRequest, Committable, InputModel, JSONBody, PathParam


class SampleUserPatchOptions(InputModel):
    """The editable fields of a SampleUser. Its field names are what make the matching fields on the
    entity writable, and every other field read-only."""

    login: str | None = None
    full_name: str | None = None


class SampleUserPatchRequest(ApiRequest[None]):
    method = "PATCH"
    request_path = "/users/{login}"
    response_model = None

    login: Annotated[str, PathParam()]
    body: Annotated[SampleUserPatchOptions, JSONBody()]


class SampleUserEntity(Committable):
    @classmethod
    def _patch_request_type(cls) -> type[ApiRequest]:
        return SampleUserPatchRequest

    def _to_patch_request(self) -> ApiRequest:
        raise NotImplementedError(
            "SampleUserEntity is a stand-in for interface-generation tests; only its patch Option "
            "is read, so it never builds a request."
        )
