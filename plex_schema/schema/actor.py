from marshmallow import fields

from plex_schema.model import Actor
from plex_schema.schema.person import PersonSchema

__all__ = ["ActorSchema", "ActorStrictSchema"]


class ActorSchema(PersonSchema):
    """
    Schema for :class:`plex_schema.model.Actor`
    """

    role = fields.Str(allow_none=True)

    @property
    def data_class(self) -> type:
        return Actor


class ActorStrictSchema(ActorSchema):
    """
    Strict schema for :class:`plex_schema.model.Actor`
    """

    name = fields.Str(allow_none=False, required=True)
    photo = fields.Str(allow_none=True)
    role = fields.Str(allow_none=False, required=True)
