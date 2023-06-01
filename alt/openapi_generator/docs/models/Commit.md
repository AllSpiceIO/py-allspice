# allspice_client.model.commit.Commit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**author** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**commit** | [**RepoCommit**](RepoCommit.md) | [**RepoCommit**](RepoCommit.md) |  | [optional] 
**committer** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**created** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[files](#files)** | list, tuple,  | tuple,  |  | [optional] 
**html_url** | str,  | str,  |  | [optional] 
**[parents](#parents)** | list, tuple,  | tuple,  |  | [optional] 
**sha** | str,  | str,  |  | [optional] 
**stats** | [**CommitStats**](CommitStats.md) | [**CommitStats**](CommitStats.md) |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# files

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommitAffectedFiles**](CommitAffectedFiles.md) | [**CommitAffectedFiles**](CommitAffectedFiles.md) | [**CommitAffectedFiles**](CommitAffectedFiles.md) |  | 

# parents

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommitMeta**](CommitMeta.md) | [**CommitMeta**](CommitMeta.md) | [**CommitMeta**](CommitMeta.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

