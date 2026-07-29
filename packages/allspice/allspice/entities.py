"""Hand-maintained active-record façade over the generated schema models.
One class per editable/deletable resource; the generated schema class inherits
it (e.g. `class Repository(RepositoryEntity)`).

Import discipline: this module is imported *before* schemas.py / api_requests.py
(both depend on it), so at module level it may import only from allspice.base.
References to generated classes are lazy (method-body) or TYPE_CHECKING.
"""

from collections.abc import Iterable
from typing import TYPE_CHECKING, cast

from pydantic import PrivateAttr

from allspice.base import AllSpiceEntity, ApiRequest, Committable, Deletable, ReadOnlyEntity

if TYPE_CHECKING:
    from allspice.api_requests import (
        AdminDeleteUserRequest,
        AdminEditUserRequest,
        IssueDeleteCommentRequest,
        IssueEditCommentRequest,
        IssueEditIssueRequest,
        OrgDeleteRequest,
        OrgDeleteTeamRequest,
        OrgEditRequest,
        OrgEditTeamRequest,
        RepoDeleteDesignReviewReviewRequest,
        RepoDeleteReleaseRequest,
        RepoDeleteRequest,
        RepoEditDesignReviewRequest,
        RepoEditReleaseAttachmentRequest,
        RepoEditReleaseRequest,
        RepoEditRequest,
    )
    from allspice.schemas import (
        Attachment,
        Comment,
        DesignReview,
        DesignReviewReview,
        Issue,
        Organization,
        Release,
        Repository,
        Team,
        User,
    )


# --- Mixins: shared entity behavior ---


class HasRepositoryParent(AllSpiceEntity):
    """Mixin for entities whose direct parent is a repository

    Holds that parent repository — readable via `repository`, set by the repo method that fetched
    this resource — and resolves the owner/repo its requests need: from that repository when
    present, otherwise from the path context captured when it was fetched.
    """

    _repository: "Repository | None" = PrivateAttr(default=None)

    @property
    def repository(self) -> "Repository | None":
        return self._repository

    def _owner_repo(self) -> tuple[str, str]:
        """The parent repo's (owner, repo), for filling those params in this resource's requests."""
        if self._repository is not None:
            return self._repository.owner.login, self._repository.name
        ctx = self._path_context
        if "owner" in ctx and "repo" in ctx:
            return ctx["owner"], ctx["repo"]
        raise ValueError(
            "This resource has no repository or path context — fetch it through a client "
            "(a Repository method or client.send(...)) before editing or deleting."
        )

    def _set_parent(self, parent: "AllSpiceEntity") -> None:
        from allspice import schemas as s

        # Fail loudly if wired with the wrong parent type — callers are internal and
        # type-guided, so a mismatch is an entity-layer bug, not bad user input.
        assert isinstance(parent, s.Repository), (
            f"expected Repository parent, got {type(parent).__name__}"
        )
        self._repository = parent


# --- Entities ---


# TODO: All these classes will need convenience methods that the different apiobjects current have to keep their interface the same

class RepositoryEntity(Committable, Deletable):
    @classmethod
    def _patch_request_type(cls) -> type["RepoEditRequest"]:
        from allspice import api_requests as r

        return r.RepoEditRequest

    def _to_patch_request(self) -> "RepoEditRequest":
        from allspice import api_requests as r
        from allspice import schemas as s

        repo = cast("Repository", self)
        return r.RepoEditRequest(
            owner=repo.owner.login,
            repo=repo.name,
            body=s.EditRepoOption(**self._dirty_values()),
        )

    def _to_delete_request(self) -> "RepoDeleteRequest":
        from allspice import api_requests as r

        repo = cast("Repository", self)
        return r.RepoDeleteRequest(owner=repo.owner.login, repo=repo.name)


class ReleaseEntity(Committable, Deletable, HasRepositoryParent):
    def _owned_children(self) -> Iterable["AllSpiceEntity"]:
        return cast("Release", self).assets

    @classmethod
    def _patch_request_type(cls) -> type["RepoEditReleaseRequest"]:
        from allspice import api_requests as r

        return r.RepoEditReleaseRequest

    def _to_patch_request(self) -> "RepoEditReleaseRequest":
        from allspice import api_requests as r
        from allspice import schemas as s

        owner, repo = self._owner_repo()
        return r.RepoEditReleaseRequest(
            owner=owner,
            repo=repo,
            id=cast("Release", self).id,
            body=s.EditReleaseOption(**self._dirty_values()),
        )

    def _to_delete_request(self) -> "RepoDeleteReleaseRequest":
        from allspice import api_requests as r

        owner, repo = self._owner_repo()
        return r.RepoDeleteReleaseRequest(owner=owner, repo=repo, id=cast("Release", self).id)


