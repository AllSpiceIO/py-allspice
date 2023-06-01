# allspice_client.model.issue_template.IssueTemplate

IssueTemplate represents an issue template for a repository

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | IssueTemplate represents an issue template for a repository | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**about** | str,  | str,  |  | [optional] 
**[body](#body)** | list, tuple,  | tuple,  |  | [optional] 
**content** | str,  | str,  |  | [optional] 
**file_name** | str,  | str,  |  | [optional] 
**labels** | [**IssueTemplateLabels**](IssueTemplateLabels.md) | [**IssueTemplateLabels**](IssueTemplateLabels.md) |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**ref** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# body

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IssueFormField**](IssueFormField.md) | [**IssueFormField**](IssueFormField.md) | [**IssueFormField**](IssueFormField.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

