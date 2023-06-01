from allspice_client.paths.orgs_org_labels_id.get import ApiForget
from allspice_client.paths.orgs_org_labels_id.delete import ApiFordelete
from allspice_client.paths.orgs_org_labels_id.patch import ApiForpatch


class OrgsOrgLabelsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
