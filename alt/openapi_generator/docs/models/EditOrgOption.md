# allspice_client.model.edit_org_option.EditOrgOption

EditOrgOption options for editing an organization

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EditOrgOption options for editing an organization | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | str,  | str,  |  | [optional] 
**full_name** | str,  | str,  |  | [optional] 
**location** | str,  | str,  |  | [optional] 
**repo_admin_change_team_access** | bool,  | BoolClass,  |  | [optional] 
**visibility** | str,  | str,  | possible values are &#x60;public&#x60;, &#x60;limited&#x60; or &#x60;private&#x60; | [optional] must be one of ["public", "limited", "private", ] 
**website** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

