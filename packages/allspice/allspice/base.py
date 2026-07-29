"""Hand-written foundation for the generated Hub API classes: the request base classes and the
schema model bases. Not regenerated from the OpenAPI spec — the generated request and schema
modules build on it."""

import re
from abc import abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass
from enum import Enum
from functools import cached_property
from typing import TYPE_CHECKING, Any, ClassVar, Generic, TypeVar, cast

import requests
from pydantic import BaseModel, ConfigDict, PrivateAttr, ValidationInfo, model_validator

if TYPE_CHECKING:
    from allspice.allspice import AllSpice

ResponseT = TypeVar("ResponseT")
ItemT = TypeVar("ItemT")


# --- API Requests ---

# --- Request Field Markers: the second arg of Annotated[...] on a request field ---

@dataclass(frozen=True)
class RequestFieldMarker:
    """A base marker class for any request field for converting any field into a request"""


@dataclass(frozen=True)
class ParamMarker(RequestFieldMarker):
    """Base for param markers. `api_name` is the name the API expects, set only when it differs from
    the Python field name."""

    api_name: str | None = None


class PathParam(ParamMarker):
    """Substituted into the path template, e.g. the `{owner}` in the path."""


class QueryParam(ParamMarker):
    """Sent as a URL query parameter."""


class HeaderParam(ParamMarker):
    """Sent as a request header."""


class JSONBody(RequestFieldMarker):
    """Marks the field carrying the JSON request body."""


@dataclass(frozen=True)
class FileBody(RequestFieldMarker):
    """Marks a field uploaded as a multipart file. `api_name` is the form-field name the server
    expects, set only when it differs from the Python field name."""

    api_name: str | None = None


# --- Base class every generated request inherits ---


class ApiRequest(BaseModel, Generic[ResponseT]):
    method: ClassVar[str]
    request_path: ClassVar[str]
    response_model: ClassVar[Any]  # model class, X | Y union, list[X], NewType, or None — anything TypeAdapter validates

    def path_params(self) -> dict[str, Any]:
        """The PathParam field values, keyed by api_name."""
        params: dict[str, Any] = {}
        for name, field in type(self).model_fields.items():
            marker = next((m for m in field.metadata if isinstance(m, ParamMarker)), None)
            if isinstance(marker, PathParam):
                params[getattr(marker, "api_name", None) or name] = getattr(self, name)
        return params

    def to_request(self, base_url: str) -> requests.Request:
        """Build a `requests.Request` against `base_url` by
        routing the declared fields into the path / query / headers / body.
        """
        path_values = self.path_params()
        query: dict[str, Any] = {}
        headers: dict[str, Any] = {}
        files: dict[str, Any] = {}
        body: BaseModel | None = None

        for name, field in type(self).model_fields.items():
            marker = next((m for m in field.metadata if isinstance(m, (ParamMarker, JSONBody, FileBody))), None)
            value = getattr(self, name)
            api_name = getattr(marker, "api_name", None) or name

            if isinstance(marker, PathParam):
                continue  # already captured by path_params()
            elif isinstance(marker, QueryParam):
                if value is not None:
                    query[api_name] = value
            elif isinstance(marker, HeaderParam):
                if value is not None:
                    headers[api_name] = value
            elif isinstance(marker, JSONBody):
                body = value
            elif isinstance(marker, FileBody):
                files[api_name] = value
            else:
                raise TypeError(
                    f"{type(self).__name__}.{name} must be tagged with one of "
                    "PathParam / QueryParam / HeaderParam / JSONBody / FileBody"
                )

        placeholders = set(re.findall(r"{(\w+)}", self.request_path))
        missing = placeholders - path_values.keys()
        if missing:
            raise TypeError(
                f"{type(self).__name__}: path {self.request_path!r} has unfilled "
                f"placeholder(s) {sorted(missing)} — add a PathParam field for each."
            )
        extra = path_values.keys() - placeholders
        if extra:
            raise TypeError(
                f"{type(self).__name__}: PathParam field(s) {sorted(extra)} have no "
                f"matching placeholder in path {self.request_path!r}."
            )

        return requests.Request(
            method=self.method,
            url=base_url + self.request_path.format(**path_values),
            params=query,
            headers=headers,
            # by_alias so bodies serialize under their api names (some models
            # alias PascalCase keys to snake_case attrs), not the Python attr names.
            # exclude_none drops unset optionals: Hub treats a missing key and an
            # explicit null the same (its optionals are pointers), so we send only
            # what the caller actually set.
            json=body.model_dump(mode="json", by_alias=True, exclude_none=True) if body is not None else None,
            files=files or None,
        )


