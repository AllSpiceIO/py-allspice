from allspice_client.paths.repos_owner_repo_issues_index_labels.get import ApiForget
from allspice_client.paths.repos_owner_repo_issues_index_labels.put import ApiForput
from allspice_client.paths.repos_owner_repo_issues_index_labels.post import ApiForpost
from allspice_client.paths.repos_owner_repo_issues_index_labels.delete import ApiFordelete


class ReposOwnerRepoIssuesIndexLabels(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
