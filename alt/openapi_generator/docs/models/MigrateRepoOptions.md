# allspice_client.model.migrate_repo_options.MigrateRepoOptions

MigrateRepoOptions options for migrating repository's this is used to interact with api v1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | MigrateRepoOptions options for migrating repository&#x27;s this is used to interact with api v1 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clone_addr** | str,  | str,  |  | 
**repo_name** | str,  | str,  |  | 
**auth_password** | str,  | str,  |  | [optional] 
**auth_token** | str,  | str,  |  | [optional] 
**auth_username** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**issues** | bool,  | BoolClass,  |  | [optional] 
**labels** | bool,  | BoolClass,  |  | [optional] 
**lfs** | bool,  | BoolClass,  |  | [optional] 
**lfs_endpoint** | str,  | str,  |  | [optional] 
**milestones** | bool,  | BoolClass,  |  | [optional] 
**mirror** | bool,  | BoolClass,  |  | [optional] 
**mirror_interval** | str,  | str,  |  | [optional] 
**private** | bool,  | BoolClass,  |  | [optional] 
**pull_requests** | bool,  | BoolClass,  |  | [optional] 
**releases** | bool,  | BoolClass,  |  | [optional] 
**repo_owner** | str,  | str,  | Name of User or Organisation who will own Repo after migration | [optional] 
**service** | str,  | str,  |  | [optional] must be one of ["git", "github", "gitea", "gitlab", ] 
**uid** | decimal.Decimal, int,  | decimal.Decimal,  | deprecated (only for backwards compatibility) | [optional] value must be a 64 bit integer
**wiki** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

