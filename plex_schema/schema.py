"""
This module provides schema object to convert between common Plex data object
and dictionary.
"""

from dataclasses import asdict, is_dataclass
from typing import Any, Dict

from marshmallow import Schema, fields, post_load, pre_dump

from plex_schema.model import Actor, Episode, Movie, Show

__all__ = ["ActorSchema", "ShowSchema", "EpisodeSchema", "MovieSchema"]


class DataClassSchema(Schema):
    """
    Base schema class for dataclass. It implements simple dump and load.
    """

    # pylint: disable=R0201
    @pre_dump
    def pre_dump(self, data) -> Dict[str, Any]:
        """
        Convert dataclass object to dict.

        :param data: Input data
        :type data: Any
        :return: Dictionary for dumping.
        :rtype: Dict[str, Any]
        """
        if is_dataclass(data):
            return asdict(data)
        return data

    @post_load
    def post_load(self, data) -> Any:
        """
        Convert dict to dataclass object

        :param data: Input data
        :type data: Dict[str, Any]
        :return: Dataclass
        :rtype: Any
        """
        data_class = self.data_class
        return data_class(**data)

    @property
    def data_class(self) -> type:
        """
        Provide the dataclass of this schema.

        :return: Dataclass
        :rtype: type
        """
        raise NotImplementedError()


class ActorSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Actor`
    """

    name = fields.Str()
    role = fields.Str()
    photo = fields.Str()

    @property
    def data_class(self) -> type:
        return Actor


class ShowSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Show`
    """

    title = fields.Str()
    sort_title = fields.Str()
    original_title = fields.Str()
    content_rating = fields.Str()
    tagline = fields.Str()
    studio = fields.Str()
    aired = fields.Date()
    summary = fields.Str()
    rating = fields.Float()
    genres = fields.List(fields.Str(allow_none=False))
    collections = fields.List(fields.Str(allow_none=False))
    actors = fields.List(fields.Nested(ActorSchema, allow_none=False))

    @property
    def data_class(self) -> type:
        return Show


class EpisodeSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Episode`
    """

    title = fields.Str()
    episode = fields.Int()
    aired = fields.Date()
    content_rating = fields.Str()
    summary = fields.Str()
    directors = fields.List(fields.Str(allow_none=False))
    writers = fields.List(fields.Str(allow_none=False))
    rating = fields.Float()

    @property
    def data_class(self) -> type:
        return Episode


class MovieSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Movie`
    """

    title = fields.Str()
    sort_title = fields.Str()
    original_title = fields.Str()
    content_rating = fields.Str()
    tagline = fields.Str()
    studio = fields.Str()
    aired = fields.Date()
    summary = fields.Str()
    rating = fields.Float()
    genres = fields.List(fields.Str(allow_none=False))
    collections = fields.List(fields.Str(allow_none=False))
    actors = fields.List(fields.Nested(ActorSchema, allow_none=False))
    writers = fields.List(fields.Str(allow_none=False))
    directors = fields.List(fields.Str(allow_none=False))

    @property
    def data_class(self) -> type:
        return Movie
