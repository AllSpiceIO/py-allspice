from allspice_client.paths.repos_owner_repo_milestones_id.get import ApiForget
from allspice_client.paths.repos_owner_repo_milestones_id.delete import ApiFordelete
from allspice_client.paths.repos_owner_repo_milestones_id.patch import ApiForpatch


class ReposOwnerRepoMilestonesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
