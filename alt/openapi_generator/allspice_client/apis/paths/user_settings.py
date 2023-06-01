from allspice_client.paths.user_settings.get import ApiForget
from allspice_client.paths.user_settings.patch import ApiForpatch


class UserSettings(
    ApiForget,
    ApiForpatch,
):
    pass