# --- Paginated Requests ---


class PaginatedRequest(ApiRequest[ResponseT], Generic[ResponseT, ItemT]):
    """A request whose list response is paginated. `_page_key` is the page query-param name
    (almost always "page"); `_page_items_attr` is the response attribute holding the page's list,
    or None when the response *is* the list. Both are set by the generator per request."""

    _page_key: ClassVar[str] = "page"
    _page_items_attr: ClassVar[str | None] = None

    def set_page(self, page: int) -> None:
        """Set the page param for the next request; override if an endpoint pages differently."""
        setattr(self, self._page_key, page)

    def page_items(self, response: ResponseT) -> list[ItemT]:
        """The page's list — the response itself, or the list held in its `_page_items_attr`."""
        items = response if self._page_items_attr is None else getattr(response, self._page_items_attr)
        return cast("list[ItemT]", items)


# --- Models ---

# --- Open enum base for generated enums ---


class OpenEnum(Enum):
    """Base for generated enum schema types. A value matching no member resolves to the
    subclass's `UNKNOWN` member (via `_missing_`) instead of raising, so a value added on the
    server later degrades gracefully rather than failing the whole response parse. Each generated
    enum defines its own `UNKNOWN` — a client-only sentinel, never a real api value."""

    @classmethod
    def _missing_(cls, value: object) -> "OpenEnum":
        # A member of another enum (e.g. a response's AccessMode fed into the input's
        # AccessModeOption) maps to the member here that shares its value. 
        # A foreign enum member with no counterpart is a bug in caller code, 
        # so fail loudly rather than silently sending UNKNOWN to the server.
        if isinstance(value, Enum):
            for member in cls:
                if member.value == value.value:
                    return member
            raise ValueError(
                f"{type(value).__name__}.{value.name} ({value.value!r}) has no equivalent "
                f"in {cls.__name__}"
            )
        # A raw api value this client version doesn't recognize degrades to UNKNOWN, so a value
        # added on the server later doesn't fail the whole response parse.
        return cls["UNKNOWN"]


# --- Model base hierarchy ---


class AllSpiceBaseModel(BaseModel):
    """Shared config root for the model hierarchy. Not used directly as a generated base — the
    concrete bases below (ReadOnlyModel, InputModel) and the entity chain (via AllSpiceEntity)
    inherit it, and Pydantic merges this config into each subclass."""

    # populate_by_name lets models be built with their snake_case field names,
    # not only the original spec-name aliases.
    model_config = ConfigDict(populate_by_name=True)


class ReadOnlyModel(AllSpiceBaseModel):
    """Base for schema models only reachable from a response — immutable after construction.
    frozen=True raises on field assignment at runtime (and makes the model hashable) and merges
    with the inherited populate_by_name."""

    model_config = ConfigDict(frozen=True)


class InputModel(AllSpiceBaseModel):
    """Base for input only schema models (request bodies, parameters, etc) — mutable, 
    so callers can build them field by field."""


# --- Entity base and capability mixins ---


