"""
This module provides schema object to convert between common Plex data object
and dictionary.
"""

from marshmallow import fields
from marshmallow.validate import Length, Range

from plex_schema.model import Movie
from plex_schema.patch import PatchDateField
from plex_schema.schema.actor import ActorSchema
from plex_schema.schema.base import DataClassSchema
from plex_schema.schema.person import PersonSchema, PersonStrictSchema

__all__ = ["MovieSchema", "MovieStrictSchema"]


class MovieSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Movie`
    """

    title = fields.Str(allow_none=True)
    sort_title = fields.Str(allow_none=True)
    original_title = fields.Str(allow_none=True)
    content_rating = fields.Str(allow_none=True)
    tagline = fields.List(fields.Str(allow_none=False), allow_none=False)
    studio = fields.List(fields.Str(allow_none=False), allow_none=False)
    aired = PatchDateField(allow_none=True)
    summary = fields.Str(allow_none=True)
    rating = fields.Float(validate=Range(min=0, max=10), allow_none=True)
    genres = fields.List(fields.Str(allow_none=False), allow_none=False)
    collections = fields.List(fields.Str(allow_none=False), allow_none=False)
    actors = fields.List(
        fields.Nested(ActorSchema, allow_none=False),
        allow_none=False
    )
    writers = fields.List(
        fields.Nested(PersonSchema, allow_none=False, only="name"),
        allow_none=False
    )
    directors = fields.List(
        fields.Nested(PersonSchema, allow_none=False, only="name"),
        allow_none=False
    )

    @property
    def data_class(self) -> type:
        return Movie


class MovieStrictSchema(MovieSchema):
    """
    Strict schema for :class:`plex_schema.model.Movie`
    """

    title = fields.Str(allow_none=False, required=True)
    sort_title = fields.Str(allow_none=False, required=True)
    original_title = fields.Str(allow_none=False, required=True)
    content_rating = fields.Str(allow_none=False, required=True)
    tagline = fields.List(
        fields.Str(allow_none=False),
        allow_none=False,
        required=True
    )
    studio = fields.List(
        fields.Str(allow_none=False),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
    aired = PatchDateField(allow_none=False, required=True)
    summary = fields.Str(allow_none=False, required=True)
    rating = fields.Float(validate=Range(min=0, max=10), allow_none=False)
    genres = fields.List(
        fields.Str(allow_none=False),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
    collections = fields.List(
        fields.Str(allow_none=False),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
    actors = fields.List(
        fields.Nested(ActorSchema, allow_none=False),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
    writers = fields.List(
        fields.Nested(PersonStrictSchema, allow_none=False, only="name"),
        allow_none=False,
        required=True
    )
    directors = fields.List(
        fields.Nested(PersonStrictSchema, allow_none=False, only="name"),
        allow_none=False,
        required=True
    )
