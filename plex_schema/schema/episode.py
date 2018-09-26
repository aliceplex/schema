"""
This module provides schema object to convert between common Plex data object
and dictionary.
"""

from marshmallow import fields
from marshmallow.validate import Length, Range

from plex_schema.model import Episode
from plex_schema.patch import PatchDateField
from plex_schema.schema.base import DataClassSchema
from plex_schema.schema.person import PersonSchema, PersonStrictSchema

__all__ = ["EpisodeSchema", "EpisodeStrictSchema"]


class EpisodeSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Episode`
    """

    title = fields.List(fields.Str(allow_none=False), allow_none=False)
    aired = PatchDateField(allow_none=True)
    content_rating = fields.Str(allow_none=True)
    summary = fields.Str(allow_none=True)
    directors = fields.List(
        fields.Nested(PersonSchema, allow_none=False, only="name"),
        allow_none=False
    )
    writers = fields.List(
        fields.Nested(PersonSchema, allow_none=False, only="name"),
        allow_none=False
    )
    rating = fields.Float(validate=Range(min=0, max=10), allow_none=True)

    @property
    def data_class(self) -> type:
        return Episode


class EpisodeStrictSchema(EpisodeSchema):
    """
    Strict schema for :class:`plex_schema.model.Episode`
    """

    title = fields.List(
        fields.Str(allow_none=False),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
    aired = PatchDateField(allow_none=True)
    content_rating = fields.Str(allow_none=False, required=True)
    summary = fields.Str(allow_none=False, required=True)
    directors = fields.List(
        fields.Nested(PersonStrictSchema, allow_none=False, only="name"),
        allow_none=False,
        required=True
    )
    writers = fields.List(
        fields.Nested(PersonStrictSchema, allow_none=False, only="name"),
        allow_none=False,
        required=True
    )
    rating = fields.Float(validate=Range(min=0, max=10), allow_none=True)
