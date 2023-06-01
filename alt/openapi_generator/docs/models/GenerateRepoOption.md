# allspice_client.model.generate_repo_option.GenerateRepoOption

GenerateRepoOption options when creating repository using a template

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | GenerateRepoOption options when creating repository using a template | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**owner** | str,  | str,  | The organization or person who will own the new repository | 
**name** | str,  | str,  | Name of the repository to create | 
**avatar** | bool,  | BoolClass,  | include avatar of the template repo | [optional] 
**default_branch** | str,  | str,  | Default branch of the new repository | [optional] 
**description** | str,  | str,  | Description of the repository to create | [optional] 
**git_content** | bool,  | BoolClass,  | include git content of default branch in template repo | [optional] 
**git_hooks** | bool,  | BoolClass,  | include git hooks in template repo | [optional] 
**labels** | bool,  | BoolClass,  | include labels in template repo | [optional] 
**private** | bool,  | BoolClass,  | Whether the repository is private | [optional] 
**topics** | bool,  | BoolClass,  | include topics in template repo | [optional] 
**webhooks** | bool,  | BoolClass,  | include webhooks in template repo | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

