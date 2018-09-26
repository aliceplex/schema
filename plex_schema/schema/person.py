from marshmallow import fields

from plex_schema.model import Person
from plex_schema.schema.base import DataClassSchema

__all__ = ["PersonSchema", "PersonStrictSchema"]


class PersonSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Person`
    """

    name = fields.Str(allow_none=True)
    photo = fields.Str(allow_none=True)

    @property
    def data_class(self) -> type:
        return Person


class PersonStrictSchema(PersonSchema):
    """
    Strict schema for :class:`plex_schema.model.Person`
    """

    name = fields.Str(allow_none=False, required=True)
    photo = fields.Str(allow_none=True)
