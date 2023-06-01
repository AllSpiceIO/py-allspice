from allspice_client.paths.repos_owner_repo_contents_filepath.get import ApiForget
from allspice_client.paths.repos_owner_repo_contents_filepath.put import ApiForput
from allspice_client.paths.repos_owner_repo_contents_filepath.post import ApiForpost
from allspice_client.paths.repos_owner_repo_contents_filepath.delete import ApiFordelete


class ReposOwnerRepoContentsFilepath(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
