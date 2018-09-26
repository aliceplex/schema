"""
This module provides schema object to convert between common Plex data object
and dictionary.
"""

from marshmallow import fields
from marshmallow.validate import Length

from plex_schema.model import Album
from plex_schema.patch import PatchDateField
from plex_schema.schema.base import DataClassSchema

__all__ = ["AlbumSchema", "AlbumStrictSchema"]


class AlbumSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Album`
    """

    summary = fields.Str(allow_none=True)
    aired = PatchDateField(allow_none=True)
    genres = fields.List(fields.Str(allow_none=True), allow_none=True)
    collections = fields.List(fields.Str(allow_none=True), allow_none=True)

    @property
    def data_class(self) -> type:
        return Album


class AlbumStrictSchema(AlbumSchema):
    """
    Strict schema for :class:`plex_schema.model.Album`
    """

    summary = fields.Str(allow_none=False, required=True)
    aired = PatchDateField(allow_none=False, required=True)
    genres = fields.List(
        fields.Str(allow_none=False),
        validate=Length(min=1),
        allow_none=False,
        required=True)
    collections = fields.List(
        fields.Str(allow_none=False),
        allow_none=False,
        required=True
    )
