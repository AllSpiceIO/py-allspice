# allspice_client.model.user.User

User represents a user

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | User represents a user | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**active** | bool,  | BoolClass,  | Is user active | [optional] 
**avatar_url** | str,  | str,  | URL to the user&#x27;s avatar | [optional] 
**created** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**description** | str,  | str,  | the user&#x27;s description | [optional] 
**email** | str,  | str,  |  | [optional] 
**followers_count** | decimal.Decimal, int,  | decimal.Decimal,  | user counts | [optional] value must be a 64 bit integer
**following_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**full_name** | str,  | str,  | the user&#x27;s full name | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | the user&#x27;s id | [optional] value must be a 64 bit integer
**is_admin** | bool,  | BoolClass,  | Is the user an administrator | [optional] 
**language** | str,  | str,  | User locale | [optional] 
**last_login** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**location** | str,  | str,  | the user&#x27;s location | [optional] 
**login** | str,  | str,  | the user&#x27;s username | [optional] 
**login_name** | str,  | str,  | the user&#x27;s authentication sign-in name. | [optional] if omitted the server will use the default value of "empty"
**prohibit_login** | bool,  | BoolClass,  | Is user login prohibited | [optional] 
**restricted** | bool,  | BoolClass,  | Is user restricted | [optional] 
**starred_repos_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**visibility** | str,  | str,  | User visibility level option: public, limited, private | [optional] 
**website** | str,  | str,  | the user&#x27;s website | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

