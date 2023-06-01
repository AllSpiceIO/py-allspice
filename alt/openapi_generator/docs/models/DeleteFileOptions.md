# allspice_client.model.delete_file_options.DeleteFileOptions

DeleteFileOptions options for deleting files (used for other File structs below) Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DeleteFileOptions options for deleting files (used for other File structs below) Note: &#x60;author&#x60; and &#x60;committer&#x60; are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sha** | str,  | str,  | sha is the SHA for the file that already exists | 
**author** | [**Identity**](Identity.md) | [**Identity**](Identity.md) |  | [optional] 
**branch** | str,  | str,  | branch (optional) to base this file from. if not given, the default branch is used | [optional] 
**committer** | [**Identity**](Identity.md) | [**Identity**](Identity.md) |  | [optional] 
**dates** | [**CommitDateOptions**](CommitDateOptions.md) | [**CommitDateOptions**](CommitDateOptions.md) |  | [optional] 
**message** | str,  | str,  | message (optional) for the commit of this file. if not supplied, a default message will be used | [optional] 
**new_branch** | str,  | str,  | new_branch (optional) will make a new branch from &#x60;branch&#x60; before creating the file | [optional] 
**signoff** | bool,  | BoolClass,  | Add a Signed-off-by trailer by the committer at the end of the commit log message. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

