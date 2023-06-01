# allspice_client.model.node_info.NodeInfo

NodeInfo contains standardized way of exposing metadata about a server running one of the distributed social networks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | NodeInfo contains standardized way of exposing metadata about a server running one of the distributed social networks | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**openRegistrations** | bool,  | BoolClass,  |  | [optional] 
**[protocols](#protocols)** | list, tuple,  | tuple,  |  | [optional] 
**services** | [**NodeInfoServices**](NodeInfoServices.md) | [**NodeInfoServices**](NodeInfoServices.md) |  | [optional] 
**software** | [**NodeInfoSoftware**](NodeInfoSoftware.md) | [**NodeInfoSoftware**](NodeInfoSoftware.md) |  | [optional] 
**usage** | [**NodeInfoUsage**](NodeInfoUsage.md) | [**NodeInfoUsage**](NodeInfoUsage.md) |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

