# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from allspice_client.paths.repos_owner_repo_topics_topic import Api

from allspice_client.paths import PathValues

path = PathValues.REPOS_OWNER_REPO_TOPICS_TOPIC