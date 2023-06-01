# allspice_client.model.create_issue_option.CreateIssueOption

CreateIssueOption options to create one issue

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreateIssueOption options to create one issue | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  |  | 
**assignee** | str,  | str,  | deprecated | [optional] 
**[assignees](#assignees)** | list, tuple,  | tuple,  |  | [optional] 
**body** | str,  | str,  |  | [optional] 
**closed** | bool,  | BoolClass,  |  | [optional] 
**due_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[labels](#labels)** | list, tuple,  | tuple,  | list of label ids | [optional] 
**milestone** | decimal.Decimal, int,  | decimal.Decimal,  | milestone id | [optional] value must be a 64 bit integer
**ref** | str,  | str,  |  | [optional] 
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

# labels

list of label ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | list of label ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

