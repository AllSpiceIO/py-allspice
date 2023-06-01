# allspice_client.model.pull_request.PullRequest

PullRequest represents a pull request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PullRequest represents a pull request | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**allow_maintainer_edit** | bool,  | BoolClass,  |  | [optional] 
**assignee** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**[assignees](#assignees)** | list, tuple,  | tuple,  |  | [optional] 
**base** | [**PRBranchInfo**](PRBranchInfo.md) | [**PRBranchInfo**](PRBranchInfo.md) |  | [optional] 
**body** | str,  | str,  |  | [optional] 
**closed_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**comments** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**diff_url** | str,  | str,  |  | [optional] 
**due_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**head** | [**PRBranchInfo**](PRBranchInfo.md) | [**PRBranchInfo**](PRBranchInfo.md) |  | [optional] 
**html_url** | str,  | str,  |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**is_locked** | bool,  | BoolClass,  |  | [optional] 
**[labels](#labels)** | list, tuple,  | tuple,  |  | [optional] 
**merge_base** | str,  | str,  |  | [optional] 
**merge_commit_sha** | str,  | str,  |  | [optional] 
**mergeable** | bool,  | BoolClass,  |  | [optional] 
**merged** | bool,  | BoolClass,  |  | [optional] 
**merged_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**merged_by** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) | [**Milestone**](Milestone.md) |  | [optional] 
**number** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**patch_url** | str,  | str,  |  | [optional] 
**state** | str,  | str,  | StateType issue state type | [optional] 
**title** | str,  | str,  |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**url** | str,  | str,  |  | [optional] 
**user** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# assignees

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**User**](User.md) | [**User**](User.md) | [**User**](User.md) |  | 

# labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Label**](Label.md) | [**Label**](Label.md) | [**Label**](Label.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

