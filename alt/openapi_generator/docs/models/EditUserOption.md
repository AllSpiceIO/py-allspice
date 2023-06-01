# allspice_client.model.edit_user_option.EditUserOption

EditUserOption edit user options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EditUserOption edit user options | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**login_name** | str,  | str,  |  | 
**source_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**active** | bool,  | BoolClass,  |  | [optional] 
**admin** | bool,  | BoolClass,  |  | [optional] 
**allow_create_organization** | bool,  | BoolClass,  |  | [optional] 
**allow_git_hook** | bool,  | BoolClass,  |  | [optional] 
**allow_import_local** | bool,  | BoolClass,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**full_name** | str,  | str,  |  | [optional] 
**location** | str,  | str,  |  | [optional] 
**max_repo_creation** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**must_change_password** | bool,  | BoolClass,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**prohibit_login** | bool,  | BoolClass,  |  | [optional] 
**restricted** | bool,  | BoolClass,  |  | [optional] 
**visibility** | str,  | str,  |  | [optional] 
**website** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

