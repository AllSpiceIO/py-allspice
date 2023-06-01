from allspice_client.paths.user_following_username.get import ApiForget
from allspice_client.paths.user_following_username.put import ApiForput
from allspice_client.paths.user_following_username.delete import ApiFordelete


class UserFollowingUsername(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
