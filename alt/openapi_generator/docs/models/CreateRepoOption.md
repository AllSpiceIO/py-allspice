# allspice_client.model.create_repo_option.CreateRepoOption

CreateRepoOption options when creating repository

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreateRepoOption options when creating repository | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Name of the repository to create | 
**auto_init** | bool,  | BoolClass,  | Whether the repository should be auto-initialized? | [optional] 
**create_develop_branch** | bool,  | BoolClass,  | Whether to initialize the repository with a secondary develop branch | [optional] 
**default_branch** | str,  | str,  | DefaultBranch of the repository (used when initializes and in template) | [optional] 
**description** | str,  | str,  | Description of the repository to create | [optional] 
**gitignores** | str,  | str,  | Gitignores to use | [optional] 
**issue_labels** | str,  | str,  | Label-Set to use | [optional] 
**license** | str,  | str,  | License to use | [optional] 
**private** | bool,  | BoolClass,  | Whether the repository is private | [optional] 
**readme** | str,  | str,  | Readme of the repository to create | [optional] 
**template** | bool,  | BoolClass,  | Whether the repository is template | [optional] 
**trust_model** | str,  | str,  | TrustModel of the repository | [optional] must be one of ["default", "collaborator", "committer", "collaboratorcommitter", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

