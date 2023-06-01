<a id="__pageTop"></a>
# allspice_client.apis.tags.settings_api.SettingsApi

All URIs are relative to *https://hub.allspice.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_general_api_settings**](#get_general_api_settings) | **get** /settings/api | Get instance&#x27;s global settings for api
[**get_general_attachment_settings**](#get_general_attachment_settings) | **get** /settings/attachment | Get instance&#x27;s global settings for Attachment
[**get_general_repository_settings**](#get_general_repository_settings) | **get** /settings/repository | Get instance&#x27;s global settings for repositories
[**get_general_ui_settings**](#get_general_ui_settings) | **get** /settings/ui | Get instance&#x27;s global settings for ui

# **get_general_api_settings**
<a id="get_general_api_settings"></a>
> GeneralAPISettings get_general_api_settings()

Get instance's global settings for api

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import allspice_client
from allspice_client.apis.tags import settings_api
from allspice_client.model.general_api_settings import GeneralAPISettings
from pprint import pprint
# Defining the host is optional and defaults to https://hub.allspice.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = allspice_client.Configuration(
    host = "https://hub.allspice.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = allspice_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'
# Enter a context with an instance of the API client
with allspice_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get instance's global settings for api
        api_response = api_instance.get_general_api_settings()
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling SettingsApi->get_general_api_settings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_general_api_settings.ApiResponseFor200) | GeneralAPISettings

#### get_general_api_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GeneralAPISettings**](../../models/GeneralAPISettings.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**GeneralAPISettings**](../../models/GeneralAPISettings.md) |  | 


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_general_attachment_settings**
<a id="get_general_attachment_settings"></a>
> GeneralAttachmentSettings get_general_attachment_settings()

Get instance's global settings for Attachment

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import allspice_client
from allspice_client.apis.tags import settings_api
from allspice_client.model.general_attachment_settings import GeneralAttachmentSettings
from pprint import pprint
# Defining the host is optional and defaults to https://hub.allspice.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = allspice_client.Configuration(
    host = "https://hub.allspice.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = allspice_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'
# Enter a context with an instance of the API client
with allspice_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get instance's global settings for Attachment
        api_response = api_instance.get_general_attachment_settings()
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling SettingsApi->get_general_attachment_settings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_general_attachment_settings.ApiResponseFor200) | GeneralAttachmentSettings

#### get_general_attachment_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GeneralAttachmentSettings**](../../models/GeneralAttachmentSettings.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**GeneralAttachmentSettings**](../../models/GeneralAttachmentSettings.md) |  | 


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_general_repository_settings**
<a id="get_general_repository_settings"></a>
> GeneralRepoSettings get_general_repository_settings()

Get instance's global settings for repositories

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import allspice_client
from allspice_client.apis.tags import settings_api
from allspice_client.model.general_repo_settings import GeneralRepoSettings
from pprint import pprint
# Defining the host is optional and defaults to https://hub.allspice.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = allspice_client.Configuration(
    host = "https://hub.allspice.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = allspice_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'
# Enter a context with an instance of the API client
with allspice_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get instance's global settings for repositories
        api_response = api_instance.get_general_repository_settings()
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling SettingsApi->get_general_repository_settings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_general_repository_settings.ApiResponseFor200) | GeneralRepoSettings

#### get_general_repository_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GeneralRepoSettings**](../../models/GeneralRepoSettings.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**GeneralRepoSettings**](../../models/GeneralRepoSettings.md) |  | 


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_general_ui_settings**
<a id="get_general_ui_settings"></a>
> GeneralUISettings get_general_ui_settings()

Get instance's global settings for ui

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import allspice_client
from allspice_client.apis.tags import settings_api
from allspice_client.model.general_ui_settings import GeneralUISettings
from pprint import pprint
# Defining the host is optional and defaults to https://hub.allspice.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = allspice_client.Configuration(
    host = "https://hub.allspice.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = allspice_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'
# Enter a context with an instance of the API client
with allspice_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get instance's global settings for ui
        api_response = api_instance.get_general_ui_settings()
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling SettingsApi->get_general_ui_settings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_general_ui_settings.ApiResponseFor200) | GeneralUISettings

#### get_general_ui_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GeneralUISettings**](../../models/GeneralUISettings.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**GeneralUISettings**](../../models/GeneralUISettings.md) |  | 


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

