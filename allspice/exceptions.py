import json
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class APIError:
    """The body of an AllSpice Hub error response"""

    message: Optional[str]
    url: Optional[str]

    @classmethod
    def from_json(cls, text: str) -> Optional["APIError"]:
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            return None

        if not isinstance(data, dict):
            return None

        message = data.get("message") or None
        url = data.get("url") or None

        if message is None and url is None:
            return None

        return cls(message=message, url=url)


class InternalServerException(Exception):
    def __init__(self, message: str, body: Optional[APIError] = None):
        super().__init__(message)
        self.body = body


class RenderException(Exception):
    """Raised when a server-side render fails; not retried."""

    @classmethod
    def from_internal(
        cls, internal: InternalServerException, file_path: str, ref: Optional[str]
    ) -> "RenderException":
        body = internal.body
        if body and body.message:
            message = body.message
        else:
            message = f"Render failed for {file_path}"
            if ref is not None:
                message += f" at ref {ref}"

        # Include a diagnostic url if present (a Hub link to the admin panel, don't include other links like swagger docs),
        # otherwise just ask them to check Hub logs
        if body and body.url and "-/admin/" in body.url:
            message += f"; A diagnostic report for this failure can be downloaded by a site admin at {body.url}."
        else:
            message += "; Check AllSpice Hub logs for more information."

        return cls(message)


class AlreadyExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class ObjectIsInvalid(Exception):
    pass


class ConflictException(Exception):
    pass


class NotYetGeneratedException(Exception):
    """
    For AllSpice generated objects, this exception is raised when the
    object has not yet been generated.

    Usually, retrying after a while will be successful.
    """

    pass


class RawRequestEndpointMissing(Exception):
    """This ApiObject can only be obtained through other api objects and does not have
    direct .request method."""

    pass


class MissingEqualityImplementation(Exception):
    """
    Each Object obtained from the AllSpice Hub api must be able to check itself for equality in relation to its
    fields obtained from gitea. Risen if an api object is lacking the proper implementation.
    """

    pass
