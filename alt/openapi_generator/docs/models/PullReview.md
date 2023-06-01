# allspice_client.model.pull_review.PullReview

PullReview represents a pull request review

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PullReview represents a pull request review | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**body** | str,  | str,  |  | [optional] 
**comments_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**commit_id** | str,  | str,  |  | [optional] 
**dismissed** | bool,  | BoolClass,  |  | [optional] 
**html_url** | str,  | str,  |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**official** | bool,  | BoolClass,  |  | [optional] 
**pull_request_url** | str,  | str,  |  | [optional] 
**stale** | bool,  | BoolClass,  |  | [optional] 
**state** | str,  | str,  | ReviewStateType review state type | [optional] 
**submitted_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**team** | [**Team**](Team.md) | [**Team**](Team.md) |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**user** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

