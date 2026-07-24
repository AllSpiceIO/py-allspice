"""Stand-in for py-allspice's real allspice.entities module, used by the entity-base test. It
mirrors how the generated schemas will import their entity classes — pulling AllSpiceEntity out of
the real base; tests can swap its allspice.entities import to this module."""

from allspice.base import AllSpiceEntity


class SampleUserEntity(AllSpiceEntity):
    pass
