from allspice_client.paths.repos_owner_repo_branch_protections_name.get import ApiForget
from allspice_client.paths.repos_owner_repo_branch_protections_name.delete import ApiFordelete
from allspice_client.paths.repos_owner_repo_branch_protections_name.patch import ApiForpatch


class ReposOwnerRepoBranchProtectionsName(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
