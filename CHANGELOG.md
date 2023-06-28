# Changelog

## v2.1.0

This is a minor version bump. Only new functionality was added, and you may not
need to change your scripts to update to this version.

- Add APIs to create comments and attachments on Issues. In particular, you can
  now use `Issue.create_comment` to add a comment, and
  `Comment.create_attachment` to add an attachment to a comment.
- Add APIs for working with Design Reviews. See the `DesignReview` class for
  more details, and `Repository.create_design_review` to make one.
- Add more filters for fetching Design Reviews and Issues.
  `Repository.get_issues_state` is now deprecated, prefer using
  `Repository.get_issues` with a state filter instead.
- Fixed an issue where `Repository.get_branches` only returned the first page of
  branches in a repo.
- Add four more example scripts and a top level index for examples. Check
  [the examples folder](./examples/) for more examples.

## v2.0.0

This is a breaking change. You will need to update your scripts to use py-allspice v2.

- Renamed Gitea across py-allspice to AllSpice. For example,

    ```py
    from gitea import Gitea

    gitea = Gitea(URL, TOKEN)
    ```

    to

    ```py
    from allspice import AllSpice

    allspice_client = AllSpice(token_text=TOKEN)
    ```

- Added example scripts in [the examples directory](./examples).
- Added functions to get AllSpice generated svg and json for CAD files.
- Added optional Rate Limiting to the client. By default, Rate Limiting is on at 100
  requests every minute. You can disable it by setting `ratelimiting` to `None` when
  creating an instance of `AllSpice`.
- Added `units_map` argument when creating a new team.
