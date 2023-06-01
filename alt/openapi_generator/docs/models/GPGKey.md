# allspice_client.model.gpg_key.GPGKey

GPGKey a user GPG key to sign commit and tag in repository

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | GPGKey a user GPG key to sign commit and tag in repository | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**can_certify** | bool,  | BoolClass,  |  | [optional] 
**can_encrypt_comms** | bool,  | BoolClass,  |  | [optional] 
**can_encrypt_storage** | bool,  | BoolClass,  |  | [optional] 
**can_sign** | bool,  | BoolClass,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[emails](#emails)** | list, tuple,  | tuple,  |  | [optional] 
**expires_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**key_id** | str,  | str,  |  | [optional] 
**primary_key_id** | str,  | str,  |  | [optional] 
**public_key** | str,  | str,  |  | [optional] 
**[subkeys](#subkeys)** | list, tuple,  | tuple,  |  | [optional] 
**verified** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# emails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GPGKeyEmail**](GPGKeyEmail.md) | [**GPGKeyEmail**](GPGKeyEmail.md) | [**GPGKeyEmail**](GPGKeyEmail.md) |  | 

# subkeys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GPGKey**](GPGKey.md) | [**GPGKey**](GPGKey.md) | [**GPGKey**](GPGKey.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