class AllSpiceEntity(AllSpiceBaseModel):
    """Base for schema models that represent a live Hub resource (rather than a plain-data
    Option model). Holds the client used to act on that resource."""

    _client: "AllSpice" = PrivateAttr()
    # Path params of the request that produced this entity, keyed by api name — kept so
    # the entity can supply parent-resource params (owner, repo, …) its own requests need.
    _path_context: dict[str, Any] = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def _attach_client(self, info: ValidationInfo) -> "AllSpiceEntity":
        # Attach the client passed via validation context so the entity can make
        # follow-up requests; also reaches nested entities validated in the same tree.
        if info.context and (client := info.context.get("client")):
            self._client = client
        return self

    def _owned_children(self) -> Iterable["AllSpiceEntity"]:
        """The sub-resources this entity owns and that arrive inline with it (e.g. a
        release's assets). Empty unless overridden. Referenced-but-not-owned entities (a
        release's author, say) are deliberately excluded — they aren't this one's children."""
        return ()

    def _set_parent(self, parent: "AllSpiceEntity") -> None:
        """Record `parent` as this resource's parent. No-op unless a sub-resource mixin
        overrides it to keep a typed reference (an asset keeps its release, etc.)."""

    def _attach_parents(self) -> None:
        """Set self as the parent of every owned child, depth-first."""
        for child in self._owned_children():
            child._set_parent(self)
            child._attach_parents()


class ReadOnlyEntity(AllSpiceEntity):
    """Base for read-only resources that still need entity behavior — they carry the client so they
    can host classmethod fetchers (`request`) and instance methods (e.g. `Commit.get_status`) —
    while staying immutable. `frozen` guards field assignment at runtime; pyright gets the same
    read-only view from the Final-typed stub (a non-Committable entity has no patchable fields, so
    every field is frozen there). Private attrs (`_client`, path context) aren't model fields, so
    the entity machinery still sets them on a frozen instance."""

    model_config = ConfigDict(frozen=True)


class Committable(AllSpiceEntity):
    """Entity mixin for resources that can be edited and PATCHed back. Fields that
    appear on the entity's patch Option are writable and recorded as dirty; every
    other field is read-only."""

    _dirty_fields: set[str] = PrivateAttr(default_factory=set)

    @classmethod
    @abstractmethod
    def _patch_request_type(cls) -> type[ApiRequest]:
        """The PATCH request class for this entity; its body type is the patch Option."""

    @abstractmethod
    def _to_patch_request(self) -> ApiRequest:
        """Build the PATCH request for the current dirty state."""

    @classmethod
    def _compute_patchable_fields(cls) -> set[str]:
        request_type = cls._patch_request_type()
        option = request_type.model_fields["body"].annotation
        if not (isinstance(option, type) and issubclass(option, BaseModel)):
            raise TypeError(
                f"{cls.__name__}: {request_type.__name__}'s body is not a model "
                f"({option!r}); can't derive patchable fields."
            )
        return set(option.model_fields)

    @cached_property
    def _patchable_fields(self) -> set[str]:
        return self._compute_patchable_fields()

    def _dirty_values(self) -> dict[str, Any]:
        return {name: getattr(self, name) for name in self._dirty_fields}

    def __setattr__(self, name: str, value: Any) -> None:
        if name in type(self).model_fields:
            if name not in self._patchable_fields:
                raise AttributeError(
                    f"{type(self).__name__}.{name!r} is read-only; only fields on "
                    "its patch Option can be set."
                )
            if isinstance(value, OpenEnum) and value.name == "UNKNOWN":
                raise ValueError(
                    f"{type(self).__name__}.{name!r}: refusing to set "
                    f"{type(value).__name__}.UNKNOWN — it's a placeholder for a value this client "
                    "version doesn't recognize, not a real value to send back to the server."
                )
            self._dirty_fields.add(name)
        super().__setattr__(name, value)

    def commit(self) -> None:
        updated = self._client.send(self._to_patch_request())
        if updated is not None:
            # Re-hydrate from the server's authoritative post-edit state so derived fields
            # (full_name, *_url, updated_at, …) don't go stale. vars() is the instance field
            # dict; private attrs (_client, path context) live elsewhere and are left untouched.
            vars(self).update(vars(updated))
        self._dirty_fields.clear()


class Deletable(AllSpiceEntity):
    """Entity mixin for resources that can be deleted."""

    @abstractmethod
    def _to_delete_request(self) -> ApiRequest:
        """Build the DELETE request for this entity."""

    def delete(self) -> None:
        self._client.send(self._to_delete_request())
