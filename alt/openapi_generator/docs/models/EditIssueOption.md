# allspice_client.model.edit_issue_option.EditIssueOption

EditIssueOption options for editing an issue

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EditIssueOption options for editing an issue | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**assignee** | str,  | str,  | deprecated | [optional] 
**[assignees](#assignees)** | list, tuple,  | tuple,  |  | [optional] 
**body** | str,  | str,  |  | [optional] 
**due_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**milestone** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**ref** | str,  | str,  |  | [optional] 
**state** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**unset_due_date** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# assignees

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

