from allspice_client.paths.repos_owner_repo.get import ApiForget
from allspice_client.paths.repos_owner_repo.delete import ApiFordelete
from allspice_client.paths.repos_owner_repo.patch import ApiForpatch


class ReposOwnerRepo(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
