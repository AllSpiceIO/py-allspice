# allspice_client.model.payload_commit_verification.PayloadCommitVerification

PayloadCommitVerification represents the GPG verification of a commit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PayloadCommitVerification represents the GPG verification of a commit | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**payload** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**signature** | str,  | str,  |  | [optional] 
**signer** | [**PayloadUser**](PayloadUser.md) | [**PayloadUser**](PayloadUser.md) |  | [optional] 
**verified** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

