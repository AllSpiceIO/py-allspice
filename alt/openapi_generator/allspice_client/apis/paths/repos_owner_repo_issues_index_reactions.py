from allspice_client.paths.repos_owner_repo_issues_index_reactions.get import ApiForget
from allspice_client.paths.repos_owner_repo_issues_index_reactions.post import ApiForpost
from allspice_client.paths.repos_owner_repo_issues_index_reactions.delete import ApiFordelete


class ReposOwnerRepoIssuesIndexReactions(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
