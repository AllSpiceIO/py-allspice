import typing_extensions

from allspice_client.paths import PathValues
from allspice_client.apis.paths.activitypub_user_id_user_id import ActivitypubUserIdUserId
from allspice_client.apis.paths.activitypub_user_id_user_id_inbox import ActivitypubUserIdUserIdInbox
from allspice_client.apis.paths.admin_cron import AdminCron
from allspice_client.apis.paths.admin_cron_task import AdminCronTask
from allspice_client.apis.paths.admin_hooks import AdminHooks
from allspice_client.apis.paths.admin_hooks_id import AdminHooksId
from allspice_client.apis.paths.admin_orgs import AdminOrgs
from allspice_client.apis.paths.admin_unadopted import AdminUnadopted
from allspice_client.apis.paths.admin_unadopted_owner_repo import AdminUnadoptedOwnerRepo
from allspice_client.apis.paths.admin_users import AdminUsers
from allspice_client.apis.paths.admin_users_username import AdminUsersUsername
from allspice_client.apis.paths.admin_users_username_keys import AdminUsersUsernameKeys
from allspice_client.apis.paths.admin_users_username_keys_id import AdminUsersUsernameKeysId
from allspice_client.apis.paths.admin_users_username_orgs import AdminUsersUsernameOrgs
from allspice_client.apis.paths.admin_users_username_repos import AdminUsersUsernameRepos
from allspice_client.apis.paths.markdown import Markdown
from allspice_client.apis.paths.markdown_raw import MarkdownRaw
from allspice_client.apis.paths.nodeinfo import Nodeinfo
from allspice_client.apis.paths.notifications import Notifications
from allspice_client.apis.paths.notifications_new import NotificationsNew
from allspice_client.apis.paths.notifications_threads_id import NotificationsThreadsId
from allspice_client.apis.paths.org_org_repos import OrgOrgRepos
from allspice_client.apis.paths.orgs import Orgs
from allspice_client.apis.paths.orgs_org import OrgsOrg
from allspice_client.apis.paths.orgs_org_hooks import OrgsOrgHooks
from allspice_client.apis.paths.orgs_org_hooks_id import OrgsOrgHooksId
from allspice_client.apis.paths.orgs_org_labels import OrgsOrgLabels
from allspice_client.apis.paths.orgs_org_labels_id import OrgsOrgLabelsId
from allspice_client.apis.paths.orgs_org_members import OrgsOrgMembers
from allspice_client.apis.paths.orgs_org_members_username import OrgsOrgMembersUsername
from allspice_client.apis.paths.orgs_org_public_members import OrgsOrgPublicMembers
from allspice_client.apis.paths.orgs_org_public_members_username import OrgsOrgPublicMembersUsername
from allspice_client.apis.paths.orgs_org_repos import OrgsOrgRepos
from allspice_client.apis.paths.orgs_org_teams import OrgsOrgTeams
from allspice_client.apis.paths.orgs_org_teams_search import OrgsOrgTeamsSearch
from allspice_client.apis.paths.packages_owner import PackagesOwner
from allspice_client.apis.paths.packages_owner_type_name_version import PackagesOwnerTypeNameVersion
from allspice_client.apis.paths.packages_owner_type_name_version_files import PackagesOwnerTypeNameVersionFiles
from allspice_client.apis.paths.repos_issues_search import ReposIssuesSearch
from allspice_client.apis.paths.repos_migrate import ReposMigrate
from allspice_client.apis.paths.repos_search import ReposSearch
from allspice_client.apis.paths.repos_owner_repo import ReposOwnerRepo
from allspice_client.apis.paths.repos_owner_repo_allspice_generated_json_filepath import ReposOwnerRepoAllspiceGeneratedJsonFilepath
from allspice_client.apis.paths.repos_owner_repo_allspice_generated_svg_filepath import ReposOwnerRepoAllspiceGeneratedSvgFilepath
from allspice_client.apis.paths.repos_owner_repo_archive_archive import ReposOwnerRepoArchiveArchive
from allspice_client.apis.paths.repos_owner_repo_assignees import ReposOwnerRepoAssignees
from allspice_client.apis.paths.repos_owner_repo_branch_protections import ReposOwnerRepoBranchProtections
from allspice_client.apis.paths.repos_owner_repo_branch_protections_name import ReposOwnerRepoBranchProtectionsName
from allspice_client.apis.paths.repos_owner_repo_branches import ReposOwnerRepoBranches
from allspice_client.apis.paths.repos_owner_repo_branches_branch import ReposOwnerRepoBranchesBranch
from allspice_client.apis.paths.repos_owner_repo_collaborators import ReposOwnerRepoCollaborators
from allspice_client.apis.paths.repos_owner_repo_collaborators_collaborator import ReposOwnerRepoCollaboratorsCollaborator
from allspice_client.apis.paths.repos_owner_repo_collaborators_collaborator_permission import ReposOwnerRepoCollaboratorsCollaboratorPermission
from allspice_client.apis.paths.repos_owner_repo_commits import ReposOwnerRepoCommits
from allspice_client.apis.paths.repos_owner_repo_commits_ref_status import ReposOwnerRepoCommitsRefStatus
from allspice_client.apis.paths.repos_owner_repo_commits_ref_statuses import ReposOwnerRepoCommitsRefStatuses
from allspice_client.apis.paths.repos_owner_repo_contents import ReposOwnerRepoContents
from allspice_client.apis.paths.repos_owner_repo_contents_filepath import ReposOwnerRepoContentsFilepath
from allspice_client.apis.paths.repos_owner_repo_diffpatch import ReposOwnerRepoDiffpatch
from allspice_client.apis.paths.repos_owner_repo_editorconfig_filepath import ReposOwnerRepoEditorconfigFilepath
from allspice_client.apis.paths.repos_owner_repo_forks import ReposOwnerRepoForks
from allspice_client.apis.paths.repos_owner_repo_git_blobs_sha import ReposOwnerRepoGitBlobsSha
from allspice_client.apis.paths.repos_owner_repo_git_commits_sha import ReposOwnerRepoGitCommitsSha
from allspice_client.apis.paths.repos_owner_repo_git_commits_sha_diff_type import ReposOwnerRepoGitCommitsShaDiffType
from allspice_client.apis.paths.repos_owner_repo_git_notes_sha import ReposOwnerRepoGitNotesSha
from allspice_client.apis.paths.repos_owner_repo_git_refs import ReposOwnerRepoGitRefs
from allspice_client.apis.paths.repos_owner_repo_git_refs_ref import ReposOwnerRepoGitRefsRef
from allspice_client.apis.paths.repos_owner_repo_git_tags_sha import ReposOwnerRepoGitTagsSha
from allspice_client.apis.paths.repos_owner_repo_git_trees_sha import ReposOwnerRepoGitTreesSha
from allspice_client.apis.paths.repos_owner_repo_hooks import ReposOwnerRepoHooks
from allspice_client.apis.paths.repos_owner_repo_hooks_git import ReposOwnerRepoHooksGit
from allspice_client.apis.paths.repos_owner_repo_hooks_git_id import ReposOwnerRepoHooksGitId
from allspice_client.apis.paths.repos_owner_repo_hooks_id import ReposOwnerRepoHooksId
from allspice_client.apis.paths.repos_owner_repo_hooks_id_tests import ReposOwnerRepoHooksIdTests
from allspice_client.apis.paths.repos_owner_repo_issue_templates import ReposOwnerRepoIssueTemplates
from allspice_client.apis.paths.repos_owner_repo_issues import ReposOwnerRepoIssues
from allspice_client.apis.paths.repos_owner_repo_issues_comments import ReposOwnerRepoIssuesComments
from allspice_client.apis.paths.repos_owner_repo_issues_comments_id import ReposOwnerRepoIssuesCommentsId
from allspice_client.apis.paths.repos_owner_repo_issues_comments_id_assets import ReposOwnerRepoIssuesCommentsIdAssets
from allspice_client.apis.paths.repos_owner_repo_issues_comments_id_assets_attachment_id import ReposOwnerRepoIssuesCommentsIdAssetsAttachmentId
from allspice_client.apis.paths.repos_owner_repo_issues_comments_id_reactions import ReposOwnerRepoIssuesCommentsIdReactions
from allspice_client.apis.paths.repos_owner_repo_issues_index import ReposOwnerRepoIssuesIndex
from allspice_client.apis.paths.repos_owner_repo_issues_index_assets import ReposOwnerRepoIssuesIndexAssets
from allspice_client.apis.paths.repos_owner_repo_issues_index_assets_attachment_id import ReposOwnerRepoIssuesIndexAssetsAttachmentId
from allspice_client.apis.paths.repos_owner_repo_issues_index_comments import ReposOwnerRepoIssuesIndexComments
from allspice_client.apis.paths.repos_owner_repo_issues_index_comments_id import ReposOwnerRepoIssuesIndexCommentsId
from allspice_client.apis.paths.repos_owner_repo_issues_index_deadline import ReposOwnerRepoIssuesIndexDeadline
from allspice_client.apis.paths.repos_owner_repo_issues_index_labels import ReposOwnerRepoIssuesIndexLabels
from allspice_client.apis.paths.repos_owner_repo_issues_index_labels_id import ReposOwnerRepoIssuesIndexLabelsId
from allspice_client.apis.paths.repos_owner_repo_issues_index_reactions import ReposOwnerRepoIssuesIndexReactions
from allspice_client.apis.paths.repos_owner_repo_issues_index_stopwatch_delete import ReposOwnerRepoIssuesIndexStopwatchDelete
from allspice_client.apis.paths.repos_owner_repo_issues_index_stopwatch_start import ReposOwnerRepoIssuesIndexStopwatchStart
from allspice_client.apis.paths.repos_owner_repo_issues_index_stopwatch_stop import ReposOwnerRepoIssuesIndexStopwatchStop
from allspice_client.apis.paths.repos_owner_repo_issues_index_subscriptions import ReposOwnerRepoIssuesIndexSubscriptions
from allspice_client.apis.paths.repos_owner_repo_issues_index_subscriptions_check import ReposOwnerRepoIssuesIndexSubscriptionsCheck
from allspice_client.apis.paths.repos_owner_repo_issues_index_subscriptions_user import ReposOwnerRepoIssuesIndexSubscriptionsUser
from allspice_client.apis.paths.repos_owner_repo_issues_index_timeline import ReposOwnerRepoIssuesIndexTimeline
from allspice_client.apis.paths.repos_owner_repo_issues_index_times import ReposOwnerRepoIssuesIndexTimes
from allspice_client.apis.paths.repos_owner_repo_issues_index_times_id import ReposOwnerRepoIssuesIndexTimesId
from allspice_client.apis.paths.repos_owner_repo_keys import ReposOwnerRepoKeys
from allspice_client.apis.paths.repos_owner_repo_keys_id import ReposOwnerRepoKeysId
from allspice_client.apis.paths.repos_owner_repo_labels import ReposOwnerRepoLabels
from allspice_client.apis.paths.repos_owner_repo_labels_id import ReposOwnerRepoLabelsId
from allspice_client.apis.paths.repos_owner_repo_languages import ReposOwnerRepoLanguages
from allspice_client.apis.paths.repos_owner_repo_media_filepath import ReposOwnerRepoMediaFilepath
from allspice_client.apis.paths.repos_owner_repo_milestones import ReposOwnerRepoMilestones
from allspice_client.apis.paths.repos_owner_repo_milestones_id import ReposOwnerRepoMilestonesId
from allspice_client.apis.paths.repos_owner_repo_mirror_sync import ReposOwnerRepoMirrorSync
from allspice_client.apis.paths.repos_owner_repo_notifications import ReposOwnerRepoNotifications
from allspice_client.apis.paths.repos_owner_repo_pulls import ReposOwnerRepoPulls
from allspice_client.apis.paths.repos_owner_repo_pulls_index import ReposOwnerRepoPullsIndex
from allspice_client.apis.paths.repos_owner_repo_pulls_index_diff_type import ReposOwnerRepoPullsIndexDiffType
from allspice_client.apis.paths.repos_owner_repo_pulls_index_commits import ReposOwnerRepoPullsIndexCommits
from allspice_client.apis.paths.repos_owner_repo_pulls_index_files import ReposOwnerRepoPullsIndexFiles
from allspice_client.apis.paths.repos_owner_repo_pulls_index_merge import ReposOwnerRepoPullsIndexMerge
from allspice_client.apis.paths.repos_owner_repo_pulls_index_requested_reviewers import ReposOwnerRepoPullsIndexRequestedReviewers
from allspice_client.apis.paths.repos_owner_repo_pulls_index_reviews import ReposOwnerRepoPullsIndexReviews
from allspice_client.apis.paths.repos_owner_repo_pulls_index_reviews_id import ReposOwnerRepoPullsIndexReviewsId
from allspice_client.apis.paths.repos_owner_repo_pulls_index_reviews_id_comments import ReposOwnerRepoPullsIndexReviewsIdComments
from allspice_client.apis.paths.repos_owner_repo_pulls_index_reviews_id_dismissals import ReposOwnerRepoPullsIndexReviewsIdDismissals
from allspice_client.apis.paths.repos_owner_repo_pulls_index_reviews_id_undismissals import ReposOwnerRepoPullsIndexReviewsIdUndismissals
from allspice_client.apis.paths.repos_owner_repo_pulls_index_update import ReposOwnerRepoPullsIndexUpdate
from allspice_client.apis.paths.repos_owner_repo_push_mirrors import ReposOwnerRepoPushMirrors
from allspice_client.apis.paths.repos_owner_repo_push_mirrors_sync import ReposOwnerRepoPushMirrorsSync
from allspice_client.apis.paths.repos_owner_repo_push_mirrors_name import ReposOwnerRepoPushMirrorsName
from allspice_client.apis.paths.repos_owner_repo_raw_filepath import ReposOwnerRepoRawFilepath
from allspice_client.apis.paths.repos_owner_repo_releases import ReposOwnerRepoReleases
from allspice_client.apis.paths.repos_owner_repo_releases_latest import ReposOwnerRepoReleasesLatest
from allspice_client.apis.paths.repos_owner_repo_releases_tags_tag import ReposOwnerRepoReleasesTagsTag
from allspice_client.apis.paths.repos_owner_repo_releases_id import ReposOwnerRepoReleasesId
from allspice_client.apis.paths.repos_owner_repo_releases_id_assets import ReposOwnerRepoReleasesIdAssets
from allspice_client.apis.paths.repos_owner_repo_releases_id_assets_attachment_id import ReposOwnerRepoReleasesIdAssetsAttachmentId
from allspice_client.apis.paths.repos_owner_repo_reviewers import ReposOwnerRepoReviewers
from allspice_client.apis.paths.repos_owner_repo_signing_key_gpg import ReposOwnerRepoSigningKeyGpg
from allspice_client.apis.paths.repos_owner_repo_stargazers import ReposOwnerRepoStargazers
from allspice_client.apis.paths.repos_owner_repo_statuses_sha import ReposOwnerRepoStatusesSha
from allspice_client.apis.paths.repos_owner_repo_subscribers import ReposOwnerRepoSubscribers
from allspice_client.apis.paths.repos_owner_repo_subscription import ReposOwnerRepoSubscription
from allspice_client.apis.paths.repos_owner_repo_tags import ReposOwnerRepoTags
from allspice_client.apis.paths.repos_owner_repo_tags_tag import ReposOwnerRepoTagsTag
from allspice_client.apis.paths.repos_owner_repo_teams import ReposOwnerRepoTeams
from allspice_client.apis.paths.repos_owner_repo_teams_team import ReposOwnerRepoTeamsTeam
from allspice_client.apis.paths.repos_owner_repo_times import ReposOwnerRepoTimes
from allspice_client.apis.paths.repos_owner_repo_times_user import ReposOwnerRepoTimesUser
from allspice_client.apis.paths.repos_owner_repo_topics import ReposOwnerRepoTopics
from allspice_client.apis.paths.repos_owner_repo_topics_topic import ReposOwnerRepoTopicsTopic
from allspice_client.apis.paths.repos_owner_repo_transfer import ReposOwnerRepoTransfer
from allspice_client.apis.paths.repos_owner_repo_transfer_accept import ReposOwnerRepoTransferAccept
from allspice_client.apis.paths.repos_owner_repo_transfer_reject import ReposOwnerRepoTransferReject
from allspice_client.apis.paths.repos_owner_repo_wiki_new import ReposOwnerRepoWikiNew
from allspice_client.apis.paths.repos_owner_repo_wiki_page_page_name import ReposOwnerRepoWikiPagePageName
from allspice_client.apis.paths.repos_owner_repo_wiki_pages import ReposOwnerRepoWikiPages
from allspice_client.apis.paths.repos_owner_repo_wiki_revisions_page_name import ReposOwnerRepoWikiRevisionsPageName
from allspice_client.apis.paths.repos_template_owner_template_repo_generate import ReposTemplateOwnerTemplateRepoGenerate
from allspice_client.apis.paths.repositories_id import RepositoriesId
from allspice_client.apis.paths.settings_api import SettingsApi
from allspice_client.apis.paths.settings_attachment import SettingsAttachment
from allspice_client.apis.paths.settings_repository import SettingsRepository
from allspice_client.apis.paths.settings_ui import SettingsUi
from allspice_client.apis.paths.signing_key_gpg import SigningKeyGpg
from allspice_client.apis.paths.teams_id import TeamsId
from allspice_client.apis.paths.teams_id_members import TeamsIdMembers
from allspice_client.apis.paths.teams_id_members_username import TeamsIdMembersUsername
from allspice_client.apis.paths.teams_id_repos import TeamsIdRepos
from allspice_client.apis.paths.teams_id_repos_org_repo import TeamsIdReposOrgRepo
from allspice_client.apis.paths.topics_search import TopicsSearch
from allspice_client.apis.paths.user import User
from allspice_client.apis.paths.user_applications_oauth2 import UserApplicationsOauth2
from allspice_client.apis.paths.user_applications_oauth2_id import UserApplicationsOauth2Id
from allspice_client.apis.paths.user_emails import UserEmails
from allspice_client.apis.paths.user_followers import UserFollowers
from allspice_client.apis.paths.user_following import UserFollowing
from allspice_client.apis.paths.user_following_username import UserFollowingUsername
from allspice_client.apis.paths.user_gpg_key_token import UserGpgKeyToken
from allspice_client.apis.paths.user_gpg_key_verify import UserGpgKeyVerify
from allspice_client.apis.paths.user_gpg_keys import UserGpgKeys
from allspice_client.apis.paths.user_gpg_keys_id import UserGpgKeysId
from allspice_client.apis.paths.user_keys import UserKeys
from allspice_client.apis.paths.user_keys_id import UserKeysId
from allspice_client.apis.paths.user_orgs import UserOrgs
from allspice_client.apis.paths.user_repos import UserRepos
from allspice_client.apis.paths.user_settings import UserSettings
from allspice_client.apis.paths.user_starred import UserStarred
from allspice_client.apis.paths.user_starred_owner_repo import UserStarredOwnerRepo
from allspice_client.apis.paths.user_stopwatches import UserStopwatches
from allspice_client.apis.paths.user_subscriptions import UserSubscriptions
from allspice_client.apis.paths.user_teams import UserTeams
from allspice_client.apis.paths.user_times import UserTimes
from allspice_client.apis.paths.users_search import UsersSearch
from allspice_client.apis.paths.users_username import UsersUsername
from allspice_client.apis.paths.users_username_followers import UsersUsernameFollowers
from allspice_client.apis.paths.users_username_following import UsersUsernameFollowing
from allspice_client.apis.paths.users_username_following_target import UsersUsernameFollowingTarget
from allspice_client.apis.paths.users_username_gpg_keys import UsersUsernameGpgKeys
from allspice_client.apis.paths.users_username_heatmap import UsersUsernameHeatmap
from allspice_client.apis.paths.users_username_keys import UsersUsernameKeys
from allspice_client.apis.paths.users_username_orgs import UsersUsernameOrgs
from allspice_client.apis.paths.users_username_orgs_org_permissions import UsersUsernameOrgsOrgPermissions
from allspice_client.apis.paths.users_username_repos import UsersUsernameRepos
from allspice_client.apis.paths.users_username_starred import UsersUsernameStarred
from allspice_client.apis.paths.users_username_subscriptions import UsersUsernameSubscriptions
from allspice_client.apis.paths.users_username_tokens import UsersUsernameTokens
from allspice_client.apis.paths.users_username_tokens_token import UsersUsernameTokensToken
from allspice_client.apis.paths.version import Version

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACTIVITYPUB_USERID_USERID: ActivitypubUserIdUserId,
        PathValues.ACTIVITYPUB_USERID_USERID_INBOX: ActivitypubUserIdUserIdInbox,
        PathValues.ADMIN_CRON: AdminCron,
        PathValues.ADMIN_CRON_TASK: AdminCronTask,
        PathValues.ADMIN_HOOKS: AdminHooks,
        PathValues.ADMIN_HOOKS_ID: AdminHooksId,
        PathValues.ADMIN_ORGS: AdminOrgs,
        PathValues.ADMIN_UNADOPTED: AdminUnadopted,
        PathValues.ADMIN_UNADOPTED_OWNER_REPO: AdminUnadoptedOwnerRepo,
        PathValues.ADMIN_USERS: AdminUsers,
        PathValues.ADMIN_USERS_USERNAME: AdminUsersUsername,
        PathValues.ADMIN_USERS_USERNAME_KEYS: AdminUsersUsernameKeys,
        PathValues.ADMIN_USERS_USERNAME_KEYS_ID: AdminUsersUsernameKeysId,
        PathValues.ADMIN_USERS_USERNAME_ORGS: AdminUsersUsernameOrgs,
        PathValues.ADMIN_USERS_USERNAME_REPOS: AdminUsersUsernameRepos,
        PathValues.MARKDOWN: Markdown,
        PathValues.MARKDOWN_RAW: MarkdownRaw,
        PathValues.NODEINFO: Nodeinfo,
        PathValues.NOTIFICATIONS: Notifications,
        PathValues.NOTIFICATIONS_NEW: NotificationsNew,
        PathValues.NOTIFICATIONS_THREADS_ID: NotificationsThreadsId,
        PathValues.ORG_ORG_REPOS: OrgOrgRepos,
        PathValues.ORGS: Orgs,
        PathValues.ORGS_ORG: OrgsOrg,
        PathValues.ORGS_ORG_HOOKS: OrgsOrgHooks,
        PathValues.ORGS_ORG_HOOKS_ID: OrgsOrgHooksId,
        PathValues.ORGS_ORG_LABELS: OrgsOrgLabels,
        PathValues.ORGS_ORG_LABELS_ID: OrgsOrgLabelsId,
        PathValues.ORGS_ORG_MEMBERS: OrgsOrgMembers,
        PathValues.ORGS_ORG_MEMBERS_USERNAME: OrgsOrgMembersUsername,
        PathValues.ORGS_ORG_PUBLIC_MEMBERS: OrgsOrgPublicMembers,
        PathValues.ORGS_ORG_PUBLIC_MEMBERS_USERNAME: OrgsOrgPublicMembersUsername,
        PathValues.ORGS_ORG_REPOS: OrgsOrgRepos,
        PathValues.ORGS_ORG_TEAMS: OrgsOrgTeams,
        PathValues.ORGS_ORG_TEAMS_SEARCH: OrgsOrgTeamsSearch,
        PathValues.PACKAGES_OWNER: PackagesOwner,
        PathValues.PACKAGES_OWNER_TYPE_NAME_VERSION: PackagesOwnerTypeNameVersion,
        PathValues.PACKAGES_OWNER_TYPE_NAME_VERSION_FILES: PackagesOwnerTypeNameVersionFiles,
        PathValues.REPOS_ISSUES_SEARCH: ReposIssuesSearch,
        PathValues.REPOS_MIGRATE: ReposMigrate,
        PathValues.REPOS_SEARCH: ReposSearch,
        PathValues.REPOS_OWNER_REPO: ReposOwnerRepo,
        PathValues.REPOS_OWNER_REPO_ALLSPICE_GENERATED_JSON_FILEPATH: ReposOwnerRepoAllspiceGeneratedJsonFilepath,
        PathValues.REPOS_OWNER_REPO_ALLSPICE_GENERATED_SVG_FILEPATH: ReposOwnerRepoAllspiceGeneratedSvgFilepath,
        PathValues.REPOS_OWNER_REPO_ARCHIVE_ARCHIVE: ReposOwnerRepoArchiveArchive,
        PathValues.REPOS_OWNER_REPO_ASSIGNEES: ReposOwnerRepoAssignees,
        PathValues.REPOS_OWNER_REPO_BRANCH_PROTECTIONS: ReposOwnerRepoBranchProtections,
        PathValues.REPOS_OWNER_REPO_BRANCH_PROTECTIONS_NAME: ReposOwnerRepoBranchProtectionsName,
        PathValues.REPOS_OWNER_REPO_BRANCHES: ReposOwnerRepoBranches,
        PathValues.REPOS_OWNER_REPO_BRANCHES_BRANCH: ReposOwnerRepoBranchesBranch,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS: ReposOwnerRepoCollaborators,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS_COLLABORATOR: ReposOwnerRepoCollaboratorsCollaborator,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS_COLLABORATOR_PERMISSION: ReposOwnerRepoCollaboratorsCollaboratorPermission,
        PathValues.REPOS_OWNER_REPO_COMMITS: ReposOwnerRepoCommits,
        PathValues.REPOS_OWNER_REPO_COMMITS_REF_STATUS: ReposOwnerRepoCommitsRefStatus,
        PathValues.REPOS_OWNER_REPO_COMMITS_REF_STATUSES: ReposOwnerRepoCommitsRefStatuses,
        PathValues.REPOS_OWNER_REPO_CONTENTS: ReposOwnerRepoContents,
        PathValues.REPOS_OWNER_REPO_CONTENTS_FILEPATH: ReposOwnerRepoContentsFilepath,
        PathValues.REPOS_OWNER_REPO_DIFFPATCH: ReposOwnerRepoDiffpatch,
        PathValues.REPOS_OWNER_REPO_EDITORCONFIG_FILEPATH: ReposOwnerRepoEditorconfigFilepath,
        PathValues.REPOS_OWNER_REPO_FORKS: ReposOwnerRepoForks,
        PathValues.REPOS_OWNER_REPO_GIT_BLOBS_SHA: ReposOwnerRepoGitBlobsSha,
        PathValues.REPOS_OWNER_REPO_GIT_COMMITS_SHA: ReposOwnerRepoGitCommitsSha,
        PathValues.REPOS_OWNER_REPO_GIT_COMMITS_SHA_DIFF_TYPE: ReposOwnerRepoGitCommitsShaDiffType,
        PathValues.REPOS_OWNER_REPO_GIT_NOTES_SHA: ReposOwnerRepoGitNotesSha,
        PathValues.REPOS_OWNER_REPO_GIT_REFS: ReposOwnerRepoGitRefs,
        PathValues.REPOS_OWNER_REPO_GIT_REFS_REF: ReposOwnerRepoGitRefsRef,
        PathValues.REPOS_OWNER_REPO_GIT_TAGS_SHA: ReposOwnerRepoGitTagsSha,
        PathValues.REPOS_OWNER_REPO_GIT_TREES_SHA: ReposOwnerRepoGitTreesSha,
        PathValues.REPOS_OWNER_REPO_HOOKS: ReposOwnerRepoHooks,
        PathValues.REPOS_OWNER_REPO_HOOKS_GIT: ReposOwnerRepoHooksGit,
        PathValues.REPOS_OWNER_REPO_HOOKS_GIT_ID: ReposOwnerRepoHooksGitId,
        PathValues.REPOS_OWNER_REPO_HOOKS_ID: ReposOwnerRepoHooksId,
        PathValues.REPOS_OWNER_REPO_HOOKS_ID_TESTS: ReposOwnerRepoHooksIdTests,
        PathValues.REPOS_OWNER_REPO_ISSUE_TEMPLATES: ReposOwnerRepoIssueTemplates,
        PathValues.REPOS_OWNER_REPO_ISSUES: ReposOwnerRepoIssues,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS: ReposOwnerRepoIssuesComments,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID: ReposOwnerRepoIssuesCommentsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_ASSETS: ReposOwnerRepoIssuesCommentsIdAssets,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_ASSETS_ATTACHMENT_ID: ReposOwnerRepoIssuesCommentsIdAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_REACTIONS: ReposOwnerRepoIssuesCommentsIdReactions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX: ReposOwnerRepoIssuesIndex,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_ASSETS: ReposOwnerRepoIssuesIndexAssets,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_ASSETS_ATTACHMENT_ID: ReposOwnerRepoIssuesIndexAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_COMMENTS: ReposOwnerRepoIssuesIndexComments,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_COMMENTS_ID: ReposOwnerRepoIssuesIndexCommentsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_DEADLINE: ReposOwnerRepoIssuesIndexDeadline,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_LABELS: ReposOwnerRepoIssuesIndexLabels,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_LABELS_ID: ReposOwnerRepoIssuesIndexLabelsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_REACTIONS: ReposOwnerRepoIssuesIndexReactions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_DELETE: ReposOwnerRepoIssuesIndexStopwatchDelete,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_START: ReposOwnerRepoIssuesIndexStopwatchStart,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_STOP: ReposOwnerRepoIssuesIndexStopwatchStop,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS: ReposOwnerRepoIssuesIndexSubscriptions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS_CHECK: ReposOwnerRepoIssuesIndexSubscriptionsCheck,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS_USER: ReposOwnerRepoIssuesIndexSubscriptionsUser,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMELINE: ReposOwnerRepoIssuesIndexTimeline,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMES: ReposOwnerRepoIssuesIndexTimes,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMES_ID: ReposOwnerRepoIssuesIndexTimesId,
        PathValues.REPOS_OWNER_REPO_KEYS: ReposOwnerRepoKeys,
        PathValues.REPOS_OWNER_REPO_KEYS_ID: ReposOwnerRepoKeysId,
        PathValues.REPOS_OWNER_REPO_LABELS: ReposOwnerRepoLabels,
        PathValues.REPOS_OWNER_REPO_LABELS_ID: ReposOwnerRepoLabelsId,
        PathValues.REPOS_OWNER_REPO_LANGUAGES: ReposOwnerRepoLanguages,
        PathValues.REPOS_OWNER_REPO_MEDIA_FILEPATH: ReposOwnerRepoMediaFilepath,
        PathValues.REPOS_OWNER_REPO_MILESTONES: ReposOwnerRepoMilestones,
        PathValues.REPOS_OWNER_REPO_MILESTONES_ID: ReposOwnerRepoMilestonesId,
        PathValues.REPOS_OWNER_REPO_MIRRORSYNC: ReposOwnerRepoMirrorSync,
        PathValues.REPOS_OWNER_REPO_NOTIFICATIONS: ReposOwnerRepoNotifications,
        PathValues.REPOS_OWNER_REPO_PULLS: ReposOwnerRepoPulls,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX: ReposOwnerRepoPullsIndex,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_DIFF_TYPE: ReposOwnerRepoPullsIndexDiffType,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_COMMITS: ReposOwnerRepoPullsIndexCommits,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_FILES: ReposOwnerRepoPullsIndexFiles,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_MERGE: ReposOwnerRepoPullsIndexMerge,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REQUESTED_REVIEWERS: ReposOwnerRepoPullsIndexRequestedReviewers,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS: ReposOwnerRepoPullsIndexReviews,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID: ReposOwnerRepoPullsIndexReviewsId,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_COMMENTS: ReposOwnerRepoPullsIndexReviewsIdComments,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_DISMISSALS: ReposOwnerRepoPullsIndexReviewsIdDismissals,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_UNDISMISSALS: ReposOwnerRepoPullsIndexReviewsIdUndismissals,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_UPDATE: ReposOwnerRepoPullsIndexUpdate,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORS: ReposOwnerRepoPushMirrors,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORSSYNC: ReposOwnerRepoPushMirrorsSync,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORS_NAME: ReposOwnerRepoPushMirrorsName,
        PathValues.REPOS_OWNER_REPO_RAW_FILEPATH: ReposOwnerRepoRawFilepath,
        PathValues.REPOS_OWNER_REPO_RELEASES: ReposOwnerRepoReleases,
        PathValues.REPOS_OWNER_REPO_RELEASES_LATEST: ReposOwnerRepoReleasesLatest,
        PathValues.REPOS_OWNER_REPO_RELEASES_TAGS_TAG: ReposOwnerRepoReleasesTagsTag,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID: ReposOwnerRepoReleasesId,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID_ASSETS: ReposOwnerRepoReleasesIdAssets,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID_ASSETS_ATTACHMENT_ID: ReposOwnerRepoReleasesIdAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_REVIEWERS: ReposOwnerRepoReviewers,
        PathValues.REPOS_OWNER_REPO_SIGNINGKEY_GPG: ReposOwnerRepoSigningKeyGpg,
        PathValues.REPOS_OWNER_REPO_STARGAZERS: ReposOwnerRepoStargazers,
        PathValues.REPOS_OWNER_REPO_STATUSES_SHA: ReposOwnerRepoStatusesSha,
        PathValues.REPOS_OWNER_REPO_SUBSCRIBERS: ReposOwnerRepoSubscribers,
        PathValues.REPOS_OWNER_REPO_SUBSCRIPTION: ReposOwnerRepoSubscription,
        PathValues.REPOS_OWNER_REPO_TAGS: ReposOwnerRepoTags,
        PathValues.REPOS_OWNER_REPO_TAGS_TAG: ReposOwnerRepoTagsTag,
        PathValues.REPOS_OWNER_REPO_TEAMS: ReposOwnerRepoTeams,
        PathValues.REPOS_OWNER_REPO_TEAMS_TEAM: ReposOwnerRepoTeamsTeam,
        PathValues.REPOS_OWNER_REPO_TIMES: ReposOwnerRepoTimes,
        PathValues.REPOS_OWNER_REPO_TIMES_USER: ReposOwnerRepoTimesUser,
        PathValues.REPOS_OWNER_REPO_TOPICS: ReposOwnerRepoTopics,
        PathValues.REPOS_OWNER_REPO_TOPICS_TOPIC: ReposOwnerRepoTopicsTopic,
        PathValues.REPOS_OWNER_REPO_TRANSFER: ReposOwnerRepoTransfer,
        PathValues.REPOS_OWNER_REPO_TRANSFER_ACCEPT: ReposOwnerRepoTransferAccept,
        PathValues.REPOS_OWNER_REPO_TRANSFER_REJECT: ReposOwnerRepoTransferReject,
        PathValues.REPOS_OWNER_REPO_WIKI_NEW: ReposOwnerRepoWikiNew,
        PathValues.REPOS_OWNER_REPO_WIKI_PAGE_PAGE_NAME: ReposOwnerRepoWikiPagePageName,
        PathValues.REPOS_OWNER_REPO_WIKI_PAGES: ReposOwnerRepoWikiPages,
        PathValues.REPOS_OWNER_REPO_WIKI_REVISIONS_PAGE_NAME: ReposOwnerRepoWikiRevisionsPageName,
        PathValues.REPOS_TEMPLATE_OWNER_TEMPLATE_REPO_GENERATE: ReposTemplateOwnerTemplateRepoGenerate,
        PathValues.REPOSITORIES_ID: RepositoriesId,
        PathValues.SETTINGS_API: SettingsApi,
        PathValues.SETTINGS_ATTACHMENT: SettingsAttachment,
        PathValues.SETTINGS_REPOSITORY: SettingsRepository,
        PathValues.SETTINGS_UI: SettingsUi,
        PathValues.SIGNINGKEY_GPG: SigningKeyGpg,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.TEAMS_ID_MEMBERS: TeamsIdMembers,
        PathValues.TEAMS_ID_MEMBERS_USERNAME: TeamsIdMembersUsername,
        PathValues.TEAMS_ID_REPOS: TeamsIdRepos,
        PathValues.TEAMS_ID_REPOS_ORG_REPO: TeamsIdReposOrgRepo,
        PathValues.TOPICS_SEARCH: TopicsSearch,
        PathValues.USER: User,
        PathValues.USER_APPLICATIONS_OAUTH2: UserApplicationsOauth2,
        PathValues.USER_APPLICATIONS_OAUTH2_ID: UserApplicationsOauth2Id,
        PathValues.USER_EMAILS: UserEmails,
        PathValues.USER_FOLLOWERS: UserFollowers,
        PathValues.USER_FOLLOWING: UserFollowing,
        PathValues.USER_FOLLOWING_USERNAME: UserFollowingUsername,
        PathValues.USER_GPG_KEY_TOKEN: UserGpgKeyToken,
        PathValues.USER_GPG_KEY_VERIFY: UserGpgKeyVerify,
        PathValues.USER_GPG_KEYS: UserGpgKeys,
        PathValues.USER_GPG_KEYS_ID: UserGpgKeysId,
        PathValues.USER_KEYS: UserKeys,
        PathValues.USER_KEYS_ID: UserKeysId,
        PathValues.USER_ORGS: UserOrgs,
        PathValues.USER_REPOS: UserRepos,
        PathValues.USER_SETTINGS: UserSettings,
        PathValues.USER_STARRED: UserStarred,
        PathValues.USER_STARRED_OWNER_REPO: UserStarredOwnerRepo,
        PathValues.USER_STOPWATCHES: UserStopwatches,
        PathValues.USER_SUBSCRIPTIONS: UserSubscriptions,
        PathValues.USER_TEAMS: UserTeams,
        PathValues.USER_TIMES: UserTimes,
        PathValues.USERS_SEARCH: UsersSearch,
        PathValues.USERS_USERNAME: UsersUsername,
        PathValues.USERS_USERNAME_FOLLOWERS: UsersUsernameFollowers,
        PathValues.USERS_USERNAME_FOLLOWING: UsersUsernameFollowing,
        PathValues.USERS_USERNAME_FOLLOWING_TARGET: UsersUsernameFollowingTarget,
        PathValues.USERS_USERNAME_GPG_KEYS: UsersUsernameGpgKeys,
        PathValues.USERS_USERNAME_HEATMAP: UsersUsernameHeatmap,
        PathValues.USERS_USERNAME_KEYS: UsersUsernameKeys,
        PathValues.USERS_USERNAME_ORGS: UsersUsernameOrgs,
        PathValues.USERS_USERNAME_ORGS_ORG_PERMISSIONS: UsersUsernameOrgsOrgPermissions,
        PathValues.USERS_USERNAME_REPOS: UsersUsernameRepos,
        PathValues.USERS_USERNAME_STARRED: UsersUsernameStarred,
        PathValues.USERS_USERNAME_SUBSCRIPTIONS: UsersUsernameSubscriptions,
        PathValues.USERS_USERNAME_TOKENS: UsersUsernameTokens,
        PathValues.USERS_USERNAME_TOKENS_TOKEN: UsersUsernameTokensToken,
        PathValues.VERSION: Version,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACTIVITYPUB_USERID_USERID: ActivitypubUserIdUserId,
        PathValues.ACTIVITYPUB_USERID_USERID_INBOX: ActivitypubUserIdUserIdInbox,
        PathValues.ADMIN_CRON: AdminCron,
        PathValues.ADMIN_CRON_TASK: AdminCronTask,
        PathValues.ADMIN_HOOKS: AdminHooks,
        PathValues.ADMIN_HOOKS_ID: AdminHooksId,
        PathValues.ADMIN_ORGS: AdminOrgs,
        PathValues.ADMIN_UNADOPTED: AdminUnadopted,
        PathValues.ADMIN_UNADOPTED_OWNER_REPO: AdminUnadoptedOwnerRepo,
        PathValues.ADMIN_USERS: AdminUsers,
        PathValues.ADMIN_USERS_USERNAME: AdminUsersUsername,
        PathValues.ADMIN_USERS_USERNAME_KEYS: AdminUsersUsernameKeys,
        PathValues.ADMIN_USERS_USERNAME_KEYS_ID: AdminUsersUsernameKeysId,
        PathValues.ADMIN_USERS_USERNAME_ORGS: AdminUsersUsernameOrgs,
        PathValues.ADMIN_USERS_USERNAME_REPOS: AdminUsersUsernameRepos,
        PathValues.MARKDOWN: Markdown,
        PathValues.MARKDOWN_RAW: MarkdownRaw,
        PathValues.NODEINFO: Nodeinfo,
        PathValues.NOTIFICATIONS: Notifications,
        PathValues.NOTIFICATIONS_NEW: NotificationsNew,
        PathValues.NOTIFICATIONS_THREADS_ID: NotificationsThreadsId,
        PathValues.ORG_ORG_REPOS: OrgOrgRepos,
        PathValues.ORGS: Orgs,
        PathValues.ORGS_ORG: OrgsOrg,
        PathValues.ORGS_ORG_HOOKS: OrgsOrgHooks,
        PathValues.ORGS_ORG_HOOKS_ID: OrgsOrgHooksId,
        PathValues.ORGS_ORG_LABELS: OrgsOrgLabels,
        PathValues.ORGS_ORG_LABELS_ID: OrgsOrgLabelsId,
        PathValues.ORGS_ORG_MEMBERS: OrgsOrgMembers,
        PathValues.ORGS_ORG_MEMBERS_USERNAME: OrgsOrgMembersUsername,
        PathValues.ORGS_ORG_PUBLIC_MEMBERS: OrgsOrgPublicMembers,
        PathValues.ORGS_ORG_PUBLIC_MEMBERS_USERNAME: OrgsOrgPublicMembersUsername,
        PathValues.ORGS_ORG_REPOS: OrgsOrgRepos,
        PathValues.ORGS_ORG_TEAMS: OrgsOrgTeams,
        PathValues.ORGS_ORG_TEAMS_SEARCH: OrgsOrgTeamsSearch,
        PathValues.PACKAGES_OWNER: PackagesOwner,
        PathValues.PACKAGES_OWNER_TYPE_NAME_VERSION: PackagesOwnerTypeNameVersion,
        PathValues.PACKAGES_OWNER_TYPE_NAME_VERSION_FILES: PackagesOwnerTypeNameVersionFiles,
        PathValues.REPOS_ISSUES_SEARCH: ReposIssuesSearch,
        PathValues.REPOS_MIGRATE: ReposMigrate,
        PathValues.REPOS_SEARCH: ReposSearch,
        PathValues.REPOS_OWNER_REPO: ReposOwnerRepo,
        PathValues.REPOS_OWNER_REPO_ALLSPICE_GENERATED_JSON_FILEPATH: ReposOwnerRepoAllspiceGeneratedJsonFilepath,
        PathValues.REPOS_OWNER_REPO_ALLSPICE_GENERATED_SVG_FILEPATH: ReposOwnerRepoAllspiceGeneratedSvgFilepath,
        PathValues.REPOS_OWNER_REPO_ARCHIVE_ARCHIVE: ReposOwnerRepoArchiveArchive,
        PathValues.REPOS_OWNER_REPO_ASSIGNEES: ReposOwnerRepoAssignees,
        PathValues.REPOS_OWNER_REPO_BRANCH_PROTECTIONS: ReposOwnerRepoBranchProtections,
        PathValues.REPOS_OWNER_REPO_BRANCH_PROTECTIONS_NAME: ReposOwnerRepoBranchProtectionsName,
        PathValues.REPOS_OWNER_REPO_BRANCHES: ReposOwnerRepoBranches,
        PathValues.REPOS_OWNER_REPO_BRANCHES_BRANCH: ReposOwnerRepoBranchesBranch,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS: ReposOwnerRepoCollaborators,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS_COLLABORATOR: ReposOwnerRepoCollaboratorsCollaborator,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS_COLLABORATOR_PERMISSION: ReposOwnerRepoCollaboratorsCollaboratorPermission,
        PathValues.REPOS_OWNER_REPO_COMMITS: ReposOwnerRepoCommits,
        PathValues.REPOS_OWNER_REPO_COMMITS_REF_STATUS: ReposOwnerRepoCommitsRefStatus,
        PathValues.REPOS_OWNER_REPO_COMMITS_REF_STATUSES: ReposOwnerRepoCommitsRefStatuses,
        PathValues.REPOS_OWNER_REPO_CONTENTS: ReposOwnerRepoContents,
        PathValues.REPOS_OWNER_REPO_CONTENTS_FILEPATH: ReposOwnerRepoContentsFilepath,
        PathValues.REPOS_OWNER_REPO_DIFFPATCH: ReposOwnerRepoDiffpatch,
        PathValues.REPOS_OWNER_REPO_EDITORCONFIG_FILEPATH: ReposOwnerRepoEditorconfigFilepath,
        PathValues.REPOS_OWNER_REPO_FORKS: ReposOwnerRepoForks,
        PathValues.REPOS_OWNER_REPO_GIT_BLOBS_SHA: ReposOwnerRepoGitBlobsSha,
        PathValues.REPOS_OWNER_REPO_GIT_COMMITS_SHA: ReposOwnerRepoGitCommitsSha,
        PathValues.REPOS_OWNER_REPO_GIT_COMMITS_SHA_DIFF_TYPE: ReposOwnerRepoGitCommitsShaDiffType,
        PathValues.REPOS_OWNER_REPO_GIT_NOTES_SHA: ReposOwnerRepoGitNotesSha,
        PathValues.REPOS_OWNER_REPO_GIT_REFS: ReposOwnerRepoGitRefs,
        PathValues.REPOS_OWNER_REPO_GIT_REFS_REF: ReposOwnerRepoGitRefsRef,
        PathValues.REPOS_OWNER_REPO_GIT_TAGS_SHA: ReposOwnerRepoGitTagsSha,
        PathValues.REPOS_OWNER_REPO_GIT_TREES_SHA: ReposOwnerRepoGitTreesSha,
        PathValues.REPOS_OWNER_REPO_HOOKS: ReposOwnerRepoHooks,
        PathValues.REPOS_OWNER_REPO_HOOKS_GIT: ReposOwnerRepoHooksGit,
        PathValues.REPOS_OWNER_REPO_HOOKS_GIT_ID: ReposOwnerRepoHooksGitId,
        PathValues.REPOS_OWNER_REPO_HOOKS_ID: ReposOwnerRepoHooksId,
        PathValues.REPOS_OWNER_REPO_HOOKS_ID_TESTS: ReposOwnerRepoHooksIdTests,
        PathValues.REPOS_OWNER_REPO_ISSUE_TEMPLATES: ReposOwnerRepoIssueTemplates,
        PathValues.REPOS_OWNER_REPO_ISSUES: ReposOwnerRepoIssues,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS: ReposOwnerRepoIssuesComments,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID: ReposOwnerRepoIssuesCommentsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_ASSETS: ReposOwnerRepoIssuesCommentsIdAssets,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_ASSETS_ATTACHMENT_ID: ReposOwnerRepoIssuesCommentsIdAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_REACTIONS: ReposOwnerRepoIssuesCommentsIdReactions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX: ReposOwnerRepoIssuesIndex,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_ASSETS: ReposOwnerRepoIssuesIndexAssets,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_ASSETS_ATTACHMENT_ID: ReposOwnerRepoIssuesIndexAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_COMMENTS: ReposOwnerRepoIssuesIndexComments,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_COMMENTS_ID: ReposOwnerRepoIssuesIndexCommentsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_DEADLINE: ReposOwnerRepoIssuesIndexDeadline,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_LABELS: ReposOwnerRepoIssuesIndexLabels,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_LABELS_ID: ReposOwnerRepoIssuesIndexLabelsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_REACTIONS: ReposOwnerRepoIssuesIndexReactions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_DELETE: ReposOwnerRepoIssuesIndexStopwatchDelete,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_START: ReposOwnerRepoIssuesIndexStopwatchStart,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_STOP: ReposOwnerRepoIssuesIndexStopwatchStop,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS: ReposOwnerRepoIssuesIndexSubscriptions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS_CHECK: ReposOwnerRepoIssuesIndexSubscriptionsCheck,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS_USER: ReposOwnerRepoIssuesIndexSubscriptionsUser,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMELINE: ReposOwnerRepoIssuesIndexTimeline,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMES: ReposOwnerRepoIssuesIndexTimes,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMES_ID: ReposOwnerRepoIssuesIndexTimesId,
        PathValues.REPOS_OWNER_REPO_KEYS: ReposOwnerRepoKeys,
        PathValues.REPOS_OWNER_REPO_KEYS_ID: ReposOwnerRepoKeysId,
        PathValues.REPOS_OWNER_REPO_LABELS: ReposOwnerRepoLabels,
        PathValues.REPOS_OWNER_REPO_LABELS_ID: ReposOwnerRepoLabelsId,
        PathValues.REPOS_OWNER_REPO_LANGUAGES: ReposOwnerRepoLanguages,
        PathValues.REPOS_OWNER_REPO_MEDIA_FILEPATH: ReposOwnerRepoMediaFilepath,
        PathValues.REPOS_OWNER_REPO_MILESTONES: ReposOwnerRepoMilestones,
        PathValues.REPOS_OWNER_REPO_MILESTONES_ID: ReposOwnerRepoMilestonesId,
        PathValues.REPOS_OWNER_REPO_MIRRORSYNC: ReposOwnerRepoMirrorSync,
        PathValues.REPOS_OWNER_REPO_NOTIFICATIONS: ReposOwnerRepoNotifications,
        PathValues.REPOS_OWNER_REPO_PULLS: ReposOwnerRepoPulls,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX: ReposOwnerRepoPullsIndex,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_DIFF_TYPE: ReposOwnerRepoPullsIndexDiffType,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_COMMITS: ReposOwnerRepoPullsIndexCommits,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_FILES: ReposOwnerRepoPullsIndexFiles,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_MERGE: ReposOwnerRepoPullsIndexMerge,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REQUESTED_REVIEWERS: ReposOwnerRepoPullsIndexRequestedReviewers,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS: ReposOwnerRepoPullsIndexReviews,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID: ReposOwnerRepoPullsIndexReviewsId,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_COMMENTS: ReposOwnerRepoPullsIndexReviewsIdComments,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_DISMISSALS: ReposOwnerRepoPullsIndexReviewsIdDismissals,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_UNDISMISSALS: ReposOwnerRepoPullsIndexReviewsIdUndismissals,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_UPDATE: ReposOwnerRepoPullsIndexUpdate,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORS: ReposOwnerRepoPushMirrors,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORSSYNC: ReposOwnerRepoPushMirrorsSync,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORS_NAME: ReposOwnerRepoPushMirrorsName,
        PathValues.REPOS_OWNER_REPO_RAW_FILEPATH: ReposOwnerRepoRawFilepath,
        PathValues.REPOS_OWNER_REPO_RELEASES: ReposOwnerRepoReleases,
        PathValues.REPOS_OWNER_REPO_RELEASES_LATEST: ReposOwnerRepoReleasesLatest,
        PathValues.REPOS_OWNER_REPO_RELEASES_TAGS_TAG: ReposOwnerRepoReleasesTagsTag,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID: ReposOwnerRepoReleasesId,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID_ASSETS: ReposOwnerRepoReleasesIdAssets,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID_ASSETS_ATTACHMENT_ID: ReposOwnerRepoReleasesIdAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_REVIEWERS: ReposOwnerRepoReviewers,
        PathValues.REPOS_OWNER_REPO_SIGNINGKEY_GPG: ReposOwnerRepoSigningKeyGpg,
        PathValues.REPOS_OWNER_REPO_STARGAZERS: ReposOwnerRepoStargazers,
        PathValues.REPOS_OWNER_REPO_STATUSES_SHA: ReposOwnerRepoStatusesSha,
        PathValues.REPOS_OWNER_REPO_SUBSCRIBERS: ReposOwnerRepoSubscribers,
        PathValues.REPOS_OWNER_REPO_SUBSCRIPTION: ReposOwnerRepoSubscription,
        PathValues.REPOS_OWNER_REPO_TAGS: ReposOwnerRepoTags,
        PathValues.REPOS_OWNER_REPO_TAGS_TAG: ReposOwnerRepoTagsTag,
        PathValues.REPOS_OWNER_REPO_TEAMS: ReposOwnerRepoTeams,
        PathValues.REPOS_OWNER_REPO_TEAMS_TEAM: ReposOwnerRepoTeamsTeam,
        PathValues.REPOS_OWNER_REPO_TIMES: ReposOwnerRepoTimes,
        PathValues.REPOS_OWNER_REPO_TIMES_USER: ReposOwnerRepoTimesUser,
        PathValues.REPOS_OWNER_REPO_TOPICS: ReposOwnerRepoTopics,
        PathValues.REPOS_OWNER_REPO_TOPICS_TOPIC: ReposOwnerRepoTopicsTopic,
        PathValues.REPOS_OWNER_REPO_TRANSFER: ReposOwnerRepoTransfer,
        PathValues.REPOS_OWNER_REPO_TRANSFER_ACCEPT: ReposOwnerRepoTransferAccept,
        PathValues.REPOS_OWNER_REPO_TRANSFER_REJECT: ReposOwnerRepoTransferReject,
        PathValues.REPOS_OWNER_REPO_WIKI_NEW: ReposOwnerRepoWikiNew,
        PathValues.REPOS_OWNER_REPO_WIKI_PAGE_PAGE_NAME: ReposOwnerRepoWikiPagePageName,
        PathValues.REPOS_OWNER_REPO_WIKI_PAGES: ReposOwnerRepoWikiPages,
        PathValues.REPOS_OWNER_REPO_WIKI_REVISIONS_PAGE_NAME: ReposOwnerRepoWikiRevisionsPageName,
        PathValues.REPOS_TEMPLATE_OWNER_TEMPLATE_REPO_GENERATE: ReposTemplateOwnerTemplateRepoGenerate,
        PathValues.REPOSITORIES_ID: RepositoriesId,
        PathValues.SETTINGS_API: SettingsApi,
        PathValues.SETTINGS_ATTACHMENT: SettingsAttachment,
        PathValues.SETTINGS_REPOSITORY: SettingsRepository,
        PathValues.SETTINGS_UI: SettingsUi,
        PathValues.SIGNINGKEY_GPG: SigningKeyGpg,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.TEAMS_ID_MEMBERS: TeamsIdMembers,
        PathValues.TEAMS_ID_MEMBERS_USERNAME: TeamsIdMembersUsername,
        PathValues.TEAMS_ID_REPOS: TeamsIdRepos,
        PathValues.TEAMS_ID_REPOS_ORG_REPO: TeamsIdReposOrgRepo,
        PathValues.TOPICS_SEARCH: TopicsSearch,
        PathValues.USER: User,
        PathValues.USER_APPLICATIONS_OAUTH2: UserApplicationsOauth2,
        PathValues.USER_APPLICATIONS_OAUTH2_ID: UserApplicationsOauth2Id,
        PathValues.USER_EMAILS: UserEmails,
        PathValues.USER_FOLLOWERS: UserFollowers,
        PathValues.USER_FOLLOWING: UserFollowing,
        PathValues.USER_FOLLOWING_USERNAME: UserFollowingUsername,
        PathValues.USER_GPG_KEY_TOKEN: UserGpgKeyToken,
        PathValues.USER_GPG_KEY_VERIFY: UserGpgKeyVerify,
        PathValues.USER_GPG_KEYS: UserGpgKeys,
        PathValues.USER_GPG_KEYS_ID: UserGpgKeysId,
        PathValues.USER_KEYS: UserKeys,
        PathValues.USER_KEYS_ID: UserKeysId,
        PathValues.USER_ORGS: UserOrgs,
        PathValues.USER_REPOS: UserRepos,
        PathValues.USER_SETTINGS: UserSettings,
        PathValues.USER_STARRED: UserStarred,
        PathValues.USER_STARRED_OWNER_REPO: UserStarredOwnerRepo,
        PathValues.USER_STOPWATCHES: UserStopwatches,
        PathValues.USER_SUBSCRIPTIONS: UserSubscriptions,
        PathValues.USER_TEAMS: UserTeams,
        PathValues.USER_TIMES: UserTimes,
        PathValues.USERS_SEARCH: UsersSearch,
        PathValues.USERS_USERNAME: UsersUsername,
        PathValues.USERS_USERNAME_FOLLOWERS: UsersUsernameFollowers,
        PathValues.USERS_USERNAME_FOLLOWING: UsersUsernameFollowing,
        PathValues.USERS_USERNAME_FOLLOWING_TARGET: UsersUsernameFollowingTarget,
        PathValues.USERS_USERNAME_GPG_KEYS: UsersUsernameGpgKeys,
        PathValues.USERS_USERNAME_HEATMAP: UsersUsernameHeatmap,
        PathValues.USERS_USERNAME_KEYS: UsersUsernameKeys,
        PathValues.USERS_USERNAME_ORGS: UsersUsernameOrgs,
        PathValues.USERS_USERNAME_ORGS_ORG_PERMISSIONS: UsersUsernameOrgsOrgPermissions,
        PathValues.USERS_USERNAME_REPOS: UsersUsernameRepos,
        PathValues.USERS_USERNAME_STARRED: UsersUsernameStarred,
        PathValues.USERS_USERNAME_SUBSCRIPTIONS: UsersUsernameSubscriptions,
        PathValues.USERS_USERNAME_TOKENS: UsersUsernameTokens,
        PathValues.USERS_USERNAME_TOKENS_TOKEN: UsersUsernameTokensToken,
        PathValues.VERSION: Version,
    }
)
