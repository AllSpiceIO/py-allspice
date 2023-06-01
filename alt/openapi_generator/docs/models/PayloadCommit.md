# allspice_client.model.payload_commit.PayloadCommit

PayloadCommit represents a commit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PayloadCommit represents a commit | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[added](#added)** | list, tuple,  | tuple,  |  | [optional] 
**author** | [**PayloadUser**](PayloadUser.md) | [**PayloadUser**](PayloadUser.md) |  | [optional] 
**committer** | [**PayloadUser**](PayloadUser.md) | [**PayloadUser**](PayloadUser.md) |  | [optional] 
**id** | str,  | str,  | sha1 hash of the commit | [optional] 
**message** | str,  | str,  |  | [optional] 
**[modified](#modified)** | list, tuple,  | tuple,  |  | [optional] 
**[removed](#removed)** | list, tuple,  | tuple,  |  | [optional] 
**timestamp** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**url** | str,  | str,  |  | [optional] 
**verification** | [**PayloadCommitVerification**](PayloadCommitVerification.md) | [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# added

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# modified

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# removed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

