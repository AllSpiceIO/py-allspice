import logging
import time
from typing import Callable, Optional, TypeVar, Union

from ..apiobject import Content, Ref
from ..exceptions import InternalServerException, NotYetGeneratedException, RenderException

MAX_RETRIES_FOR_GENERATED = 10
"""The maximum number of times to retry fetching generated JSON files."""

SLEEP_FOR_GENERATED = 1
"""The amount of time to sleep between attempts to fetch generated JSON files."""

TReturn = TypeVar("TReturn")


def retry_not_yet_generated(
    method: Callable[[Union[Content, str], Optional[Ref], Optional[dict]], TReturn],
    file_path: Union[Content, str],
    ref: Optional[Ref] = None,
    params: Optional[dict] = None,
    logger: Optional[logging.Logger] = None,
) -> TReturn:
    """
    Request AllSpice generated endpoints with retries if not yet available

    :param method: The request method that may raise
        NotYetGeneratedException, takes file_path and ref as arguments
    :param file_path: The path to the design document
    :param ref: The git ref to check.
    :param params: Optional parameters to pass to the method.
    :param logger: Optional logger used to record transient server errors before
        retrying. Retries are silent if it is omitted.
    :returns: The return value of the method if successful
    """
    attempts = 0
    while attempts < MAX_RETRIES_FOR_GENERATED:
        try:
            return method(file_path, ref, params)
        except NotYetGeneratedException:
            attempts += 1
            time.sleep(SLEEP_FOR_GENERATED)
        except InternalServerException as e:
            render_error = RenderException.from_internal(
                e, str(file_path), str(ref) if ref is not None else None
            )

            if render_error is not None:
                raise render_error from e

            if logger is not None:
                detail = e.body.message if e.body else None
                logger.warning(
                    "Transient server error fetching %s: %s - retrying", file_path, detail or e
                )

            attempts += 1
            time.sleep(SLEEP_FOR_GENERATED)

    raise TimeoutError(
        f"Failed to fetch JSON for {file_path} after {MAX_RETRIES_FOR_GENERATED} attempts."
    )