class AttachmentEntity(Committable, Deletable):
    # One `Attachment` schema backs issue, comment, and release attachments, and the backend routes
    # edit/delete through three different endpoint families by parent. So the entity holds its parent
    # (any of the three entities) and picks the request family from it, falling back to the path
    # context captured at fetch when there's no parent object.
    _parent: "AllSpiceEntity | None" = PrivateAttr(default=None)

    @property
    def issue(self) -> "Issue | None":
        from allspice import schemas as s

        return self._parent if isinstance(self._parent, s.Issue) else None

    @property
    def comment(self) -> "Comment | None":
        from allspice import schemas as s

        return self._parent if isinstance(self._parent, s.Comment) else None

    @property
    def release(self) -> "Release | None":
        from allspice import schemas as s

        return self._parent if isinstance(self._parent, s.Release) else None

    def _set_parent(self, parent: "AllSpiceEntity") -> None:
        from allspice import schemas as s

        assert isinstance(parent, (s.Issue, s.Comment, s.Release)), (
            f"expected Issue, Comment, or Release parent, got {type(parent).__name__}"
        )
        self._parent = parent

    def _route(self) -> tuple[str, str, str, int]:
        """(kind, owner, repo, parent_id) for this attachment's requests — kind is
        'issue'|'comment'|'release'. From the explicit parent when set, else from the path context
        captured at fetch (issue paths carry `index`, release paths carry `attachment_id`, and a
        bare `id` is a comment)."""
        from allspice import schemas as s

        parent = self._parent
        if isinstance(parent, s.Issue):
            owner, repo = parent._owner_repo()
            return "issue", owner, repo, parent.number
        if isinstance(parent, s.Comment):
            owner, repo = parent._owner_repo()
            return "comment", owner, repo, parent.id
        if isinstance(parent, s.Release):
            owner, repo = parent._owner_repo()
            return "release", owner, repo, parent.id
        ctx = self._path_context
        if "owner" in ctx and "repo" in ctx:
            if "index" in ctx:
                return "issue", ctx["owner"], ctx["repo"], ctx["index"]
            if "attachment_id" in ctx:
                return "release", ctx["owner"], ctx["repo"], ctx["id"]
            if "id" in ctx:
                return "comment", ctx["owner"], ctx["repo"], ctx["id"]
        raise ValueError(
            "This attachment has no parent or path context — fetch it through a parent "
            "(issue/comment/release) or client.send(...) before editing or deleting."
        )

    @classmethod
    def _patch_request_type(cls) -> type["RepoEditReleaseAttachmentRequest"]:
        # Only used to derive patchable fields; the three edit requests share EditAttachmentOptions,
        # so any one is representative.
        from allspice import api_requests as r

        return r.RepoEditReleaseAttachmentRequest

    def _to_patch_request(self) -> "ApiRequest":
        from allspice import api_requests as r
        from allspice import schemas as s

        kind, owner, repo, parent_id = self._route()
        aid = cast("Attachment", self).id
        body = s.EditAttachmentOptions(**self._dirty_values())
        if kind == "issue":
            return r.IssueEditIssueAttachmentRequest(
                owner=owner, repo=repo, index=parent_id, attachment_id=aid, body=body
            )
        if kind == "comment":
            return r.IssueEditIssueCommentAttachmentRequest(
                owner=owner, repo=repo, id=parent_id, attachment_id=aid, body=body
            )
        return r.RepoEditReleaseAttachmentRequest(
            owner=owner, repo=repo, id=parent_id, attachment_id=aid, body=body
        )

    def _to_delete_request(self) -> "ApiRequest":
        from allspice import api_requests as r

        kind, owner, repo, parent_id = self._route()
        aid = cast("Attachment", self).id
        if kind == "issue":
            return r.IssueDeleteIssueAttachmentRequest(
                owner=owner, repo=repo, index=parent_id, attachment_id=aid
            )
        if kind == "comment":
            return r.IssueDeleteIssueCommentAttachmentRequest(
                owner=owner, repo=repo, id=parent_id, attachment_id=aid
            )
        return r.RepoDeleteReleaseAttachmentRequest(
            owner=owner, repo=repo, id=parent_id, attachment_id=aid
        )


class OrganizationEntity(Committable, Deletable):
    @classmethod
    def _patch_request_type(cls) -> type["OrgEditRequest"]:
        from allspice import api_requests as r

        return r.OrgEditRequest

    def _to_patch_request(self) -> "OrgEditRequest":
        from allspice import api_requests as r
        from allspice import schemas as s

        org = cast("Organization", self)
        return r.OrgEditRequest(org=org.name, body=s.EditOrgOption(**self._dirty_values()))

    def _to_delete_request(self) -> "OrgDeleteRequest":
        from allspice import api_requests as r

        org = cast("Organization", self)
        return r.OrgDeleteRequest(org=org.name)


class TeamEntity(Committable, Deletable):
    @classmethod
    def _patch_request_type(cls) -> type["OrgEditTeamRequest"]:
        from allspice import api_requests as r

        return r.OrgEditTeamRequest

    def _to_patch_request(self) -> "OrgEditTeamRequest":
        from allspice import api_requests as r
        from allspice import schemas as s

        team = cast("Team", self)
        return r.OrgEditTeamRequest(id=team.id, body=s.EditTeamOption(**self._dirty_values()))

    def _to_delete_request(self) -> "OrgDeleteTeamRequest":
        from allspice import api_requests as r

        team = cast("Team", self)
        return r.OrgDeleteTeamRequest(id=team.id)


