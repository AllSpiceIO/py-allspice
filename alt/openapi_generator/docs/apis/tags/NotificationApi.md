<a id="__pageTop"></a>
# allspice_client.apis.tags.notification_api.NotificationApi

All URIs are relative to *https://hub.allspice.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notify_get_list**](#notify_get_list) | **get** /notifications | List users&#x27;s notification threads
[**notify_get_repo_list**](#notify_get_repo_list) | **get** /repos/{owner}/{repo}/notifications | List users&#x27;s notification threads on a specific repo
[**notify_get_thread**](#notify_get_thread) | **get** /notifications/threads/{id} | Get notification thread by ID
[**notify_new_available**](#notify_new_available) | **get** /notifications/new | Check if unread notifications exist
[**notify_read_list**](#notify_read_list) | **put** /notifications | Mark notification threads as read, pinned or unread
[**notify_read_repo_list**](#notify_read_repo_list) | **put** /repos/{owner}/{repo}/notifications | Mark notification threads as read, pinned or unread on a specific repo
[**notify_read_thread**](#notify_read_thread) | **patch** /notifications/threads/{id} | Mark notification thread as read by ID

# **notify_get_list**
<a id="notify_get_list"></a>
> [NotificationThread] notify_get_list()

List users's notification threads

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
from allspice_client.apis.tags import notification_api
from allspice_client.model.notification_thread import NotificationThread
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
    api_instance = notification_api.NotificationApi(api_client)

    # example passing only optional values
    query_params = {
        'all': True,
        'status-types': [
        "status-types_example"
    ],
        'subject-type': [
        "issue"
    ],
        'since': "1970-01-01T00:00:00.00Z",
        'before': "1970-01-01T00:00:00.00Z",
        'page': 1,
        'limit': 1,
    }
    try:
        # List users's notification threads
        api_response = api_instance.notify_get_list(
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling NotificationApi->notify_get_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
all | AllSchema | | optional
status-types | StatusTypesSchema | | optional
subject-type | SubjectTypeSchema | | optional
since | SinceSchema | | optional
before | BeforeSchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional


# AllSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StatusTypesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# SubjectTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["issue", "pull", "commit", "repository", ] 

# SinceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeforeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#notify_get_list.ApiResponseFor200) | NotificationThreadList

#### notify_get_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **notify_get_repo_list**
<a id="notify_get_repo_list"></a>
> [NotificationThread] notify_get_repo_list(ownerrepo)

List users's notification threads on a specific repo

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
from allspice_client.apis.tags import notification_api
from allspice_client.model.notification_thread import NotificationThread
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
    api_instance = notification_api.NotificationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
    }
    try:
        # List users's notification threads on a specific repo
        api_response = api_instance.notify_get_repo_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling NotificationApi->notify_get_repo_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
        'all': True,
        'status-types': [
        "status-types_example"
    ],
        'subject-type': [
        "issue"
    ],
        'since': "1970-01-01T00:00:00.00Z",
        'before': "1970-01-01T00:00:00.00Z",
        'page': 1,
        'limit': 1,
    }
    try:
        # List users's notification threads on a specific repo
        api_response = api_instance.notify_get_repo_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling NotificationApi->notify_get_repo_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
all | AllSchema | | optional
status-types | StatusTypesSchema | | optional
subject-type | SubjectTypeSchema | | optional
since | SinceSchema | | optional
before | BeforeSchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional


# AllSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StatusTypesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# SubjectTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["issue", "pull", "commit", "repository", ] 

# SinceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeforeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 

# OwnerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RepoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#notify_get_repo_list.ApiResponseFor200) | NotificationThreadList

#### notify_get_repo_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **notify_get_thread**
<a id="notify_get_thread"></a>
> NotificationThread notify_get_thread(id)

Get notification thread by ID

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
from allspice_client.apis.tags import notification_api
from allspice_client.model.notification_thread import NotificationThread
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
    api_instance = notification_api.NotificationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get notification thread by ID
        api_response = api_instance.notify_get_thread(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling NotificationApi->notify_get_thread: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#notify_get_thread.ApiResponseFor200) | NotificationThread
403 | [ApiResponseFor403](#notify_get_thread.ApiResponseFor403) | APIForbiddenError is a forbidden error response
404 | [ApiResponseFor404](#notify_get_thread.ApiResponseFor404) | APINotFound is a not found empty response

#### notify_get_thread.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationThread**](../../models/NotificationThread.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationThread**](../../models/NotificationThread.md) |  | 


#### notify_get_thread.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor403 |  |
#### ResponseHeadersFor403

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
message | MessageSchema | | optional
url | UrlSchema | | optional

# MessageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### notify_get_thread.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **notify_new_available**
<a id="notify_new_available"></a>
> NotificationCount notify_new_available()

Check if unread notifications exist

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
from allspice_client.apis.tags import notification_api
from allspice_client.model.notification_count import NotificationCount
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
    api_instance = notification_api.NotificationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check if unread notifications exist
        api_response = api_instance.notify_new_available()
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling NotificationApi->notify_new_available: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#notify_new_available.ApiResponseFor200) | Number of unread notifications

#### notify_new_available.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationCount**](../../models/NotificationCount.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationCount**](../../models/NotificationCount.md) |  | 


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **notify_read_list**
<a id="notify_read_list"></a>
> [NotificationThread] notify_read_list()

Mark notification threads as read, pinned or unread

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
from allspice_client.apis.tags import notification_api
from allspice_client.model.notification_thread import NotificationThread
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
    api_instance = notification_api.NotificationApi(api_client)

    # example passing only optional values
    query_params = {
        'last_read_at': "1970-01-01T00:00:00.00Z",
        'all': "all_example",
        'status-types': [
        "status-types_example"
    ],
        'to-status': "to-status_example",
    }
    try:
        # Mark notification threads as read, pinned or unread
        api_response = api_instance.notify_read_list(
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling NotificationApi->notify_read_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
last_read_at | LastReadAtSchema | | optional
all | AllSchema | | optional
status-types | StatusTypesSchema | | optional
to-status | ToStatusSchema | | optional


# LastReadAtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# AllSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusTypesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ToStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
205 | [ApiResponseFor205](#notify_read_list.ApiResponseFor205) | NotificationThreadList

#### notify_read_list.ApiResponseFor205
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor205ResponseBodyApplicationJson, SchemaFor205ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor205ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) |  | 

# SchemaFor205ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **notify_read_repo_list**
<a id="notify_read_repo_list"></a>
> [NotificationThread] notify_read_repo_list(ownerrepo)

Mark notification threads as read, pinned or unread on a specific repo

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
from allspice_client.apis.tags import notification_api
from allspice_client.model.notification_thread import NotificationThread
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
    api_instance = notification_api.NotificationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
    }
    try:
        # Mark notification threads as read, pinned or unread on a specific repo
        api_response = api_instance.notify_read_repo_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling NotificationApi->notify_read_repo_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
        'all': "all_example",
        'status-types': [
        "status-types_example"
    ],
        'to-status': "to-status_example",
        'last_read_at': "1970-01-01T00:00:00.00Z",
    }
    try:
        # Mark notification threads as read, pinned or unread on a specific repo
        api_response = api_instance.notify_read_repo_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling NotificationApi->notify_read_repo_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
all | AllSchema | | optional
status-types | StatusTypesSchema | | optional
to-status | ToStatusSchema | | optional
last_read_at | LastReadAtSchema | | optional


# AllSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusTypesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ToStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastReadAtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 

# OwnerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RepoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
205 | [ApiResponseFor205](#notify_read_repo_list.ApiResponseFor205) | NotificationThreadList

#### notify_read_repo_list.ApiResponseFor205
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor205ResponseBodyApplicationJson, SchemaFor205ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor205ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) |  | 

# SchemaFor205ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) | [**NotificationThread**]({{complexTypePrefix}}NotificationThread.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **notify_read_thread**
<a id="notify_read_thread"></a>
> NotificationThread notify_read_thread(id)

Mark notification thread as read by ID

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
from allspice_client.apis.tags import notification_api
from allspice_client.model.notification_thread import NotificationThread
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
    api_instance = notification_api.NotificationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    try:
        # Mark notification thread as read by ID
        api_response = api_instance.notify_read_thread(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling NotificationApi->notify_read_thread: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'to-status': "read",
    }
    try:
        # Mark notification thread as read by ID
        api_response = api_instance.notify_read_thread(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling NotificationApi->notify_read_thread: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
to-status | ToStatusSchema | | optional


# ToStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "read"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
205 | [ApiResponseFor205](#notify_read_thread.ApiResponseFor205) | NotificationThread
403 | [ApiResponseFor403](#notify_read_thread.ApiResponseFor403) | APIForbiddenError is a forbidden error response
404 | [ApiResponseFor404](#notify_read_thread.ApiResponseFor404) | APINotFound is a not found empty response

#### notify_read_thread.ApiResponseFor205
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor205ResponseBodyApplicationJson, SchemaFor205ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor205ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationThread**](../../models/NotificationThread.md) |  | 


# SchemaFor205ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationThread**](../../models/NotificationThread.md) |  | 


#### notify_read_thread.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor403 |  |
#### ResponseHeadersFor403

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
message | MessageSchema | | optional
url | UrlSchema | | optional

# MessageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### notify_read_thread.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

