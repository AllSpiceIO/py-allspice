from allspice_client.paths.orgs_org_hooks_id.get import ApiForget
from allspice_client.paths.orgs_org_hooks_id.delete import ApiFordelete
from allspice_client.paths.orgs_org_hooks_id.patch import ApiForpatch


class OrgsOrgHooksId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
