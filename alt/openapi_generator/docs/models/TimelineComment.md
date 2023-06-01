# allspice_client.model.timeline_comment.TimelineComment

TimelineComment represents a timeline comment (comment of any type) on a commit or issue

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TimelineComment represents a timeline comment (comment of any type) on a commit or issue | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**assignee** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**assignee_team** | [**Team**](Team.md) | [**Team**](Team.md) |  | [optional] 
**body** | str,  | str,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**dependent_issue** | [**Issue**](Issue.md) | [**Issue**](Issue.md) |  | [optional] 
**html_url** | str,  | str,  |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**issue_url** | str,  | str,  |  | [optional] 
**label** | [**Label**](Label.md) | [**Label**](Label.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) | [**Milestone**](Milestone.md) |  | [optional] 
**new_ref** | str,  | str,  |  | [optional] 
**new_title** | str,  | str,  |  | [optional] 
**old_milestone** | [**Milestone**](Milestone.md) | [**Milestone**](Milestone.md) |  | [optional] 
**old_project_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**old_ref** | str,  | str,  |  | [optional] 
**old_title** | str,  | str,  |  | [optional] 
**project_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**pull_request_url** | str,  | str,  |  | [optional] 
**ref_action** | str,  | str,  |  | [optional] 
**ref_comment** | [**Comment**](Comment.md) | [**Comment**](Comment.md) |  | [optional] 
**ref_commit_sha** | str,  | str,  | commit SHA where issue/PR was referenced | [optional] 
**ref_issue** | [**Issue**](Issue.md) | [**Issue**](Issue.md) |  | [optional] 
**removed_assignee** | bool,  | BoolClass,  | whether the assignees were removed or added | [optional] 
**resolve_doer** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**review_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**tracked_time** | [**TrackedTime**](TrackedTime.md) | [**TrackedTime**](TrackedTime.md) |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**user** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

