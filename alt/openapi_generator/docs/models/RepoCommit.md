# allspice_client.model.repo_commit.RepoCommit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**author** | [**CommitUser**](CommitUser.md) | [**CommitUser**](CommitUser.md) |  | [optional] 
**committer** | [**CommitUser**](CommitUser.md) | [**CommitUser**](CommitUser.md) |  | [optional] 
**message** | str,  | str,  |  | [optional] 
**tree** | [**CommitMeta**](CommitMeta.md) | [**CommitMeta**](CommitMeta.md) |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**verification** | [**PayloadCommitVerification**](PayloadCommitVerification.md) | [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

