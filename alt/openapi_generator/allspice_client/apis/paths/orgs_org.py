from allspice_client.paths.orgs_org.get import ApiForget
from allspice_client.paths.orgs_org.delete import ApiFordelete
from allspice_client.paths.orgs_org.patch import ApiForpatch


class OrgsOrg(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
