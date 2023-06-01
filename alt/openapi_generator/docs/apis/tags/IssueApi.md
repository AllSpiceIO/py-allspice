<a id="__pageTop"></a>
# allspice_client.apis.tags.issue_api.IssueApi

All URIs are relative to *https://hub.allspice.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_add_label**](#issue_add_label) | **post** /repos/{owner}/{repo}/issues/{index}/labels | Add a label to an issue
[**issue_add_subscription**](#issue_add_subscription) | **put** /repos/{owner}/{repo}/issues/{index}/subscriptions/{user} | Subscribe user to issue
[**issue_add_time**](#issue_add_time) | **post** /repos/{owner}/{repo}/issues/{index}/times | Add tracked time to a issue
[**issue_check_subscription**](#issue_check_subscription) | **get** /repos/{owner}/{repo}/issues/{index}/subscriptions/check | Check if user is subscribed to an issue
[**issue_clear_labels**](#issue_clear_labels) | **delete** /repos/{owner}/{repo}/issues/{index}/labels | Remove all labels from an issue
[**issue_create_comment**](#issue_create_comment) | **post** /repos/{owner}/{repo}/issues/{index}/comments | Add a comment to an issue
[**issue_create_issue**](#issue_create_issue) | **post** /repos/{owner}/{repo}/issues | Create an issue. If using deadline only the date will be taken into account, and time of day ignored.
[**issue_create_issue_attachment**](#issue_create_issue_attachment) | **post** /repos/{owner}/{repo}/issues/{index}/assets | Create an issue attachment
[**issue_create_issue_comment_attachment**](#issue_create_issue_comment_attachment) | **post** /repos/{owner}/{repo}/issues/comments/{id}/assets | Create a comment attachment
[**issue_create_label**](#issue_create_label) | **post** /repos/{owner}/{repo}/labels | Create a label
[**issue_create_milestone**](#issue_create_milestone) | **post** /repos/{owner}/{repo}/milestones | Create a milestone
[**issue_delete**](#issue_delete) | **delete** /repos/{owner}/{repo}/issues/{index} | Delete an issue
[**issue_delete_comment**](#issue_delete_comment) | **delete** /repos/{owner}/{repo}/issues/comments/{id} | Delete a comment
[**issue_delete_comment_deprecated**](#issue_delete_comment_deprecated) | **delete** /repos/{owner}/{repo}/issues/{index}/comments/{id} | Delete a comment
[**issue_delete_comment_reaction**](#issue_delete_comment_reaction) | **delete** /repos/{owner}/{repo}/issues/comments/{id}/reactions | Remove a reaction from a comment of an issue
[**issue_delete_issue_attachment**](#issue_delete_issue_attachment) | **delete** /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | Delete an issue attachment
[**issue_delete_issue_comment_attachment**](#issue_delete_issue_comment_attachment) | **delete** /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id} | Delete a comment attachment
[**issue_delete_issue_reaction**](#issue_delete_issue_reaction) | **delete** /repos/{owner}/{repo}/issues/{index}/reactions | Remove a reaction from an issue
[**issue_delete_label**](#issue_delete_label) | **delete** /repos/{owner}/{repo}/labels/{id} | Delete a label
[**issue_delete_milestone**](#issue_delete_milestone) | **delete** /repos/{owner}/{repo}/milestones/{id} | Delete a milestone
[**issue_delete_stop_watch**](#issue_delete_stop_watch) | **delete** /repos/{owner}/{repo}/issues/{index}/stopwatch/delete | Delete an issue&#x27;s existing stopwatch.
[**issue_delete_subscription**](#issue_delete_subscription) | **delete** /repos/{owner}/{repo}/issues/{index}/subscriptions/{user} | Unsubscribe user from issue
[**issue_delete_time**](#issue_delete_time) | **delete** /repos/{owner}/{repo}/issues/{index}/times/{id} | Delete specific tracked time
[**issue_edit_comment**](#issue_edit_comment) | **patch** /repos/{owner}/{repo}/issues/comments/{id} | Edit a comment
[**issue_edit_comment_deprecated**](#issue_edit_comment_deprecated) | **patch** /repos/{owner}/{repo}/issues/{index}/comments/{id} | Edit a comment
[**issue_edit_issue**](#issue_edit_issue) | **patch** /repos/{owner}/{repo}/issues/{index} | Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.
[**issue_edit_issue_attachment**](#issue_edit_issue_attachment) | **patch** /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | Edit an issue attachment
[**issue_edit_issue_comment_attachment**](#issue_edit_issue_comment_attachment) | **patch** /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id} | Edit a comment attachment
[**issue_edit_issue_deadline**](#issue_edit_issue_deadline) | **post** /repos/{owner}/{repo}/issues/{index}/deadline | Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.
[**issue_edit_label**](#issue_edit_label) | **patch** /repos/{owner}/{repo}/labels/{id} | Update a label
[**issue_edit_milestone**](#issue_edit_milestone) | **patch** /repos/{owner}/{repo}/milestones/{id} | Update a milestone
[**issue_get_comment**](#issue_get_comment) | **get** /repos/{owner}/{repo}/issues/comments/{id} | Get a comment
[**issue_get_comment_reactions**](#issue_get_comment_reactions) | **get** /repos/{owner}/{repo}/issues/comments/{id}/reactions | Get a list of reactions from a comment of an issue
[**issue_get_comments**](#issue_get_comments) | **get** /repos/{owner}/{repo}/issues/{index}/comments | List all comments on an issue
[**issue_get_comments_and_timeline**](#issue_get_comments_and_timeline) | **get** /repos/{owner}/{repo}/issues/{index}/timeline | List all comments and events on an issue
[**issue_get_issue**](#issue_get_issue) | **get** /repos/{owner}/{repo}/issues/{index} | Get an issue
[**issue_get_issue_attachment**](#issue_get_issue_attachment) | **get** /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | Get an issue attachment
[**issue_get_issue_comment_attachment**](#issue_get_issue_comment_attachment) | **get** /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id} | Get a comment attachment
[**issue_get_issue_reactions**](#issue_get_issue_reactions) | **get** /repos/{owner}/{repo}/issues/{index}/reactions | Get a list reactions of an issue
[**issue_get_label**](#issue_get_label) | **get** /repos/{owner}/{repo}/labels/{id} | Get a single label
[**issue_get_labels**](#issue_get_labels) | **get** /repos/{owner}/{repo}/issues/{index}/labels | Get an issue&#x27;s labels
[**issue_get_milestone**](#issue_get_milestone) | **get** /repos/{owner}/{repo}/milestones/{id} | Get a milestone
[**issue_get_milestones_list**](#issue_get_milestones_list) | **get** /repos/{owner}/{repo}/milestones | Get all of a repository&#x27;s opened milestones
[**issue_get_repo_comments**](#issue_get_repo_comments) | **get** /repos/{owner}/{repo}/issues/comments | List all comments in a repository
[**issue_list_issue_attachments**](#issue_list_issue_attachments) | **get** /repos/{owner}/{repo}/issues/{index}/assets | List issue&#x27;s attachments
[**issue_list_issue_comment_attachments**](#issue_list_issue_comment_attachments) | **get** /repos/{owner}/{repo}/issues/comments/{id}/assets | List comment&#x27;s attachments
[**issue_list_issues**](#issue_list_issues) | **get** /repos/{owner}/{repo}/issues | List a repository&#x27;s issues
[**issue_list_labels**](#issue_list_labels) | **get** /repos/{owner}/{repo}/labels | Get all of a repository&#x27;s labels
[**issue_post_comment_reaction**](#issue_post_comment_reaction) | **post** /repos/{owner}/{repo}/issues/comments/{id}/reactions | Add a reaction to a comment of an issue
[**issue_post_issue_reaction**](#issue_post_issue_reaction) | **post** /repos/{owner}/{repo}/issues/{index}/reactions | Add a reaction to an issue
[**issue_remove_label**](#issue_remove_label) | **delete** /repos/{owner}/{repo}/issues/{index}/labels/{id} | Remove a label from an issue
[**issue_replace_labels**](#issue_replace_labels) | **put** /repos/{owner}/{repo}/issues/{index}/labels | Replace an issue&#x27;s labels
[**issue_reset_time**](#issue_reset_time) | **delete** /repos/{owner}/{repo}/issues/{index}/times | Reset a tracked time of an issue
[**issue_search_issues**](#issue_search_issues) | **get** /repos/issues/search | Search for issues across the repositories that the user has access to
[**issue_start_stop_watch**](#issue_start_stop_watch) | **post** /repos/{owner}/{repo}/issues/{index}/stopwatch/start | Start stopwatch on an issue.
[**issue_stop_stop_watch**](#issue_stop_stop_watch) | **post** /repos/{owner}/{repo}/issues/{index}/stopwatch/stop | Stop an issue&#x27;s existing stopwatch.
[**issue_subscriptions**](#issue_subscriptions) | **get** /repos/{owner}/{repo}/issues/{index}/subscriptions | Get users who subscribed on an issue.
[**issue_tracked_times**](#issue_tracked_times) | **get** /repos/{owner}/{repo}/issues/{index}/times | List an issue&#x27;s tracked times

# **issue_add_label**
<a id="issue_add_label"></a>
> [Label] issue_add_label(ownerrepoindex)

Add a label to an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.label import Label
from allspice_client.model.issue_labels_option import IssueLabelsOption
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Add a label to an issue
        api_response = api_instance.issue_add_label(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_add_label: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    body = IssueLabelsOption(
        labels=[
            1
        ],
    )
    try:
        # Add a label to an issue
        api_response = api_instance.issue_add_label(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_add_label: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IssueLabelsOption**](../../models/IssueLabelsOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_add_label.ApiResponseFor200) | LabelList
403 | [ApiResponseFor403](#issue_add_label.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_add_label.ApiResponseFor200
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
[**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) |  | 

#### issue_add_label.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_add_subscription**
<a id="issue_add_subscription"></a>
> issue_add_subscription(ownerrepoindexuser)

Subscribe user to issue

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'user': "user_example",
    }
    try:
        # Subscribe user to issue
        api_response = api_instance.issue_add_subscription(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_add_subscription: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 
user | UserSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_add_subscription.ApiResponseFor200) | Already subscribed
201 | [ApiResponseFor201](#issue_add_subscription.ApiResponseFor201) | Successfully Subscribed
304 | [ApiResponseFor304](#issue_add_subscription.ApiResponseFor304) | User can only subscribe itself if he is no admin
404 | [ApiResponseFor404](#issue_add_subscription.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_add_subscription.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_add_subscription.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_add_subscription.ApiResponseFor304
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_add_subscription.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_add_time**
<a id="issue_add_time"></a>
> TrackedTime issue_add_time(ownerrepoindex)

Add tracked time to a issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.tracked_time import TrackedTime
from allspice_client.model.add_time_option import AddTimeOption
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Add tracked time to a issue
        api_response = api_instance.issue_add_time(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_add_time: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    body = AddTimeOption(
        created="1970-01-01T00:00:00.00Z",
        time=1,
        user_name="user_name_example",
    )
    try:
        # Add tracked time to a issue
        api_response = api_instance.issue_add_time(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_add_time: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddTimeOption**](../../models/AddTimeOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_add_time.ApiResponseFor200) | TrackedTime
400 | [ApiResponseFor400](#issue_add_time.ApiResponseFor400) | APIError is error format response
403 | [ApiResponseFor403](#issue_add_time.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_add_time.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TrackedTime**](../../models/TrackedTime.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**TrackedTime**](../../models/TrackedTime.md) |  | 


#### issue_add_time.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor400 |  |
#### ResponseHeadersFor400

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


#### issue_add_time.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_check_subscription**
<a id="issue_check_subscription"></a>
> WatchInfo issue_check_subscription(ownerrepoindex)

Check if user is subscribed to an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.watch_info import WatchInfo
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Check if user is subscribed to an issue
        api_response = api_instance.issue_check_subscription(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_check_subscription: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_check_subscription.ApiResponseFor200) | WatchInfo
404 | [ApiResponseFor404](#issue_check_subscription.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_check_subscription.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WatchInfo**](../../models/WatchInfo.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**WatchInfo**](../../models/WatchInfo.md) |  | 


#### issue_check_subscription.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_clear_labels**
<a id="issue_clear_labels"></a>
> issue_clear_labels(ownerrepoindex)

Remove all labels from an issue

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Remove all labels from an issue
        api_response = api_instance.issue_clear_labels(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_clear_labels: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_clear_labels.ApiResponseFor204) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_clear_labels.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_clear_labels.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_clear_labels.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_create_comment**
<a id="issue_create_comment"></a>
> Comment issue_create_comment(ownerrepoindex)

Add a comment to an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.create_issue_comment_option import CreateIssueCommentOption
from allspice_client.model.comment import Comment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Add a comment to an issue
        api_response = api_instance.issue_create_comment(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_comment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    body = CreateIssueCommentOption(
        body="body_example",
    )
    try:
        # Add a comment to an issue
        api_response = api_instance.issue_create_comment(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_comment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateIssueCommentOption**](../../models/CreateIssueCommentOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#issue_create_comment.ApiResponseFor201) | Comment
403 | [ApiResponseFor403](#issue_create_comment.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_create_comment.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Comment**](../../models/Comment.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Comment**](../../models/Comment.md) |  | 


#### issue_create_comment.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_create_issue**
<a id="issue_create_issue"></a>
> Issue issue_create_issue(ownerrepo)

Create an issue. If using deadline only the date will be taken into account, and time of day ignored.

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.create_issue_option import CreateIssueOption
from allspice_client.model.issue import Issue
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    try:
        # Create an issue. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_create_issue(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    body = CreateIssueOption(
        assignee="assignee_example",
        assignees=[
            "assignees_example"
        ],
        body="body_example",
        closed=True,
        due_date="1970-01-01T00:00:00.00Z",
        labels=[
            1
        ],
        milestone=1,
        ref="ref_example",
        title="title_example",
    )
    try:
        # Create an issue. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_create_issue(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateIssueOption**](../../models/CreateIssueOption.md) |  | 


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
201 | [ApiResponseFor201](#issue_create_issue.ApiResponseFor201) | Issue
403 | [ApiResponseFor403](#issue_create_issue.ApiResponseFor403) | APIForbiddenError is a forbidden error response
412 | [ApiResponseFor412](#issue_create_issue.ApiResponseFor412) | APIError is error format response
422 | [ApiResponseFor422](#issue_create_issue.ApiResponseFor422) | APIValidationError is error format response related to input validation

#### issue_create_issue.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Issue**](../../models/Issue.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Issue**](../../models/Issue.md) |  | 


#### issue_create_issue.ApiResponseFor403
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


#### issue_create_issue.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor412 |  |
#### ResponseHeadersFor412

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


#### issue_create_issue.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor422 |  |
#### ResponseHeadersFor422

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_create_issue_attachment**
<a id="issue_create_issue_attachment"></a>
> Attachment issue_create_issue_attachment(ownerrepoindexany_type)

Create an issue attachment

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.attachment import Attachment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
    }
    body = dict(
        attachment=open('/path/to/file', 'rb'),
    )
    try:
        # Create an issue attachment
        api_response = api_instance.issue_create_issue_attachment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue_attachment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
        'name': "name_example",
    }
    body = dict(
        attachment=open('/path/to/file', 'rb'),
    )
    try:
        # Create an issue attachment
        api_response = api_instance.issue_create_issue_attachment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**attachment** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | attachment to upload | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#issue_create_issue_attachment.ApiResponseFor201) | Attachment
400 | [ApiResponseFor400](#issue_create_issue_attachment.ApiResponseFor400) | APIError is error format response
404 | [ApiResponseFor404](#issue_create_issue_attachment.ApiResponseFor404) | APIError is error format response

#### issue_create_issue_attachment.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


#### issue_create_issue_attachment.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor400 |  |
#### ResponseHeadersFor400

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


#### issue_create_issue_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_create_issue_comment_attachment**
<a id="issue_create_issue_comment_attachment"></a>
> Attachment issue_create_issue_comment_attachment(ownerrepoidany_type)

Create a comment attachment

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.attachment import Attachment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    query_params = {
    }
    body = dict(
        attachment=open('/path/to/file', 'rb'),
    )
    try:
        # Create a comment attachment
        api_response = api_instance.issue_create_issue_comment_attachment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue_comment_attachment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    query_params = {
        'name': "name_example",
    }
    body = dict(
        attachment=open('/path/to/file', 'rb'),
    )
    try:
        # Create a comment attachment
        api_response = api_instance.issue_create_issue_comment_attachment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue_comment_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**attachment** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | attachment to upload | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#issue_create_issue_comment_attachment.ApiResponseFor201) | Attachment
400 | [ApiResponseFor400](#issue_create_issue_comment_attachment.ApiResponseFor400) | APIError is error format response
404 | [ApiResponseFor404](#issue_create_issue_comment_attachment.ApiResponseFor404) | APIError is error format response

#### issue_create_issue_comment_attachment.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


#### issue_create_issue_comment_attachment.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor400 |  |
#### ResponseHeadersFor400

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


#### issue_create_issue_comment_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_create_label**
<a id="issue_create_label"></a>
> Label issue_create_label(ownerrepo)

Create a label

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.label import Label
from allspice_client.model.create_label_option import CreateLabelOption
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    try:
        # Create a label
        api_response = api_instance.issue_create_label(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_label: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    body = CreateLabelOption(
        color="#00aabb",
        description="description_example",
        exclusive=False,
        name="name_example",
    )
    try:
        # Create a label
        api_response = api_instance.issue_create_label(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_label: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateLabelOption**](../../models/CreateLabelOption.md) |  | 


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
201 | [ApiResponseFor201](#issue_create_label.ApiResponseFor201) | Label
422 | [ApiResponseFor422](#issue_create_label.ApiResponseFor422) | APIValidationError is error format response related to input validation

#### issue_create_label.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Label**](../../models/Label.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Label**](../../models/Label.md) |  | 


#### issue_create_label.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor422 |  |
#### ResponseHeadersFor422

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_create_milestone**
<a id="issue_create_milestone"></a>
> Milestone issue_create_milestone(ownerrepo)

Create a milestone

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.create_milestone_option import CreateMilestoneOption
from allspice_client.model.milestone import Milestone
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    try:
        # Create a milestone
        api_response = api_instance.issue_create_milestone(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_milestone: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    body = CreateMilestoneOption(
        description="description_example",
        due_on="1970-01-01T00:00:00.00Z",
        state="open",
        title="title_example",
    )
    try:
        # Create a milestone
        api_response = api_instance.issue_create_milestone(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_create_milestone: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateMilestoneOption**](../../models/CreateMilestoneOption.md) |  | 


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
201 | [ApiResponseFor201](#issue_create_milestone.ApiResponseFor201) | Milestone

#### issue_create_milestone.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Milestone**](../../models/Milestone.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Milestone**](../../models/Milestone.md) |  | 


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete**
<a id="issue_delete"></a>
> issue_delete(ownerrepoindex)

Delete an issue

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Delete an issue
        api_response = api_instance.issue_delete(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_delete.ApiResponseFor204) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_delete.ApiResponseFor403) | APIForbiddenError is a forbidden error response
404 | [ApiResponseFor404](#issue_delete.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete.ApiResponseFor403
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


#### issue_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_comment**
<a id="issue_delete_comment"></a>
> issue_delete_comment(ownerrepoid)

Delete a comment

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    try:
        # Delete a comment
        api_response = api_instance.issue_delete_comment(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_comment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_delete_comment.ApiResponseFor204) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_delete_comment.ApiResponseFor403) | APIForbiddenError is a forbidden error response
404 | [ApiResponseFor404](#issue_delete_comment.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_delete_comment.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_comment.ApiResponseFor403
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


#### issue_delete_comment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_comment_deprecated**
<a id="issue_delete_comment_deprecated"></a>
> issue_delete_comment_deprecated(ownerrepoindexid)

Delete a comment

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'id': 1,
    }
    try:
        # Delete a comment
        api_response = api_instance.issue_delete_comment_deprecated(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_comment_deprecated: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 
id | IdSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_delete_comment_deprecated.ApiResponseFor204) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_delete_comment_deprecated.ApiResponseFor403) | APIForbiddenError is a forbidden error response
404 | [ApiResponseFor404](#issue_delete_comment_deprecated.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_delete_comment_deprecated.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_comment_deprecated.ApiResponseFor403
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


#### issue_delete_comment_deprecated.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_comment_reaction**
<a id="issue_delete_comment_reaction"></a>
> issue_delete_comment_reaction(ownerrepoid)

Remove a reaction from a comment of an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.edit_reaction_option import EditReactionOption
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    try:
        # Remove a reaction from a comment of an issue
        api_response = api_instance.issue_delete_comment_reaction(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_comment_reaction: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    body = EditReactionOption(
        content="content_example",
    )
    try:
        # Remove a reaction from a comment of an issue
        api_response = api_instance.issue_delete_comment_reaction(
            path_params=path_params,
            body=body,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_comment_reaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditReactionOption**](../../models/EditReactionOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_delete_comment_reaction.ApiResponseFor200) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_delete_comment_reaction.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_delete_comment_reaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_comment_reaction.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_issue_attachment**
<a id="issue_delete_issue_attachment"></a>
> issue_delete_issue_attachment(ownerrepoindexattachment_id)

Delete an issue attachment

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'attachment_id': 1,
    }
    try:
        # Delete an issue attachment
        api_response = api_instance.issue_delete_issue_attachment(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_issue_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 
attachment_id | AttachmentIdSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# AttachmentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_delete_issue_attachment.ApiResponseFor204) | APIEmpty is an empty response
404 | [ApiResponseFor404](#issue_delete_issue_attachment.ApiResponseFor404) | APIError is error format response

#### issue_delete_issue_attachment.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_issue_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_issue_comment_attachment**
<a id="issue_delete_issue_comment_attachment"></a>
> issue_delete_issue_comment_attachment(ownerrepoidattachment_id)

Delete a comment attachment

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
        'attachment_id': 1,
    }
    try:
        # Delete a comment attachment
        api_response = api_instance.issue_delete_issue_comment_attachment(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_issue_comment_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 
attachment_id | AttachmentIdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# AttachmentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_delete_issue_comment_attachment.ApiResponseFor204) | APIEmpty is an empty response
404 | [ApiResponseFor404](#issue_delete_issue_comment_attachment.ApiResponseFor404) | APIError is error format response

#### issue_delete_issue_comment_attachment.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_issue_comment_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_issue_reaction**
<a id="issue_delete_issue_reaction"></a>
> issue_delete_issue_reaction(ownerrepoindex)

Remove a reaction from an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.edit_reaction_option import EditReactionOption
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Remove a reaction from an issue
        api_response = api_instance.issue_delete_issue_reaction(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_issue_reaction: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    body = EditReactionOption(
        content="content_example",
    )
    try:
        # Remove a reaction from an issue
        api_response = api_instance.issue_delete_issue_reaction(
            path_params=path_params,
            body=body,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_issue_reaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditReactionOption**](../../models/EditReactionOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_delete_issue_reaction.ApiResponseFor200) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_delete_issue_reaction.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_delete_issue_reaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_issue_reaction.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_label**
<a id="issue_delete_label"></a>
> issue_delete_label(ownerrepoid)

Delete a label

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    try:
        # Delete a label
        api_response = api_instance.issue_delete_label(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_label: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_delete_label.ApiResponseFor204) | APIEmpty is an empty response

#### issue_delete_label.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_milestone**
<a id="issue_delete_milestone"></a>
> issue_delete_milestone(ownerrepoid)

Delete a milestone

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': "id_example",
    }
    try:
        # Delete a milestone
        api_response = api_instance.issue_delete_milestone(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_milestone: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_delete_milestone.ApiResponseFor204) | APIEmpty is an empty response

#### issue_delete_milestone.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_stop_watch**
<a id="issue_delete_stop_watch"></a>
> issue_delete_stop_watch(ownerrepoindex)

Delete an issue's existing stopwatch.

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Delete an issue's existing stopwatch.
        api_response = api_instance.issue_delete_stop_watch(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_stop_watch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_delete_stop_watch.ApiResponseFor204) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_delete_stop_watch.ApiResponseFor403) | Not repo writer, user does not have rights to toggle stopwatch
404 | [ApiResponseFor404](#issue_delete_stop_watch.ApiResponseFor404) | APINotFound is a not found empty response
409 | [ApiResponseFor409](#issue_delete_stop_watch.ApiResponseFor409) | Cannot cancel a non existent stopwatch

#### issue_delete_stop_watch.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_stop_watch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_stop_watch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_stop_watch.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_subscription**
<a id="issue_delete_subscription"></a>
> issue_delete_subscription(ownerrepoindexuser)

Unsubscribe user from issue

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'user': "user_example",
    }
    try:
        # Unsubscribe user from issue
        api_response = api_instance.issue_delete_subscription(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_subscription: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 
user | UserSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_delete_subscription.ApiResponseFor200) | Already unsubscribed
201 | [ApiResponseFor201](#issue_delete_subscription.ApiResponseFor201) | Successfully Unsubscribed
304 | [ApiResponseFor304](#issue_delete_subscription.ApiResponseFor304) | User can only subscribe itself if he is no admin
404 | [ApiResponseFor404](#issue_delete_subscription.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_delete_subscription.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_subscription.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_subscription.ApiResponseFor304
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_subscription.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_delete_time**
<a id="issue_delete_time"></a>
> issue_delete_time(ownerrepoindexid)

Delete specific tracked time

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'id': 1,
    }
    try:
        # Delete specific tracked time
        api_response = api_instance.issue_delete_time(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_time: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 
id | IdSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_delete_time.ApiResponseFor204) | APIEmpty is an empty response
400 | [ApiResponseFor400](#issue_delete_time.ApiResponseFor400) | APIError is error format response
403 | [ApiResponseFor403](#issue_delete_time.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_delete_time.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_delete_time.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor400 |  |
#### ResponseHeadersFor400

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


#### issue_delete_time.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_edit_comment**
<a id="issue_edit_comment"></a>
> Comment issue_edit_comment(ownerrepoid)

Edit a comment

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.comment import Comment
from allspice_client.model.edit_issue_comment_option import EditIssueCommentOption
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    try:
        # Edit a comment
        api_response = api_instance.issue_edit_comment(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_comment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    body = EditIssueCommentOption(
        body="body_example",
    )
    try:
        # Edit a comment
        api_response = api_instance.issue_edit_comment(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_comment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditIssueCommentOption**](../../models/EditIssueCommentOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_edit_comment.ApiResponseFor200) | Comment
204 | [ApiResponseFor204](#issue_edit_comment.ApiResponseFor204) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_edit_comment.ApiResponseFor403) | APIForbiddenError is a forbidden error response
404 | [ApiResponseFor404](#issue_edit_comment.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_edit_comment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Comment**](../../models/Comment.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Comment**](../../models/Comment.md) |  | 


#### issue_edit_comment.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_edit_comment.ApiResponseFor403
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


#### issue_edit_comment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_edit_comment_deprecated**
<a id="issue_edit_comment_deprecated"></a>
> Comment issue_edit_comment_deprecated(ownerrepoindexid)

Edit a comment

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.comment import Comment
from allspice_client.model.edit_issue_comment_option import EditIssueCommentOption
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'id': 1,
    }
    try:
        # Edit a comment
        api_response = api_instance.issue_edit_comment_deprecated(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_comment_deprecated: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'id': 1,
    }
    body = EditIssueCommentOption(
        body="body_example",
    )
    try:
        # Edit a comment
        api_response = api_instance.issue_edit_comment_deprecated(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_comment_deprecated: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditIssueCommentOption**](../../models/EditIssueCommentOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 
id | IdSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_edit_comment_deprecated.ApiResponseFor200) | Comment
204 | [ApiResponseFor204](#issue_edit_comment_deprecated.ApiResponseFor204) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_edit_comment_deprecated.ApiResponseFor403) | APIForbiddenError is a forbidden error response
404 | [ApiResponseFor404](#issue_edit_comment_deprecated.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_edit_comment_deprecated.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Comment**](../../models/Comment.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Comment**](../../models/Comment.md) |  | 


#### issue_edit_comment_deprecated.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_edit_comment_deprecated.ApiResponseFor403
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


#### issue_edit_comment_deprecated.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_edit_issue**
<a id="issue_edit_issue"></a>
> Issue issue_edit_issue(ownerrepoindex)

Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.edit_issue_option import EditIssueOption
from allspice_client.model.issue import Issue
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_edit_issue(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    body = EditIssueOption(
        assignee="assignee_example",
        assignees=[
            "assignees_example"
        ],
        body="body_example",
        due_date="1970-01-01T00:00:00.00Z",
        milestone=1,
        ref="ref_example",
        state="state_example",
        title="title_example",
        unset_due_date=True,
    )
    try:
        # Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_edit_issue(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditIssueOption**](../../models/EditIssueOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#issue_edit_issue.ApiResponseFor201) | Issue
403 | [ApiResponseFor403](#issue_edit_issue.ApiResponseFor403) | APIForbiddenError is a forbidden error response
404 | [ApiResponseFor404](#issue_edit_issue.ApiResponseFor404) | APINotFound is a not found empty response
412 | [ApiResponseFor412](#issue_edit_issue.ApiResponseFor412) | APIError is error format response

#### issue_edit_issue.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Issue**](../../models/Issue.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Issue**](../../models/Issue.md) |  | 


#### issue_edit_issue.ApiResponseFor403
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


#### issue_edit_issue.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_edit_issue.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor412 |  |
#### ResponseHeadersFor412

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_edit_issue_attachment**
<a id="issue_edit_issue_attachment"></a>
> Attachment issue_edit_issue_attachment(ownerrepoindexattachment_id)

Edit an issue attachment

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.attachment import Attachment
from allspice_client.model.edit_attachment_options import EditAttachmentOptions
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'attachment_id': 1,
    }
    try:
        # Edit an issue attachment
        api_response = api_instance.issue_edit_issue_attachment(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_attachment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'attachment_id': 1,
    }
    body = EditAttachmentOptions(
        name="name_example",
    )
    try:
        # Edit an issue attachment
        api_response = api_instance.issue_edit_issue_attachment(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditAttachmentOptions**](../../models/EditAttachmentOptions.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 
attachment_id | AttachmentIdSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# AttachmentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#issue_edit_issue_attachment.ApiResponseFor201) | Attachment
404 | [ApiResponseFor404](#issue_edit_issue_attachment.ApiResponseFor404) | APIError is error format response

#### issue_edit_issue_attachment.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


#### issue_edit_issue_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_edit_issue_comment_attachment**
<a id="issue_edit_issue_comment_attachment"></a>
> Attachment issue_edit_issue_comment_attachment(ownerrepoidattachment_id)

Edit a comment attachment

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.attachment import Attachment
from allspice_client.model.edit_attachment_options import EditAttachmentOptions
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
        'attachment_id': 1,
    }
    try:
        # Edit a comment attachment
        api_response = api_instance.issue_edit_issue_comment_attachment(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_comment_attachment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
        'attachment_id': 1,
    }
    body = EditAttachmentOptions(
        name="name_example",
    )
    try:
        # Edit a comment attachment
        api_response = api_instance.issue_edit_issue_comment_attachment(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_comment_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditAttachmentOptions**](../../models/EditAttachmentOptions.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 
attachment_id | AttachmentIdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# AttachmentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#issue_edit_issue_comment_attachment.ApiResponseFor201) | Attachment
404 | [ApiResponseFor404](#issue_edit_issue_comment_attachment.ApiResponseFor404) | APIError is error format response

#### issue_edit_issue_comment_attachment.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


#### issue_edit_issue_comment_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_edit_issue_deadline**
<a id="issue_edit_issue_deadline"></a>
> IssueDeadline issue_edit_issue_deadline(ownerrepoindex)

Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.issue_deadline import IssueDeadline
from allspice_client.model.edit_deadline_option import EditDeadlineOption
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_edit_issue_deadline(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_deadline: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    body = EditDeadlineOption(
        due_date="1970-01-01T00:00:00.00Z",
    )
    try:
        # Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_edit_issue_deadline(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_deadline: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditDeadlineOption**](../../models/EditDeadlineOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#issue_edit_issue_deadline.ApiResponseFor201) | IssueDeadline
403 | [ApiResponseFor403](#issue_edit_issue_deadline.ApiResponseFor403) | APIForbiddenError is a forbidden error response
404 | [ApiResponseFor404](#issue_edit_issue_deadline.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_edit_issue_deadline.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IssueDeadline**](../../models/IssueDeadline.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**IssueDeadline**](../../models/IssueDeadline.md) |  | 


#### issue_edit_issue_deadline.ApiResponseFor403
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


#### issue_edit_issue_deadline.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_edit_label**
<a id="issue_edit_label"></a>
> Label issue_edit_label(ownerrepoid)

Update a label

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.edit_label_option import EditLabelOption
from allspice_client.model.label import Label
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    try:
        # Update a label
        api_response = api_instance.issue_edit_label(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_label: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    body = EditLabelOption(
        color="#00aabb",
        description="description_example",
        exclusive=False,
        name="name_example",
    )
    try:
        # Update a label
        api_response = api_instance.issue_edit_label(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_label: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditLabelOption**](../../models/EditLabelOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_edit_label.ApiResponseFor200) | Label
422 | [ApiResponseFor422](#issue_edit_label.ApiResponseFor422) | APIValidationError is error format response related to input validation

#### issue_edit_label.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Label**](../../models/Label.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Label**](../../models/Label.md) |  | 


#### issue_edit_label.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor422 |  |
#### ResponseHeadersFor422

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_edit_milestone**
<a id="issue_edit_milestone"></a>
> Milestone issue_edit_milestone(ownerrepoid)

Update a milestone

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.edit_milestone_option import EditMilestoneOption
from allspice_client.model.milestone import Milestone
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': "id_example",
    }
    try:
        # Update a milestone
        api_response = api_instance.issue_edit_milestone(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_milestone: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': "id_example",
    }
    body = EditMilestoneOption(
        description="description_example",
        due_on="1970-01-01T00:00:00.00Z",
        state="state_example",
        title="title_example",
    )
    try:
        # Update a milestone
        api_response = api_instance.issue_edit_milestone(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_milestone: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditMilestoneOption**](../../models/EditMilestoneOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_edit_milestone.ApiResponseFor200) | Milestone

#### issue_edit_milestone.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Milestone**](../../models/Milestone.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Milestone**](../../models/Milestone.md) |  | 


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_comment**
<a id="issue_get_comment"></a>
> Comment issue_get_comment(ownerrepoid)

Get a comment

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.comment import Comment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    try:
        # Get a comment
        api_response = api_instance.issue_get_comment(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comment: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_comment.ApiResponseFor200) | Comment
204 | [ApiResponseFor204](#issue_get_comment.ApiResponseFor204) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_get_comment.ApiResponseFor403) | APIForbiddenError is a forbidden error response
404 | [ApiResponseFor404](#issue_get_comment.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_get_comment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Comment**](../../models/Comment.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Comment**](../../models/Comment.md) |  | 


#### issue_get_comment.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_get_comment.ApiResponseFor403
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


#### issue_get_comment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_comment_reactions**
<a id="issue_get_comment_reactions"></a>
> [Reaction] issue_get_comment_reactions(ownerrepoid)

Get a list of reactions from a comment of an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.reaction import Reaction
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    try:
        # Get a list of reactions from a comment of an issue
        api_response = api_instance.issue_get_comment_reactions(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comment_reactions: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_comment_reactions.ApiResponseFor200) | ReactionList
403 | [ApiResponseFor403](#issue_get_comment_reactions.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_get_comment_reactions.ApiResponseFor200
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
[**Reaction**]({{complexTypePrefix}}Reaction.md) | [**Reaction**]({{complexTypePrefix}}Reaction.md) | [**Reaction**]({{complexTypePrefix}}Reaction.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Reaction**]({{complexTypePrefix}}Reaction.md) | [**Reaction**]({{complexTypePrefix}}Reaction.md) | [**Reaction**]({{complexTypePrefix}}Reaction.md) |  | 

#### issue_get_comment_reactions.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_comments**
<a id="issue_get_comments"></a>
> [Comment] issue_get_comments(ownerrepoindex)

List all comments on an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.comment import Comment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
    }
    try:
        # List all comments on an issue
        api_response = api_instance.issue_get_comments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comments: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
        'since': "1970-01-01T00:00:00.00Z",
        'before': "1970-01-01T00:00:00.00Z",
    }
    try:
        # List all comments on an issue
        api_response = api_instance.issue_get_comments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comments: %s\n" % e)
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
since | SinceSchema | | optional
before | BeforeSchema | | optional


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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_comments.ApiResponseFor200) | CommentList

#### issue_get_comments.ApiResponseFor200
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
[**Comment**]({{complexTypePrefix}}Comment.md) | [**Comment**]({{complexTypePrefix}}Comment.md) | [**Comment**]({{complexTypePrefix}}Comment.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Comment**]({{complexTypePrefix}}Comment.md) | [**Comment**]({{complexTypePrefix}}Comment.md) | [**Comment**]({{complexTypePrefix}}Comment.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_comments_and_timeline**
<a id="issue_get_comments_and_timeline"></a>
> [TimelineComment] issue_get_comments_and_timeline(ownerrepoindex)

List all comments and events on an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.timeline_comment import TimelineComment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
    }
    try:
        # List all comments and events on an issue
        api_response = api_instance.issue_get_comments_and_timeline(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comments_and_timeline: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
        'since': "1970-01-01T00:00:00.00Z",
        'page': 1,
        'limit': 1,
        'before': "1970-01-01T00:00:00.00Z",
    }
    try:
        # List all comments and events on an issue
        api_response = api_instance.issue_get_comments_and_timeline(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comments_and_timeline: %s\n" % e)
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
since | SinceSchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional
before | BeforeSchema | | optional


# SinceSchema

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

# BeforeSchema

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
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_comments_and_timeline.ApiResponseFor200) | TimelineList

#### issue_get_comments_and_timeline.ApiResponseFor200
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
[**TimelineComment**]({{complexTypePrefix}}TimelineComment.md) | [**TimelineComment**]({{complexTypePrefix}}TimelineComment.md) | [**TimelineComment**]({{complexTypePrefix}}TimelineComment.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TimelineComment**]({{complexTypePrefix}}TimelineComment.md) | [**TimelineComment**]({{complexTypePrefix}}TimelineComment.md) | [**TimelineComment**]({{complexTypePrefix}}TimelineComment.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_issue**
<a id="issue_get_issue"></a>
> Issue issue_get_issue(ownerrepoindex)

Get an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.issue import Issue
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Get an issue
        api_response = api_instance.issue_get_issue(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_issue: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_issue.ApiResponseFor200) | Issue
404 | [ApiResponseFor404](#issue_get_issue.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_get_issue.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Issue**](../../models/Issue.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Issue**](../../models/Issue.md) |  | 


#### issue_get_issue.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_issue_attachment**
<a id="issue_get_issue_attachment"></a>
> Attachment issue_get_issue_attachment(ownerrepoindexattachment_id)

Get an issue attachment

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.attachment import Attachment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'attachment_id': 1,
    }
    try:
        # Get an issue attachment
        api_response = api_instance.issue_get_issue_attachment(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_issue_attachment: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 
attachment_id | AttachmentIdSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# AttachmentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_issue_attachment.ApiResponseFor200) | Attachment
404 | [ApiResponseFor404](#issue_get_issue_attachment.ApiResponseFor404) | APIError is error format response

#### issue_get_issue_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


#### issue_get_issue_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_issue_comment_attachment**
<a id="issue_get_issue_comment_attachment"></a>
> Attachment issue_get_issue_comment_attachment(ownerrepoidattachment_id)

Get a comment attachment

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.attachment import Attachment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
        'attachment_id': 1,
    }
    try:
        # Get a comment attachment
        api_response = api_instance.issue_get_issue_comment_attachment(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_issue_comment_attachment: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 
attachment_id | AttachmentIdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# AttachmentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_issue_comment_attachment.ApiResponseFor200) | Attachment
404 | [ApiResponseFor404](#issue_get_issue_comment_attachment.ApiResponseFor404) | APIError is error format response

#### issue_get_issue_comment_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Attachment**](../../models/Attachment.md) |  | 


#### issue_get_issue_comment_attachment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_issue_reactions**
<a id="issue_get_issue_reactions"></a>
> [Reaction] issue_get_issue_reactions(ownerrepoindex)

Get a list reactions of an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.reaction import Reaction
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
    }
    try:
        # Get a list reactions of an issue
        api_response = api_instance.issue_get_issue_reactions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_issue_reactions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
        'page': 1,
        'limit': 1,
    }
    try:
        # Get a list reactions of an issue
        api_response = api_instance.issue_get_issue_reactions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_issue_reactions: %s\n" % e)
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
page | PageSchema | | optional
limit | LimitSchema | | optional


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
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_issue_reactions.ApiResponseFor200) | ReactionList
403 | [ApiResponseFor403](#issue_get_issue_reactions.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_get_issue_reactions.ApiResponseFor200
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
[**Reaction**]({{complexTypePrefix}}Reaction.md) | [**Reaction**]({{complexTypePrefix}}Reaction.md) | [**Reaction**]({{complexTypePrefix}}Reaction.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Reaction**]({{complexTypePrefix}}Reaction.md) | [**Reaction**]({{complexTypePrefix}}Reaction.md) | [**Reaction**]({{complexTypePrefix}}Reaction.md) |  | 

#### issue_get_issue_reactions.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_label**
<a id="issue_get_label"></a>
> Label issue_get_label(ownerrepoid)

Get a single label

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.label import Label
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    try:
        # Get a single label
        api_response = api_instance.issue_get_label(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_label: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_label.ApiResponseFor200) | Label

#### issue_get_label.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Label**](../../models/Label.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Label**](../../models/Label.md) |  | 


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_labels**
<a id="issue_get_labels"></a>
> [Label] issue_get_labels(ownerrepoindex)

Get an issue's labels

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.label import Label
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Get an issue's labels
        api_response = api_instance.issue_get_labels(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_labels: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_labels.ApiResponseFor200) | LabelList
404 | [ApiResponseFor404](#issue_get_labels.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_get_labels.ApiResponseFor200
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
[**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) |  | 

#### issue_get_labels.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_milestone**
<a id="issue_get_milestone"></a>
> Milestone issue_get_milestone(ownerrepoid)

Get a milestone

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.milestone import Milestone
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': "id_example",
    }
    try:
        # Get a milestone
        api_response = api_instance.issue_get_milestone(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_milestone: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_get_milestone.ApiResponseFor200) | Milestone

#### issue_get_milestone.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Milestone**](../../models/Milestone.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Milestone**](../../models/Milestone.md) |  | 


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_milestones_list**
<a id="issue_get_milestones_list"></a>
> [Milestone] issue_get_milestones_list(ownerrepo)

Get all of a repository's opened milestones

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.milestone import Milestone
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
    }
    try:
        # Get all of a repository's opened milestones
        api_response = api_instance.issue_get_milestones_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_milestones_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
        'state': "state_example",
        'name': "name_example",
        'page': 1,
        'limit': 1,
    }
    try:
        # Get all of a repository's opened milestones
        api_response = api_instance.issue_get_milestones_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_milestones_list: %s\n" % e)
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
state | StateSchema | | optional
name | NameSchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional


# StateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#issue_get_milestones_list.ApiResponseFor200) | MilestoneList

#### issue_get_milestones_list.ApiResponseFor200
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
[**Milestone**]({{complexTypePrefix}}Milestone.md) | [**Milestone**]({{complexTypePrefix}}Milestone.md) | [**Milestone**]({{complexTypePrefix}}Milestone.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Milestone**]({{complexTypePrefix}}Milestone.md) | [**Milestone**]({{complexTypePrefix}}Milestone.md) | [**Milestone**]({{complexTypePrefix}}Milestone.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_get_repo_comments**
<a id="issue_get_repo_comments"></a>
> [Comment] issue_get_repo_comments(ownerrepo)

List all comments in a repository

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.comment import Comment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
    }
    try:
        # List all comments in a repository
        api_response = api_instance.issue_get_repo_comments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_repo_comments: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
        'since': "1970-01-01T00:00:00.00Z",
        'before': "1970-01-01T00:00:00.00Z",
        'page': 1,
        'limit': 1,
    }
    try:
        # List all comments in a repository
        api_response = api_instance.issue_get_repo_comments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_get_repo_comments: %s\n" % e)
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
since | SinceSchema | | optional
before | BeforeSchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional


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
200 | [ApiResponseFor200](#issue_get_repo_comments.ApiResponseFor200) | CommentList

#### issue_get_repo_comments.ApiResponseFor200
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
[**Comment**]({{complexTypePrefix}}Comment.md) | [**Comment**]({{complexTypePrefix}}Comment.md) | [**Comment**]({{complexTypePrefix}}Comment.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Comment**]({{complexTypePrefix}}Comment.md) | [**Comment**]({{complexTypePrefix}}Comment.md) | [**Comment**]({{complexTypePrefix}}Comment.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_list_issue_attachments**
<a id="issue_list_issue_attachments"></a>
> [Attachment] issue_list_issue_attachments(ownerrepoindex)

List issue's attachments

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.attachment import Attachment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # List issue's attachments
        api_response = api_instance.issue_list_issue_attachments(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_list_issue_attachments: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_list_issue_attachments.ApiResponseFor200) | AttachmentList
404 | [ApiResponseFor404](#issue_list_issue_attachments.ApiResponseFor404) | APIError is error format response

#### issue_list_issue_attachments.ApiResponseFor200
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
[**Attachment**]({{complexTypePrefix}}Attachment.md) | [**Attachment**]({{complexTypePrefix}}Attachment.md) | [**Attachment**]({{complexTypePrefix}}Attachment.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Attachment**]({{complexTypePrefix}}Attachment.md) | [**Attachment**]({{complexTypePrefix}}Attachment.md) | [**Attachment**]({{complexTypePrefix}}Attachment.md) |  | 

#### issue_list_issue_attachments.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_list_issue_comment_attachments**
<a id="issue_list_issue_comment_attachments"></a>
> [Attachment] issue_list_issue_comment_attachments(ownerrepoid)

List comment's attachments

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.attachment import Attachment
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    try:
        # List comment's attachments
        api_response = api_instance.issue_list_issue_comment_attachments(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_list_issue_comment_attachments: %s\n" % e)
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
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_list_issue_comment_attachments.ApiResponseFor200) | AttachmentList
404 | [ApiResponseFor404](#issue_list_issue_comment_attachments.ApiResponseFor404) | APIError is error format response

#### issue_list_issue_comment_attachments.ApiResponseFor200
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
[**Attachment**]({{complexTypePrefix}}Attachment.md) | [**Attachment**]({{complexTypePrefix}}Attachment.md) | [**Attachment**]({{complexTypePrefix}}Attachment.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Attachment**]({{complexTypePrefix}}Attachment.md) | [**Attachment**]({{complexTypePrefix}}Attachment.md) | [**Attachment**]({{complexTypePrefix}}Attachment.md) |  | 

#### issue_list_issue_comment_attachments.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_list_issues**
<a id="issue_list_issues"></a>
> [Issue] issue_list_issues(ownerrepo)

List a repository's issues

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.issue import Issue
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
    }
    try:
        # List a repository's issues
        api_response = api_instance.issue_list_issues(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_list_issues: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
        'state': "closed",
        'labels': "labels_example",
        'q': "q_example",
        'type': "issues",
        'milestones': "milestones_example",
        'since': "1970-01-01T00:00:00.00Z",
        'before': "1970-01-01T00:00:00.00Z",
        'created_by': "created_by_example",
        'assigned_by': "assigned_by_example",
        'mentioned_by': "mentioned_by_example",
        'page': 1,
        'limit': 1,
    }
    try:
        # List a repository's issues
        api_response = api_instance.issue_list_issues(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_list_issues: %s\n" % e)
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
state | StateSchema | | optional
labels | LabelsSchema | | optional
q | QSchema | | optional
type | TypeSchema | | optional
milestones | MilestonesSchema | | optional
since | SinceSchema | | optional
before | BeforeSchema | | optional
created_by | CreatedBySchema | | optional
assigned_by | AssignedBySchema | | optional
mentioned_by | MentionedBySchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional


# StateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["closed", "open", "all", ] 

# LabelsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["issues", "pulls", ] 

# MilestonesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

# CreatedBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignedBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MentionedBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#issue_list_issues.ApiResponseFor200) | IssueList

#### issue_list_issues.ApiResponseFor200
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
[**Issue**]({{complexTypePrefix}}Issue.md) | [**Issue**]({{complexTypePrefix}}Issue.md) | [**Issue**]({{complexTypePrefix}}Issue.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Issue**]({{complexTypePrefix}}Issue.md) | [**Issue**]({{complexTypePrefix}}Issue.md) | [**Issue**]({{complexTypePrefix}}Issue.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_list_labels**
<a id="issue_list_labels"></a>
> [Label] issue_list_labels(ownerrepo)

Get all of a repository's labels

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.label import Label
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
    }
    try:
        # Get all of a repository's labels
        api_response = api_instance.issue_list_labels(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_list_labels: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
    }
    query_params = {
        'page': 1,
        'limit': 1,
    }
    try:
        # Get all of a repository's labels
        api_response = api_instance.issue_list_labels(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_list_labels: %s\n" % e)
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
page | PageSchema | | optional
limit | LimitSchema | | optional


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
200 | [ApiResponseFor200](#issue_list_labels.ApiResponseFor200) | LabelList

#### issue_list_labels.ApiResponseFor200
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
[**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_post_comment_reaction**
<a id="issue_post_comment_reaction"></a>
> Reaction issue_post_comment_reaction(ownerrepoid)

Add a reaction to a comment of an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.edit_reaction_option import EditReactionOption
from allspice_client.model.reaction import Reaction
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    try:
        # Add a reaction to a comment of an issue
        api_response = api_instance.issue_post_comment_reaction(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_post_comment_reaction: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'id': 1,
    }
    body = EditReactionOption(
        content="content_example",
    )
    try:
        # Add a reaction to a comment of an issue
        api_response = api_instance.issue_post_comment_reaction(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_post_comment_reaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditReactionOption**](../../models/EditReactionOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
id | IdSchema | | 

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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_post_comment_reaction.ApiResponseFor200) | Reaction
201 | [ApiResponseFor201](#issue_post_comment_reaction.ApiResponseFor201) | Reaction
403 | [ApiResponseFor403](#issue_post_comment_reaction.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_post_comment_reaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Reaction**](../../models/Reaction.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Reaction**](../../models/Reaction.md) |  | 


#### issue_post_comment_reaction.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Reaction**](../../models/Reaction.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Reaction**](../../models/Reaction.md) |  | 


#### issue_post_comment_reaction.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_post_issue_reaction**
<a id="issue_post_issue_reaction"></a>
> Reaction issue_post_issue_reaction(ownerrepoindex)

Add a reaction to an issue

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.edit_reaction_option import EditReactionOption
from allspice_client.model.reaction import Reaction
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Add a reaction to an issue
        api_response = api_instance.issue_post_issue_reaction(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_post_issue_reaction: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    body = EditReactionOption(
        content="content_example",
    )
    try:
        # Add a reaction to an issue
        api_response = api_instance.issue_post_issue_reaction(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_post_issue_reaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditReactionOption**](../../models/EditReactionOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_post_issue_reaction.ApiResponseFor200) | Reaction
201 | [ApiResponseFor201](#issue_post_issue_reaction.ApiResponseFor201) | Reaction
403 | [ApiResponseFor403](#issue_post_issue_reaction.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_post_issue_reaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Reaction**](../../models/Reaction.md) |  | 


# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Reaction**](../../models/Reaction.md) |  | 


#### issue_post_issue_reaction.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Reaction**](../../models/Reaction.md) |  | 


# SchemaFor201ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**Reaction**](../../models/Reaction.md) |  | 


#### issue_post_issue_reaction.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_remove_label**
<a id="issue_remove_label"></a>
> issue_remove_label(ownerrepoindexid)

Remove a label from an issue

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
        'id': 1,
    }
    try:
        # Remove a label from an issue
        api_response = api_instance.issue_remove_label(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_remove_label: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 
id | IdSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_remove_label.ApiResponseFor204) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_remove_label.ApiResponseFor403) | APIForbiddenError is a forbidden error response
422 | [ApiResponseFor422](#issue_remove_label.ApiResponseFor422) | APIValidationError is error format response related to input validation

#### issue_remove_label.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_remove_label.ApiResponseFor403
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


#### issue_remove_label.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor422 |  |
#### ResponseHeadersFor422

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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_replace_labels**
<a id="issue_replace_labels"></a>
> [Label] issue_replace_labels(ownerrepoindex)

Replace an issue's labels

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.label import Label
from allspice_client.model.issue_labels_option import IssueLabelsOption
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Replace an issue's labels
        api_response = api_instance.issue_replace_labels(
            path_params=path_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_replace_labels: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    body = IssueLabelsOption(
        labels=[
            1
        ],
    )
    try:
        # Replace an issue's labels
        api_response = api_instance.issue_replace_labels(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_replace_labels: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IssueLabelsOption**](../../models/IssueLabelsOption.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_replace_labels.ApiResponseFor200) | LabelList
403 | [ApiResponseFor403](#issue_replace_labels.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_replace_labels.ApiResponseFor200
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
[**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) | [**Label**]({{complexTypePrefix}}Label.md) |  | 

#### issue_replace_labels.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_reset_time**
<a id="issue_reset_time"></a>
> issue_reset_time(ownerrepoindex)

Reset a tracked time of an issue

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Reset a tracked time of an issue
        api_response = api_instance.issue_reset_time(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_reset_time: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#issue_reset_time.ApiResponseFor204) | APIEmpty is an empty response
400 | [ApiResponseFor400](#issue_reset_time.ApiResponseFor400) | APIError is error format response
403 | [ApiResponseFor403](#issue_reset_time.ApiResponseFor403) | APIForbiddenError is a forbidden error response

#### issue_reset_time.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_reset_time.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor400 |  |
#### ResponseHeadersFor400

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


#### issue_reset_time.ApiResponseFor403
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


### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_search_issues**
<a id="issue_search_issues"></a>
> [Issue] issue_search_issues()

Search for issues across the repositories that the user has access to

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.issue import Issue
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only optional values
    query_params = {
        'state': "state_example",
        'labels': "labels_example",
        'milestones': "milestones_example",
        'q': "q_example",
        'priority_repo_id': 1,
        'type': "type_example",
        'since': "1970-01-01T00:00:00.00Z",
        'before': "1970-01-01T00:00:00.00Z",
        'assigned': True,
        'created': True,
        'mentioned': True,
        'review_requested': True,
        'owner': "owner_example",
        'team': "team_example",
        'page': 1,
        'limit': 1,
    }
    try:
        # Search for issues across the repositories that the user has access to
        api_response = api_instance.issue_search_issues(
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_search_issues: %s\n" % e)
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
state | StateSchema | | optional
labels | LabelsSchema | | optional
milestones | MilestonesSchema | | optional
q | QSchema | | optional
priority_repo_id | PriorityRepoIdSchema | | optional
type | TypeSchema | | optional
since | SinceSchema | | optional
before | BeforeSchema | | optional
assigned | AssignedSchema | | optional
created | CreatedSchema | | optional
mentioned | MentionedSchema | | optional
review_requested | ReviewRequestedSchema | | optional
owner | OwnerSchema | | optional
team | TeamSchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional


# StateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LabelsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MilestonesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PriorityRepoIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

# AssignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# CreatedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# MentionedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ReviewRequestedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# OwnerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#issue_search_issues.ApiResponseFor200) | IssueList

#### issue_search_issues.ApiResponseFor200
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
[**Issue**]({{complexTypePrefix}}Issue.md) | [**Issue**]({{complexTypePrefix}}Issue.md) | [**Issue**]({{complexTypePrefix}}Issue.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Issue**]({{complexTypePrefix}}Issue.md) | [**Issue**]({{complexTypePrefix}}Issue.md) | [**Issue**]({{complexTypePrefix}}Issue.md) |  | 

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_start_stop_watch**
<a id="issue_start_stop_watch"></a>
> issue_start_stop_watch(ownerrepoindex)

Start stopwatch on an issue.

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Start stopwatch on an issue.
        api_response = api_instance.issue_start_stop_watch(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_start_stop_watch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#issue_start_stop_watch.ApiResponseFor201) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_start_stop_watch.ApiResponseFor403) | Not repo writer, user does not have rights to toggle stopwatch
404 | [ApiResponseFor404](#issue_start_stop_watch.ApiResponseFor404) | APINotFound is a not found empty response
409 | [ApiResponseFor409](#issue_start_stop_watch.ApiResponseFor409) | Cannot start a stopwatch again if it already exists

#### issue_start_stop_watch.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_start_stop_watch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_start_stop_watch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_start_stop_watch.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_stop_stop_watch**
<a id="issue_stop_stop_watch"></a>
> issue_stop_stop_watch(ownerrepoindex)

Stop an issue's existing stopwatch.

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
from allspice_client.apis.tags import issue_api
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    try:
        # Stop an issue's existing stopwatch.
        api_response = api_instance.issue_stop_stop_watch(
            path_params=path_params,
        )
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_stop_stop_watch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
owner | OwnerSchema | | 
repo | RepoSchema | | 
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#issue_stop_stop_watch.ApiResponseFor201) | APIEmpty is an empty response
403 | [ApiResponseFor403](#issue_stop_stop_watch.ApiResponseFor403) | Not repo writer, user does not have rights to toggle stopwatch
404 | [ApiResponseFor404](#issue_stop_stop_watch.ApiResponseFor404) | APINotFound is a not found empty response
409 | [ApiResponseFor409](#issue_stop_stop_watch.ApiResponseFor409) | Cannot stop a non existent stopwatch

#### issue_stop_stop_watch.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_stop_stop_watch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_stop_stop_watch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### issue_stop_stop_watch.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_subscriptions**
<a id="issue_subscriptions"></a>
> [User] issue_subscriptions(ownerrepoindex)

Get users who subscribed on an issue.

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.user import User
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
    }
    try:
        # Get users who subscribed on an issue.
        api_response = api_instance.issue_subscriptions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_subscriptions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
        'page': 1,
        'limit': 1,
    }
    try:
        # Get users who subscribed on an issue.
        api_response = api_instance.issue_subscriptions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_subscriptions: %s\n" % e)
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
page | PageSchema | | optional
limit | LimitSchema | | optional


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
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_subscriptions.ApiResponseFor200) | UserList
404 | [ApiResponseFor404](#issue_subscriptions.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_subscriptions.ApiResponseFor200
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
[**User**]({{complexTypePrefix}}User.md) | [**User**]({{complexTypePrefix}}User.md) | [**User**]({{complexTypePrefix}}User.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**User**]({{complexTypePrefix}}User.md) | [**User**]({{complexTypePrefix}}User.md) | [**User**]({{complexTypePrefix}}User.md) |  | 

#### issue_subscriptions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **issue_tracked_times**
<a id="issue_tracked_times"></a>
> [TrackedTime] issue_tracked_times(ownerrepoindex)

List an issue's tracked times

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
from allspice_client.apis.tags import issue_api
from allspice_client.model.tracked_time import TrackedTime
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
    api_instance = issue_api.IssueApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
    }
    try:
        # List an issue's tracked times
        api_response = api_instance.issue_tracked_times(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_tracked_times: %s\n" % e)

    # example passing only optional values
    path_params = {
        'owner': "owner_example",
        'repo': "repo_example",
        'index': 1,
    }
    query_params = {
        'user': "user_example",
        'since': "1970-01-01T00:00:00.00Z",
        'before': "1970-01-01T00:00:00.00Z",
        'page': 1,
        'limit': 1,
    }
    try:
        # List an issue's tracked times
        api_response = api_instance.issue_tracked_times(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except allspice_client.ApiException as e:
        print("Exception when calling IssueApi->issue_tracked_times: %s\n" % e)
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
user | UserSchema | | optional
since | SinceSchema | | optional
before | BeforeSchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional


# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
index | IndexSchema | | 

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

# IndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#issue_tracked_times.ApiResponseFor200) | TrackedTimeList
404 | [ApiResponseFor404](#issue_tracked_times.ApiResponseFor404) | APINotFound is a not found empty response

#### issue_tracked_times.ApiResponseFor200
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
[**TrackedTime**]({{complexTypePrefix}}TrackedTime.md) | [**TrackedTime**]({{complexTypePrefix}}TrackedTime.md) | [**TrackedTime**]({{complexTypePrefix}}TrackedTime.md) |  | 

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TrackedTime**]({{complexTypePrefix}}TrackedTime.md) | [**TrackedTime**]({{complexTypePrefix}}TrackedTime.md) | [**TrackedTime**]({{complexTypePrefix}}TrackedTime.md) |  | 

#### issue_tracked_times.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[TOTPHeader](../../../README.md#TOTPHeader), [AuthorizationHeaderToken](../../../README.md#AuthorizationHeaderToken), [SudoHeader](../../../README.md#SudoHeader), [BasicAuth](../../../README.md#BasicAuth), [AccessToken](../../../README.md#AccessToken), [SudoParam](../../../README.md#SudoParam), [Token](../../../README.md#Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

