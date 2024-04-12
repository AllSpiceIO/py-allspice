# Changelog

## v2.5.0

This is a minor version bump. Only new functionality was added, and you may not
need to change your scripts to update to this version.

### New Features and Bugfixes

- Broaden newline regex in Alitum BOM generation by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/62

  This fixes a reported issue with some Altium PrjPcb files.

- Add APIs to work with releases and their assets by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/73

  Now you can fetch a repository's releases using:

  ```py
  releases = repo.get_releases()

  # or

  release = repo.get_latest_release()

  # or

  release = repo.get_release_by_tag("v1.1")

  # and even

  release = repo.create_release("v1.2")
  ```

  And add attachments to the releases:

  ```py
  release = repo.get_latest_release()
  asset = release.create_asset(gerber_file)
  asset.download() # Download the file from the server!
  ```

  See the `allspice.Release` class for more details.

- Add API method to get the raw binary content of a single file by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/77

  Example:

  ```py
  file_content = repo.get_raw_file("README.md").decode("utf-8")
  ```

  This is better than using `repo.get_file_contents` in almost all cases.

### Internals

- CI: Add cron by @kdumontnu in https://github.com/AllSpiceIO/py-allspice/pull/52
- added flake.nix by @McRaeAlex in https://github.com/AllSpiceIO/py-allspice/pull/57
- doc: Update README to fix broken example link by @jtran in https://github.com/AllSpiceIO/py-allspice/pull/59
- Remove autopep8 completely by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/67

### New Contributors

- @McRaeAlex made their first contribution in https://github.com/AllSpiceIO/py-allspice/pull/57
- @jtran made their first contribution in https://github.com/AllSpiceIO/py-allspice/pull/59

**Full Changelog**: https://github.com/AllSpiceIO/py-allspice/compare/v2.4.0...v2.5.0

## v2.4.0

### What's Changed

- CI Fixes for Gitea 1.20 by @kdumontnu in https://github.com/AllSpiceIO/py-allspice/pull/48
- Add generate netlist routine by @kdumontnu in https://github.com/AllSpiceIO/py-allspice/pull/50
- Add error message for component link error by @kdumontnu in https://github.com/AllSpiceIO/py-allspice/pull/54
- Add delete_file routine by @kdumontnu in https://github.com/AllSpiceIO/py-allspice/pull/56

### New Contributors

- @kdumontnu made their first contribution in https://github.com/AllSpiceIO/py-allspice/pull/48

**Full Changelog**: https://github.com/AllSpiceIO/py-allspice/compare/v2.3.1...v2.4.0

## v2.3.1

This is a patch release. You should be able to update to this version without
changing your scripts.

- Fix a bug where `Team.get_members` would not return all members if there
  were more than 30 members in a team.

## v2.3.0

This is a minor version bump. Only new functionality was added, and you may not
need to change your scripts to update to this version.

- New feature: BOM Generation. Instead of an example script, BOM generation is
  included as a util within the library. See `allspice.utils.generate_bom` for
  more details, and there is an example script in
  [the examples/generate_bom directory](./examples/generate_bom/) that shows how
  to use it, along with how to compute COGS from a generated BOM.
- `Team.add_repo` now takes either a string as a repo name or a `Repository`
  object, instead of just a string as before. So you can:

  ```py
  team.add_repo(team_org, "repo_name")
  ```

  Instead of:

  ```py
  repo = Repository.request(allspice_client, "team_org", "repo_name")
  team.add_repo(team_org, repo)
  ```

  This is useful if you are making a large number of changes in bulk, as you can
  save time by not having to make a request for each repo you want to add to a
  team.

## v2.2.0

This is a minor version bump. Only new functionality was added, and you may not
need to change your scripts to update to this version.

- Add Repository search API. See `Repository.search` for more details.
- Add APIs to get and set topics on a repository. See `Repository.add_topic` and
  `Repository.get_topics` for more details. Also added example scripts to bulk
  add topics and clone all repos with a certain topic.

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
