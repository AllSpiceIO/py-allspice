from allspice_client.paths.admin_hooks_id.get import ApiForget
from allspice_client.paths.admin_hooks_id.delete import ApiFordelete
from allspice_client.paths.admin_hooks_id.patch import ApiForpatch


class AdminHooksId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
