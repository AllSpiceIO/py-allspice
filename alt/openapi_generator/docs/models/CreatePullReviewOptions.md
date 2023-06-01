# allspice_client.model.create_pull_review_options.CreatePullReviewOptions

CreatePullReviewOptions are options to create a pull review

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreatePullReviewOptions are options to create a pull review | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**body** | str,  | str,  |  | [optional] 
**[comments](#comments)** | list, tuple,  | tuple,  |  | [optional] 
**commit_id** | str,  | str,  |  | [optional] 
**event** | str,  | str,  | ReviewStateType review state type | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# comments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreatePullReviewComment**](CreatePullReviewComment.md) | [**CreatePullReviewComment**](CreatePullReviewComment.md) | [**CreatePullReviewComment**](CreatePullReviewComment.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

