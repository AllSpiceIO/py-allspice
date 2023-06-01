# allspice_client.model.external_tracker.ExternalTracker

ExternalTracker represents settings for external tracker

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExternalTracker represents settings for external tracker | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**external_tracker_format** | str,  | str,  | External Issue Tracker URL Format. Use the placeholders {user}, {repo} and {index} for the username, repository name and issue index. | [optional] 
**external_tracker_regexp_pattern** | str,  | str,  | External Issue Tracker issue regular expression | [optional] 
**external_tracker_style** | str,  | str,  | External Issue Tracker Number Format, either &#x60;numeric&#x60;, &#x60;alphanumeric&#x60;, or &#x60;regexp&#x60; | [optional] 
**external_tracker_url** | str,  | str,  | URL of external issue tracker. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

