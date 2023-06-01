# allspice_client.model.file_response.FileResponse

FileResponse contains information about a repo's file

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | FileResponse contains information about a repo&#x27;s file | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**commit** | [**FileCommitResponse**](FileCommitResponse.md) | [**FileCommitResponse**](FileCommitResponse.md) |  | [optional] 
**content** | [**ContentsResponse**](ContentsResponse.md) | [**ContentsResponse**](ContentsResponse.md) |  | [optional] 
**verification** | [**PayloadCommitVerification**](PayloadCommitVerification.md) | [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

