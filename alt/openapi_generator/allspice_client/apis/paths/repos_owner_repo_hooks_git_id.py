from allspice_client.paths.repos_owner_repo_hooks_git_id.get import ApiForget
from allspice_client.paths.repos_owner_repo_hooks_git_id.delete import ApiFordelete
from allspice_client.paths.repos_owner_repo_hooks_git_id.patch import ApiForpatch


class ReposOwnerRepoHooksGitId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
