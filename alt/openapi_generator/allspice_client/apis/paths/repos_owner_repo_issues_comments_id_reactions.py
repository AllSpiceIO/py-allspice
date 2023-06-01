from allspice_client.paths.repos_owner_repo_issues_comments_id_reactions.get import ApiForget
from allspice_client.paths.repos_owner_repo_issues_comments_id_reactions.post import ApiForpost
from allspice_client.paths.repos_owner_repo_issues_comments_id_reactions.delete import ApiFordelete


class ReposOwnerRepoIssuesCommentsIdReactions(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
