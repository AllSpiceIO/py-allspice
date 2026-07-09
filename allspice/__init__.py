"""
.. include:: ../README.md
   :start-line: 1
   :end-before: Installation
"""

from .allspice import (
    AllSpice,
)
from .apiobject import (
    Branch,
    Comment,
    Commit,
    Content,
    DesignReview,
    DesignReviewReview,
    Issue,
    Milestone,
    Organization,
    Release,
    Repository,
    Team,
    User,
)
from .exceptions import (
    AlreadyExistsException,
    APIError,
    InternalServerException,
    NotFoundException,
    RenderException,
)

__version__ = "4.2.0"

__all__ = [
    "APIError",
    "AllSpice",
    "AlreadyExistsException",
    "Branch",
    "Comment",
    "Commit",
    "Content",
    "DesignReview",
    "DesignReviewReview",
    "InternalServerException",
    "Issue",
    "Milestone",
    "NotFoundException",
    "Organization",
    "Release",
    "RenderException",
    "Repository",
    "Team",
    "User",
]
