# allspice_client.model.merge_pull_request_option.MergePullRequestOption

MergePullRequestForm form for merging Pull Request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | MergePullRequestForm form for merging Pull Request | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Do** | str,  | str,  |  | must be one of ["merge", "rebase", "rebase-merge", "squash", "manually-merged", ] 
**MergeCommitID** | str,  | str,  |  | [optional] 
**MergeMessageField** | str,  | str,  |  | [optional] 
**MergeTitleField** | str,  | str,  |  | [optional] 
**delete_branch_after_merge** | bool,  | BoolClass,  |  | [optional] 
**force_merge** | bool,  | BoolClass,  |  | [optional] 
**head_commit_id** | str,  | str,  |  | [optional] 
**merge_when_checks_succeed** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

