# Changelog

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