class UserEntity(Committable, Deletable):
    """Edit/delete go through the admin user endpoints. Also the entity for nested Users
    (e.g. repo.owner), which receive _client via _attach_client."""

    @classmethod
    def _patch_request_type(cls) -> type["AdminEditUserRequest"]:
        from allspice import api_requests as r

        return r.AdminEditUserRequest

    def _to_patch_request(self) -> "AdminEditUserRequest":
        from allspice import api_requests as r
        from allspice import schemas as s

        user = cast("User", self)
        # adminEditUser requires login_name on every call (Go binding:"Required"), so carry the
        # current value even when it isn't what changed; a dirty login_name wins via setdefault.
        values = self._dirty_values()
        values.setdefault("login_name", user.login_name)
        return r.AdminEditUserRequest(username=user.login, body=s.EditUserOption(**values))

    def _to_delete_request(self) -> "AdminDeleteUserRequest":
        from allspice import api_requests as r

        user = cast("User", self)
        return r.AdminDeleteUserRequest(username=user.login)


class CommentEntity(Committable, Deletable, HasRepositoryParent):
    def _owned_children(self) -> Iterable["AllSpiceEntity"]:
        return cast("Comment", self).assets

    @classmethod
    def _patch_request_type(cls) -> type["IssueEditCommentRequest"]:
        from allspice import api_requests as r

        return r.IssueEditCommentRequest

    def _to_patch_request(self) -> "IssueEditCommentRequest":
        from allspice import api_requests as r
        from allspice import schemas as s

        owner, repo = self._owner_repo()
        return r.IssueEditCommentRequest(
            owner=owner,
            repo=repo,
            id=cast("Comment", self).id,
            body=s.EditIssueCommentOption(**self._dirty_values()),
        )

    def _to_delete_request(self) -> "IssueDeleteCommentRequest":
        from allspice import api_requests as r

        owner, repo = self._owner_repo()
        return r.IssueDeleteCommentRequest(owner=owner, repo=repo, id=cast("Comment", self).id)


class IssueEntity(Committable):
    def _owned_children(self) -> Iterable["AllSpiceEntity"]:
        return cast("Issue", self).assets

    def _owner_repo(self) -> tuple[str, str]:
        """This issue's (owner, repo): from its inline `repository` (RepositoryMeta) when set,
        else the path context captured when it was fetched."""
        issue = cast("Issue", self)
        if issue.repository is not None and issue.repository.owner and issue.repository.name:
            return issue.repository.owner, issue.repository.name
        ctx = self._path_context
        if "owner" in ctx and "repo" in ctx:
            return ctx["owner"], ctx["repo"]
        raise ValueError(
            "This issue has no repository or path context — fetch it through a client "
            "(client.send(...)) before editing."
        )

    @classmethod
    def _patch_request_type(cls) -> type["IssueEditIssueRequest"]:
        from allspice import api_requests as r

        return r.IssueEditIssueRequest

    def _to_patch_request(self) -> "IssueEditIssueRequest":
        from allspice import api_requests as r
        from allspice import schemas as s

        owner, repo = self._owner_repo()
        return r.IssueEditIssueRequest(
            owner=owner,
            repo=repo,
            index=cast("Issue", self).number,
            body=s.EditIssueOption(**self._dirty_values()),
        )


class DesignReviewEntity(Committable, HasRepositoryParent):
    @classmethod
    def _patch_request_type(cls) -> type["RepoEditDesignReviewRequest"]:
        from allspice import api_requests as r

        return r.RepoEditDesignReviewRequest

    def _to_patch_request(self) -> "RepoEditDesignReviewRequest":
        from allspice import api_requests as r
        from allspice import schemas as s

        owner, repo = self._owner_repo()
        return r.RepoEditDesignReviewRequest(
            owner=owner,
            repo=repo,
            index=cast("DesignReview", self).number,
            body=s.EditDesignReviewOption(**self._dirty_values()),
        )


class DesignReviewReviewEntity(Deletable):
    # No inline repo/design-review reference on the model, so owner/repo/index come from the path
    # context captured when the review was fetched; the review id is on the model.

    def _owner_repo_index(self) -> tuple[str, str, int]:
        ctx = self._path_context
        if not ("owner" in ctx and "repo" in ctx and "index" in ctx):
            raise ValueError(
                "This review has no path context — fetch it through a client "
                "(client.send(...)) before acting on it."
            )
        return ctx["owner"], ctx["repo"], ctx["index"]

    def _to_delete_request(self) -> "RepoDeleteDesignReviewReviewRequest":
        from allspice import api_requests as r

        owner, repo, index = self._owner_repo_index()
        return r.RepoDeleteDesignReviewReviewRequest(
            owner=owner, repo=repo, index=index, id=cast("DesignReviewReview", self).id
        )


# TODO: These are read only, but need a client for convenience functions when pulled in
class BranchEntity(ReadOnlyEntity):
    pass


class MilestoneEntity(ReadOnlyEntity):
    pass


class CommitEntity(ReadOnlyEntity, HasRepositoryParent):
    pass
