from allspice_client.paths.repos_owner_repo_subscription.get import ApiForget
from allspice_client.paths.repos_owner_repo_subscription.put import ApiForput
from allspice_client.paths.repos_owner_repo_subscription.delete import ApiFordelete


class ReposOwnerRepoSubscription(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
