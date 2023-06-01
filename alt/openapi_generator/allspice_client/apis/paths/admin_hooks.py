from allspice_client.paths.admin_hooks.get import ApiForget
from allspice_client.paths.admin_hooks.post import ApiForpost


class AdminHooks(
    ApiForget,
    ApiForpost,
):
    pass
