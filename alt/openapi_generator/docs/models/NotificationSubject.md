# allspice_client.model.notification_subject.NotificationSubject

NotificationSubject contains the notification subject (Issue/Pull/Commit)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | NotificationSubject contains the notification subject (Issue/Pull/Commit) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**html_url** | str,  | str,  |  | [optional] 
**latest_comment_html_url** | str,  | str,  |  | [optional] 
**latest_comment_url** | str,  | str,  |  | [optional] 
**state** | str,  | str,  | StateType issue state type | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  | NotifySubjectType represent type of notification subject | [optional] 
**url** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

