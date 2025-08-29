# Changelog

## v3.11.0

### Highlights

* Add support for DeHDL BOM generation by @jackHay22 in https://github.com/AllSpiceIO/py-allspice/pull/246

## v3.10.2

### Highlights

* Normalize joined paths for finding device sheets by @jackHay22 in https://github.com/AllSpiceIO/py-allspice/pull/236
* Move change_number iteration up in the loop by @yeiterjoe in https://github.com/AllSpiceIO/py-allspice/pull/239
* Remove interpolation, add iso-8859-1 fallback	by @jackHay22 in https://github.com/AllSpiceIO/py-allspice/pull/244

## v3.10.1

### Highlights

* Fix a bug where Design Review Reviews couldn't be updated or deleted on instances on a subpath by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/229

## v3.10.0

### Highlights

* Add API to create design review reviews by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/214
* Add APIs to get DRR Comments and delete a DRR by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/224

### Other Changes

* Bump ruff from 0.9.9 to 0.11.8 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/219
* Update system capture cassette and snapshot by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/221

## v3.9.0

### Highlights

* Add support for sdax variants when generating BOM  by @jackHay22 in https://github.com/AllSpiceIO/py-allspice/pull/217

### Other Changes

* Bump ruff from 0.8.4 to 0.9.9 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/213

**Full Changelog**: https://github.com/AllSpiceIO/py-allspice/compare/v3.8.0...v3.9.0

## v3.8.0

### Highlights

* Fix invalid arguments when committing releases and assets by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/204
* Create and use a log handler to actually set log level by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/188
* Use POST instead of PUT for merging Design Reviews by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/208
* Make `has_actions` patchable on Repository by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/202
* Add method to get and create Issue attachments by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/210

### Other Changes

* Bump ruff from 0.8.1 to 0.8.4 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/201
* Update libcst requirement from ~=1.4.0 to ~=1.6.0 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/206
* Change AllSpice Hub Test org name by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/207

**Full Changelog**: https://github.com/AllSpiceIO/py-allspice/compare/v3.7.0...v3.8.0

## v3.7.0

### What's Changed

- Update system capture test snapshots with added component attributes by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/187
- Update type annotations for 1.22 by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/197
- Enforce max retries in list_components by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/198

  > [!CAUTION]
  >
  > This could potentially break your BOM generation if individual files were
  > taking too long to render.

### Internal Changes

- Update pdoc requirement from ~=14.7 to ~=15.0 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/189
- Update ruff by @kdumontnu in https://github.com/AllSpiceIO/py-allspice/pull/196

**Full Changelog**: https://github.com/AllSpiceIO/py-allspice/compare/v3.6.0...v3.7.0

## v3.6.0

### What's Changed

## What's Changed

- Generate BOMs with Device Sheets and Board Level Annotations on Altium
  Projects by @shrik450 and @polypour in
  https://github.com/AllSpiceIO/py-allspice/pull/182 and
  https://github.com/AllSpiceIO/py-allspice/pull/183/

  Adds support for Altium Device Sheets and Board Level Annotations in
  `list_components` and `generate_bom`. To use device sheets located in another
  repo, pass the `design_reuse_repositories` argument to those functions.

- Update syrupy requirement from ~=4.6 to ~=4.7 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/179
- Add method to download an attachment by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/181
- Include pin information in components by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/180
- Update pdoc requirement from ~=14.5 to ~=14.7 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/185

## v3.5.0

### What's Changed

- Fix many, but not all, typing failures by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/168

  This also fixes a few bugs that have been present in the library for a while, such as adding comments failing for issues requested using `Issue.request`.

- Add endpoint to fetch git trees by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/175

  The new `Repository.get_tree` method can be used to fetch the tree of a commit in a repository. This is useful if you want to list all files in a commit, and can replace most uses of `Repository.get_git_content`.

- Refactor BOM generation to centralize logic by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/177

  This also fixes bugs in the System Capture SDAX BOM generation which prevented sorting and filtering from being applied there.

