from allspice_client.paths.repos_owner_repo_hooks_id.get import ApiForget
from allspice_client.paths.repos_owner_repo_hooks_id.delete import ApiFordelete
from allspice_client.paths.repos_owner_repo_hooks_id.patch import ApiForpatch


class ReposOwnerRepoHooksId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
