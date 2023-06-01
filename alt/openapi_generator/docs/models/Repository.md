# allspice_client.model.repository.Repository

Repository represents a repository

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Repository represents a repository | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**allow_merge_commits** | bool,  | BoolClass,  |  | [optional] 
**allow_rebase** | bool,  | BoolClass,  |  | [optional] 
**allow_rebase_explicit** | bool,  | BoolClass,  |  | [optional] 
**allow_rebase_update** | bool,  | BoolClass,  |  | [optional] 
**allow_squash_merge** | bool,  | BoolClass,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**avatar_url** | str,  | str,  |  | [optional] 
**clone_url** | str,  | str,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**default_allow_maintainer_edit** | bool,  | BoolClass,  |  | [optional] 
**default_branch** | str,  | str,  |  | [optional] 
**default_delete_branch_after_merge** | bool,  | BoolClass,  |  | [optional] 
**default_merge_style** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**empty** | bool,  | BoolClass,  |  | [optional] 
**external_tracker** | [**ExternalTracker**](ExternalTracker.md) | [**ExternalTracker**](ExternalTracker.md) |  | [optional] 
**external_wiki** | [**ExternalWiki**](ExternalWiki.md) | [**ExternalWiki**](ExternalWiki.md) |  | [optional] 
**fork** | bool,  | BoolClass,  |  | [optional] 
**forks_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**full_name** | str,  | str,  |  | [optional] 
**has_issues** | bool,  | BoolClass,  |  | [optional] 
**has_projects** | bool,  | BoolClass,  |  | [optional] 
**has_pull_requests** | bool,  | BoolClass,  |  | [optional] 
**has_wiki** | bool,  | BoolClass,  |  | [optional] 
**html_url** | str,  | str,  |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**ignore_whitespace_conflicts** | bool,  | BoolClass,  |  | [optional] 
**internal** | bool,  | BoolClass,  |  | [optional] 
**internal_tracker** | [**InternalTracker**](InternalTracker.md) | [**InternalTracker**](InternalTracker.md) |  | [optional] 
**language** | str,  | str,  |  | [optional] 
**languages_url** | str,  | str,  |  | [optional] 
**link** | str,  | str,  |  | [optional] 
**mirror** | bool,  | BoolClass,  |  | [optional] 
**mirror_interval** | str,  | str,  |  | [optional] 
**mirror_updated** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**name** | str,  | str,  |  | [optional] 
**open_issues_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**open_pr_counter** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**original_url** | str,  | str,  |  | [optional] 
**owner** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**parent** | [**Repository**](Repository.md) | [**Repository**](Repository.md) |  | [optional] 
**permissions** | [**Permission**](Permission.md) | [**Permission**](Permission.md) |  | [optional] 
**private** | bool,  | BoolClass,  |  | [optional] 
**release_counter** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**repo_transfer** | [**RepoTransfer**](RepoTransfer.md) | [**RepoTransfer**](RepoTransfer.md) |  | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**ssh_url** | str,  | str,  |  | [optional] 
**stars_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**template** | bool,  | BoolClass,  |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**watchers_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**website** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

