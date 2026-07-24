"""Hand-written model base classes for the generated Hub API schemas.

Not regenerated from the OpenAPI spec — the stable foundation the generated models build on."""

from enum import Enum

from pydantic import BaseModel, ConfigDict


class OpenEnum(Enum):
    """Base for generated enum schema types. A wire value matching no member resolves to the
    subclass's `UNKNOWN` member (via `_missing_`) instead of raising, so a value added on the
    server later degrades gracefully rather than failing the whole response parse. Each generated
    enum defines its own `UNKNOWN` — a client-only sentinel, never a real wire value."""

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
        # A raw wire value this client version doesn't recognize degrades to UNKNOWN, so a value
        # added on the server later doesn't fail the whole response parse.
        return cls["UNKNOWN"]


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


# TODO: empty placeholder — the client field and entity behavior are not implemented yet.
class AllSpiceEntity(AllSpiceBaseModel):
    """Base for schema models that represent a live Hub resource (rather than a plain-data
    Option model). Holds the client used to act on that resource."""
