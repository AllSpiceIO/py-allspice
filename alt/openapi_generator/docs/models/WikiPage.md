# allspice_client.model.wiki_page.WikiPage

WikiPage a wiki page

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | WikiPage a wiki page | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**commit_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**content_base64** | str,  | str,  | Page content, base64 encoded | [optional] 
**footer** | str,  | str,  |  | [optional] 
**html_url** | str,  | str,  |  | [optional] 
**last_commit** | [**WikiCommit**](WikiCommit.md) | [**WikiCommit**](WikiCommit.md) |  | [optional] 
**sidebar** | str,  | str,  |  | [optional] 
**sub_url** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