- Filter out blank components in list_components by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/176

- Add column configuration to skip in output by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/178

  A new column configuration, `skip_in_output`, can be used to remove a column from the BOM output, which is useful when a column is used for grouping, filtering or sorting but isn't required in the BOM.

### Internal Changes

- Update column config cassette to include reference changes by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/166
- Apply Ruff formatting to examples by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/173
- Skip coverage comment on dependabot PRs by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/174
- Update pytest requirement from ~=8.2 to ~=8.3 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/170

**Full Changelog**: https://github.com/AllSpiceIO/py-allspice/compare/v3.4.0...v3.5.0

## v3.4.0

### What's Changed

- Combine multi-part components for OrCAD by @shrik450 in
  https://github.com/AllSpiceIO/py-allspice/pull/161

  This fixes a correctness issue where multi-part components would be
  represented as multiple components in the BOM.

- Implement simple BOM post processing by @shrik450 in
  https://github.com/AllSpiceIO/py-allspice/pull/157

  This adds suite of configuration options to customize the output of the
  `utils.bom_generation` module. You can now sort columns, filter rows using
  regex, specify the separator for grouped columns, and more. See the docs of
  the
  [bom_generation module](https://allspiceio.github.io/py-allspice/allspice/utils/bom_generation.html)
  for more details.

- Support System Capture SDAX for components list and BOM by @shrik450 in
  https://github.com/AllSpiceIO/py-allspice/pull/164

  You can now list the components in a System Capture SDAX file using
  `utils.list_components.list_components` and generate a BOM using
  `utils.bom_generation.generate_bom`.

**Full Changelog**: https://github.com/AllSpiceIO/py-allspice/compare/v3.3.1...v3.4.0

## v3.3.1

### What's Changed

- Fix Design Review Comments not having an associated repo by @shrik450 in #162

  This fixes a bug that made it impossible to make any changes or add
  attachments to a comment on a design review.

### Internal Changes

- Update ruff requirement from ~=0.4 to ~=0.5 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/156
- Fix CI typecheck failure due to changed cassettes by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/149
- Move test repo sources to AllSpiceTests org by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/160

**Full Changelog**: https://github.com/AllSpiceIO/py-allspice/compare/v3.3.0...v3.3.1

## v3.3.0

### What's Changed

- Combine Altium multi-part components by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/147

  Earlier, multi-part Altium components would be represented as multiple
  components in both `list_components` and `generate_bom`. Now,
  `list_components` adds a keyword argument: `combine_multi_part`. When set to
  `True`, multi-part components will be combined into one component for each
  instance. In `generate_bom`, multi-part components are always combined.

### Internal Changes

- doc: Add link to built pdoc documentation by @jtran in https://github.com/AllSpiceIO/py-allspice/pull/144
- Allow manual deploys to the docs by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/143
- Speedup utils tests by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/145

## v3.2.0

### What's Changed

- Remove BOM and COGS generation examples by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/116

  The packaged actions at https://hub.allspice.io/Actions/generate-bom and
  https://hub.allspice.io/Actions/cofactr-cogs are now the source of truth for
  these scripts.

- Remove non-BOM components from Altium BOM by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/119

  py-allspice now removes Standard (No BOM) components from Altium BOMs.

- Extract components list function for Altium from BOM by @shrik450 in
  https://github.com/AllSpiceIO/py-allspice/pull/122

  Now you can:

  ```py
  from allspice.utils.list_components import list_components_for_altium

  list_components_for_altium(...) # Returns a list of all components in the project
  ```

  This is useful if you want a list of components for further processing instead
  of generating a BOM and reading it as a CSV.

- Fix doubled pins in netlist generation by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/129

- Specify versions for all dependencies by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/131
- Eliminate N+1 API requests in issues by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/135
- Add API to stream file from repo by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/136
- Automatically add type hints for API Object attributes by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/141

  All API objects now have type hints for all attributes present in them! You
  can use the type hints to type check your scripts with mypy or pylance, or
  for autocomplete in your IDE.

### Internal Changes

- Remove invalid flag from pdoc invocation by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/121
- Lint that imports are sorted by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/123
- Update pdoc requirement from ~=14.4 to ~=14.5 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/137
- Remove top-level `__init__.py` by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/133
- Add dependabot config by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/132
- Replace setup.py with pyproject metadata by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/134
- Bump actions/checkout from 3 to 4 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/139
- Bump actions/setup-python from 4 to 5 by @dependabot in https://github.com/AllSpiceIO/py-allspice/pull/138

**Full Changelog**: https://github.com/AllSpiceIO/py-allspice/compare/v3.1.0...v3.2.0

## v3.1.0

### What's Changed

- Add utils for OrCAD components and BOM by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/107

  A new util module has been added: `list_components`. Use this to get a list of
  components with all attributes as a list of dictionaries:

  ```py
  from allspice.utils import list_components

  components = list_components_for_orcad(...)
  ```

  This is useful if you want to perform further processing of your own on the
  list of components, e.g. validate whether a component is allowed.

  Along with this, BOM generation now supports OrCAD schematics! To use it, try
  `allspice.utils.bom_generation.generate_bom_orcad`.

  Py-allspice now also ships with a "universal" bom generation function:
  `allspice.utils.bom_generation.generate_bom`, which will automatically decide
  whether to use the altium or orcad bom generation.

- Add **version** attr to top level module by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/110

  Now, you can check which version of py-allspice you are using in a script:

  ```py
  import allspice

  print(allspice.__version__) # => 3.1.0
  ```

- Remove BOM and COGS generation examples by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/116

  These example scripts have been removed, and users are encouraged to refer to
  the https://github.com/AllSpiceIO/generate-bom-altium and
  https://github.com/AllSpiceIO/cofactr-cogs.

**Full Changelog**: https://github.com/AllSpiceIO/py-allspice/compare/v3.0.0...v3.1.0

## v3.0.0

There are breaking changes in this release, and you may have to update your
scripts to use this version.

### Breaking Changes

The main (and only) breaking change in this release is an overhaul of the BOM
generation utility function
`allspice.utils.bom_generation.generate_bom_for_altium`. The changes are:

1. `generate_bom_for_altium` no longer takes a PcbDoc file as an argument. The
   BOM generation logic has been reworked to only use a PrjPcb file as the sole
   entrypoint and generate the entire BOM from the schematics.

   See https://github.com/AllSpiceIO/py-allspice/pull/83

2. You can now customize the columns of the BOM and how rows are grouped using
   the `columns` and `group_by` arguments. This replaces the former
   `attributes_mapping` argument.

   For example, if you want to have columns "Comment", "Part ID" and
   "Manufacturer" in your BOM and group them by the "Part ID", you would pass:

   ```py
   generate_bom_for_altium(
      # ...
      columns={
        "Comment": ["Comment", "Description", "_description"],
        "Part ID": "_part_id",
        "Manufacturer": ["Manufacturer", "MFN"],
      },
      group_by=["Part ID"],
   )
   ```

   This also shows the `_description` and `_part_id` attributes which are
   populated from the component itself.

   See https://github.com/AllSpiceIO/py-allspice/pull/84

3. BOM generation now supports variants, and you can select which variant to
   generate a BOM for using the `variant` argument.

   See https://github.com/AllSpiceIO/py-allspice/pull/86

### Other changes

The example scripts for BOM generation and COGS generation have also been
updated to work with these new changes.

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

- Add APIs to work with commit statuses by @shrik450 in https://github.com/AllSpiceIO/py-allspice/pull/74

  Commit statuses are the status of checks run via actions on commits. You can
  use the new `Commit.get_status` and `Repository.create_commit_status` methods
  to work with them.

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
