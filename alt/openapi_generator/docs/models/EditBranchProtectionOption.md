# allspice_client.model.edit_branch_protection_option.EditBranchProtectionOption

EditBranchProtectionOption options for editing a branch protection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EditBranchProtectionOption options for editing a branch protection | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[approvals_whitelist_teams](#approvals_whitelist_teams)** | list, tuple,  | tuple,  |  | [optional] 
**[approvals_whitelist_username](#approvals_whitelist_username)** | list, tuple,  | tuple,  |  | [optional] 
**block_on_official_review_requests** | bool,  | BoolClass,  |  | [optional] 
**block_on_outdated_branch** | bool,  | BoolClass,  |  | [optional] 
**block_on_rejected_reviews** | bool,  | BoolClass,  |  | [optional] 
**dismiss_stale_approvals** | bool,  | BoolClass,  |  | [optional] 
**enable_approvals_whitelist** | bool,  | BoolClass,  |  | [optional] 
**enable_merge_whitelist** | bool,  | BoolClass,  |  | [optional] 
**enable_push** | bool,  | BoolClass,  |  | [optional] 
**enable_push_whitelist** | bool,  | BoolClass,  |  | [optional] 
**enable_status_check** | bool,  | BoolClass,  |  | [optional] 
**[merge_whitelist_teams](#merge_whitelist_teams)** | list, tuple,  | tuple,  |  | [optional] 
**[merge_whitelist_usernames](#merge_whitelist_usernames)** | list, tuple,  | tuple,  |  | [optional] 
**protected_file_patterns** | str,  | str,  |  | [optional] 
**push_whitelist_deploy_keys** | bool,  | BoolClass,  |  | [optional] 
**[push_whitelist_teams](#push_whitelist_teams)** | list, tuple,  | tuple,  |  | [optional] 
**[push_whitelist_usernames](#push_whitelist_usernames)** | list, tuple,  | tuple,  |  | [optional] 
**require_signed_commits** | bool,  | BoolClass,  |  | [optional] 
**required_approvals** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**[status_check_contexts](#status_check_contexts)** | list, tuple,  | tuple,  |  | [optional] 
**unprotected_file_patterns** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# approvals_whitelist_teams

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# approvals_whitelist_username

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# merge_whitelist_teams

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# merge_whitelist_usernames

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# push_whitelist_teams

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# push_whitelist_usernames

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# status_check_contexts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

