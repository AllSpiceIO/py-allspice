from allspice_client.paths.repos_owner_repo_issues_index.get import ApiForget
from allspice_client.paths.repos_owner_repo_issues_index.delete import ApiFordelete
from allspice_client.paths.repos_owner_repo_issues_index.patch import ApiForpatch


class ReposOwnerRepoIssuesIndex(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
