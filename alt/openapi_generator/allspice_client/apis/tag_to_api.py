import typing_extensions

from allspice_client.apis.tags import TagValues
from allspice_client.apis.tags.activitypub_api import ActivitypubApi
from allspice_client.apis.tags.admin_api import AdminApi
from allspice_client.apis.tags.issue_api import IssueApi
from allspice_client.apis.tags.miscellaneous_api import MiscellaneousApi
from allspice_client.apis.tags.notification_api import NotificationApi
from allspice_client.apis.tags.organization_api import OrganizationApi
from allspice_client.apis.tags.package_api import PackageApi
from allspice_client.apis.tags.repository_api import RepositoryApi
from allspice_client.apis.tags.user_api import UserApi
from allspice_client.apis.tags.settings_api import SettingsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACTIVITYPUB: ActivitypubApi,
        TagValues.ADMIN: AdminApi,
        TagValues.ISSUE: IssueApi,
        TagValues.MISCELLANEOUS: MiscellaneousApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.PACKAGE: PackageApi,
        TagValues.REPOSITORY: RepositoryApi,
        TagValues.USER: UserApi,
        TagValues.SETTINGS: SettingsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACTIVITYPUB: ActivitypubApi,
        TagValues.ADMIN: AdminApi,
        TagValues.ISSUE: IssueApi,
        TagValues.MISCELLANEOUS: MiscellaneousApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.PACKAGE: PackageApi,
        TagValues.REPOSITORY: RepositoryApi,
        TagValues.USER: UserApi,
        TagValues.SETTINGS: SettingsApi,
    }
)
