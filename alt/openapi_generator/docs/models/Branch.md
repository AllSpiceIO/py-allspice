# allspice_client.model.branch.Branch

Branch represents a repository branch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Branch represents a repository branch | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**commit** | [**PayloadCommit**](PayloadCommit.md) | [**PayloadCommit**](PayloadCommit.md) |  | [optional] 
**effective_branch_protection_name** | str,  | str,  |  | [optional] 
**enable_status_check** | bool,  | BoolClass,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**protected** | bool,  | BoolClass,  |  | [optional] 
**required_approvals** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**[status_check_contexts](#status_check_contexts)** | list, tuple,  | tuple,  |  | [optional] 
**user_can_merge** | bool,  | BoolClass,  |  | [optional] 
**user_can_push** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# status_check_contexts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

