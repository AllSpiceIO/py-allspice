from allspice_client.paths.repos_owner_repo_releases_id.get import ApiForget
from allspice_client.paths.repos_owner_repo_releases_id.delete import ApiFordelete
from allspice_client.paths.repos_owner_repo_releases_id.patch import ApiForpatch


class ReposOwnerRepoReleasesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
