from enum import Enum


class ListPackagesType(str, Enum):
    CARGO = "cargo"
    CHEF = "chef"
    COMPOSER = "composer"
    CONAN = "conan"
    CONDA = "conda"
    CONTAINER = "container"
    GENERIC = "generic"
    HELM = "helm"
    MAVEN = "maven"
    NPM = "npm"
    NUGET = "nuget"
    PUB = "pub"
    PYPI = "pypi"
    RUBYGEMS = "rubygems"
    VAGRANT = "vagrant"

    def __str__(self) -> str:
        return str(self.value)
