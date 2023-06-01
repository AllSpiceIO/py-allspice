from allspice_client.paths.repos_owner_repo_issues_comments_id.get import ApiForget
from allspice_client.paths.repos_owner_repo_issues_comments_id.delete import ApiFordelete
from allspice_client.paths.repos_owner_repo_issues_comments_id.patch import ApiForpatch


class ReposOwnerRepoIssuesCommentsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
