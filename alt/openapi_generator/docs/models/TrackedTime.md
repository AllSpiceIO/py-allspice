# allspice_client.model.tracked_time.TrackedTime

TrackedTime worked time for an issue / pr

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TrackedTime worked time for an issue / pr | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**issue** | [**Issue**](Issue.md) | [**Issue**](Issue.md) |  | [optional] 
**issue_id** | decimal.Decimal, int,  | decimal.Decimal,  | deprecated (only for backwards compatibility) | [optional] value must be a 64 bit integer
**time** | decimal.Decimal, int,  | decimal.Decimal,  | Time in seconds | [optional] value must be a 64 bit integer
**user_id** | decimal.Decimal, int,  | decimal.Decimal,  | deprecated (only for backwards compatibility) | [optional] value must be a 64 bit integer
**user_name** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

