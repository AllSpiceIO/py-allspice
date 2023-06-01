# allspice_client.model.edit_repo_option.EditRepoOption

EditRepoOption options when editing a repository's properties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EditRepoOption options when editing a repository&#x27;s properties | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**allow_manual_merge** | bool,  | BoolClass,  | either &#x60;true&#x60; to allow mark pr as merged manually, or &#x60;false&#x60; to prevent it. | [optional] 
**allow_merge_commits** | bool,  | BoolClass,  | either &#x60;true&#x60; to allow merging pull requests with a merge commit, or &#x60;false&#x60; to prevent merging pull requests with merge commits. | [optional] 
**allow_rebase** | bool,  | BoolClass,  | either &#x60;true&#x60; to allow rebase-merging pull requests, or &#x60;false&#x60; to prevent rebase-merging. | [optional] 
**allow_rebase_explicit** | bool,  | BoolClass,  | either &#x60;true&#x60; to allow rebase with explicit merge commits (--no-ff), or &#x60;false&#x60; to prevent rebase with explicit merge commits. | [optional] 
**allow_rebase_update** | bool,  | BoolClass,  | either &#x60;true&#x60; to allow updating pull request branch by rebase, or &#x60;false&#x60; to prevent it. | [optional] 
**allow_squash_merge** | bool,  | BoolClass,  | either &#x60;true&#x60; to allow squash-merging pull requests, or &#x60;false&#x60; to prevent squash-merging. | [optional] 
**archived** | bool,  | BoolClass,  | set to &#x60;true&#x60; to archive this repository. | [optional] 
**autodetect_manual_merge** | bool,  | BoolClass,  | either &#x60;true&#x60; to enable AutodetectManualMerge, or &#x60;false&#x60; to prevent it. Note: In some special cases, misjudgments can occur. | [optional] 
**default_allow_maintainer_edit** | bool,  | BoolClass,  | set to &#x60;true&#x60; to allow edits from maintainers by default | [optional] 
**default_branch** | str,  | str,  | sets the default branch for this repository. | [optional] 
**default_delete_branch_after_merge** | bool,  | BoolClass,  | set to &#x60;true&#x60; to delete pr branch after merge by default | [optional] 
**default_merge_style** | str,  | str,  | set to a merge style to be used by this repository: \&quot;merge\&quot;, \&quot;rebase\&quot;, \&quot;rebase-merge\&quot;, or \&quot;squash\&quot;. | [optional] 
**description** | str,  | str,  | a short description of the repository. | [optional] 
**enable_prune** | bool,  | BoolClass,  | enable prune - remove obsolete remote-tracking references | [optional] 
**external_tracker** | [**ExternalTracker**](ExternalTracker.md) | [**ExternalTracker**](ExternalTracker.md) |  | [optional] 
**external_wiki** | [**ExternalWiki**](ExternalWiki.md) | [**ExternalWiki**](ExternalWiki.md) |  | [optional] 
**has_issues** | bool,  | BoolClass,  | either &#x60;true&#x60; to enable issues for this repository or &#x60;false&#x60; to disable them. | [optional] 
**has_projects** | bool,  | BoolClass,  | either &#x60;true&#x60; to enable project unit, or &#x60;false&#x60; to disable them. | [optional] 
**has_pull_requests** | bool,  | BoolClass,  | either &#x60;true&#x60; to allow pull requests, or &#x60;false&#x60; to prevent pull request. | [optional] 
**has_wiki** | bool,  | BoolClass,  | either &#x60;true&#x60; to enable the wiki for this repository or &#x60;false&#x60; to disable it. | [optional] 
**ignore_whitespace_conflicts** | bool,  | BoolClass,  | either &#x60;true&#x60; to ignore whitespace for conflicts, or &#x60;false&#x60; to not ignore whitespace. | [optional] 
**internal_tracker** | [**InternalTracker**](InternalTracker.md) | [**InternalTracker**](InternalTracker.md) |  | [optional] 
**mirror_interval** | str,  | str,  | set to a string like &#x60;8h30m0s&#x60; to set the mirror interval time | [optional] 
**name** | str,  | str,  | name of the repository | [optional] 
**private** | bool,  | BoolClass,  | either &#x60;true&#x60; to make the repository private or &#x60;false&#x60; to make it public. Note: you will get a 422 error if the organization restricts changing repository visibility to organization owners and a non-owner tries to change the value of private. | [optional] 
**template** | bool,  | BoolClass,  | either &#x60;true&#x60; to make this repository a template or &#x60;false&#x60; to make it a normal repository | [optional] 
**website** | str,  | str,  | a URL with more information about the repository. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

