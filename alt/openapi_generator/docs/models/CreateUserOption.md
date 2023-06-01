# allspice_client.model.create_user_option.CreateUserOption

CreateUserOption create user options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreateUserOption create user options | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**password** | str,  | str,  |  | 
**email** | str,  | str,  |  | 
**username** | str,  | str,  |  | 
**created_at** | str, datetime,  | str,  | For explicitly setting the user creation timestamp. Useful when users are migrated from other systems. When omitted, the user&#x27;s creation timestamp will be set to \&quot;now\&quot;. | [optional] value must conform to RFC-3339 date-time
**full_name** | str,  | str,  |  | [optional] 
**login_name** | str,  | str,  |  | [optional] 
**must_change_password** | bool,  | BoolClass,  |  | [optional] 
**restricted** | bool,  | BoolClass,  |  | [optional] 
**send_notify** | bool,  | BoolClass,  |  | [optional] 
**source_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**visibility** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

