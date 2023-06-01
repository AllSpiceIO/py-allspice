from enum import Enum


class MigrateRepoOptionsService(str, Enum):
    GIT = "git"
    GITEA = "gitea"
    GITHUB = "github"
    GITLAB = "gitlab"

    def __str__(self) -> str:
        return str(self.value)
