from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.repo_list_statuses_by_ref_sort import RepoListStatusesByRefSort
from ...models.repo_list_statuses_by_ref_state import RepoListStatusesByRefState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner: str,
    repo: str,
    ref: str,
    *,
    client: Client,
    sort: Union[Unset, None, RepoListStatusesByRefSort] = UNSET,
    state: Union[Unset, None, RepoListStatusesByRefState] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/commits/{ref}/statuses".format(client.base_url, owner=owner, repo=repo, ref=ref)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    owner: str,
    repo: str,
    ref: str,
    *,
    client: Client,
    sort: Union[Unset, None, RepoListStatusesByRefSort] = UNSET,
    state: Union[Unset, None, RepoListStatusesByRefState] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Get a commit's statuses, by branch/tag/commit reference

    Args:
        owner (str):
        repo (str):
        ref (str):
        sort (Union[Unset, None, RepoListStatusesByRefSort]):
        state (Union[Unset, None, RepoListStatusesByRefState]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        ref=ref,
        client=client,
        sort=sort,
        state=state,
        page=page,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    ref: str,
    *,
    client: Client,
    sort: Union[Unset, None, RepoListStatusesByRefSort] = UNSET,
    state: Union[Unset, None, RepoListStatusesByRefState] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Get a commit's statuses, by branch/tag/commit reference

    Args:
        owner (str):
        repo (str):
        ref (str):
        sort (Union[Unset, None, RepoListStatusesByRefSort]):
        state (Union[Unset, None, RepoListStatusesByRefState]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        ref=ref,
        client=client,
        sort=sort,
        state=state,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
