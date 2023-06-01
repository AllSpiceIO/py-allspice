# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from allspice_client.paths.user_starred_owner_repo import Api

from allspice_client.paths import PathValues

path = PathValues.USER_STARRED_OWNER_REPO