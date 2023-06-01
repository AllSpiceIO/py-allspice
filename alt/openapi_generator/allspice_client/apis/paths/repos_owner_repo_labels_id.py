from allspice_client.paths.repos_owner_repo_labels_id.get import ApiForget
from allspice_client.paths.repos_owner_repo_labels_id.delete import ApiFordelete
from allspice_client.paths.repos_owner_repo_labels_id.patch import ApiForpatch


class ReposOwnerRepoLabelsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
