"""
This module provides schema object to convert between common Plex data object
and dictionary.
"""

from dataclasses import asdict, is_dataclass
from typing import Any, Dict

from marshmallow import Schema, fields, post_load, pre_dump, pre_load
from marshmallow.validate import Length, Range

from .model import Actor, Album, Artist, Episode, Movie, Person, Show
from .patch import PatchDateField

__all__ = ["ActorSchema", "ShowSchema", "EpisodeSchema", "MovieSchema",
           "ActorStrictSchema", "EpisodeStrictSchema", "MovieStrictSchema",
           "ShowStrictSchema", "ArtistSchema", "ArtistStrictSchema",
           "AlbumSchema", "AlbumStrictSchema", "PersonSchema",
           "PersonStrictSchema"]


class DataClassSchema(Schema):
    """
    Base schema class for dataclass. It implements simple dump and load.
    """

    # pylint: disable=R0201
    @pre_load
    @pre_dump
    def convert(self, data) -> Dict[str, Any]:
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


class PersonSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Person`
    """

    name = fields.Str()
    photo = fields.Str()

    @property
    def data_class(self) -> type:
        return Person


class ActorSchema(PersonSchema):
    """
    Schema for :class:`plex_schema.model.Actor`
    """

    role = fields.Str()

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
    tagline = fields.List(fields.Str(allow_none=False), allow_none=False)
    studio = fields.List(fields.Str(allow_none=False), allow_none=False)
    aired = PatchDateField()
    summary = fields.Str()
    rating = fields.Float(allow_none=True)
    genres = fields.List(fields.Str(allow_none=False), allow_none=False)
    collections = fields.List(fields.Str(allow_none=False), allow_none=False)
    actors = fields.List(
        fields.Nested(ActorSchema, allow_none=False, only=["name", "role"]),
        allow_none=False
    )
    season_summary = fields.Dict(keys=fields.Int(), values=fields.Str())

    @property
    def data_class(self) -> type:
        return Show


class EpisodeSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Episode`
    """

    title = fields.List(fields.Str(allow_none=False), allow_none=False)
    episode = fields.Int()
    aired = PatchDateField()
    content_rating = fields.Str()
    summary = fields.Str()
    directors = fields.List(
        fields.Nested(PersonSchema, allow_none=False, only="name"),
        allow_none=False
    )
    writers = fields.List(
        fields.Nested(PersonSchema, allow_none=False, only="name"),
        allow_none=False
    )
    rating = fields.Float(allow_none=True)

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
    tagline = fields.List(fields.Str(allow_none=False), allow_none=False)
    studio = fields.List(fields.Str(allow_none=False), allow_none=False)
    aired = PatchDateField()
    summary = fields.Str()
    rating = fields.Float(allow_none=True)
    genres = fields.List(fields.Str(allow_none=False), allow_none=False)
    collections = fields.List(fields.Str(allow_none=False), allow_none=False)
    actors = fields.List(
        fields.Nested(ActorSchema, allow_none=False, only=["name", "role"]),
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


class ArtistSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Artist`
    """

    summary = fields.Str()
    similar = fields.List(fields.Str(allow_none=False), allow_none=False)
    genres = fields.List(fields.Str(allow_none=False), allow_none=False)
    collections = fields.List(fields.Str(allow_none=False), allow_none=False)

    @property
    def data_class(self) -> type:
        return Artist


class AlbumSchema(DataClassSchema):
    """
    Schema for :class:`plex_schema.model.Album`
    """

    summary = fields.Str()
    aired = PatchDateField()
    genres = fields.List(fields.Str(allow_none=False), allow_none=False)
    collections = fields.List(fields.Str(allow_none=False), allow_none=False)

    @property
    def data_class(self) -> type:
        return Album


class PersonStrictSchema(ActorSchema):
    """
    Strict schema for :class:`plex_schema.model.Person`
    """

    name = fields.Str(allow_none=False, required=True)
    photo = fields.Str(allow_none=False, required=True)


class ActorStrictSchema(PersonStrictSchema):
    """
    Strict schema for :class:`plex_schema.model.Actor`
    """

    role = fields.Str(allow_none=False, required=True)


class ShowStrictSchema(ShowSchema):
    """
    Strict schema for :class:`plex_schema.model.Show`
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
    rating = fields.Float(validate=Range(min=0, max=10), allow_none=True)
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
        fields.Nested(ActorSchema, allow_none=False, only=["name", "role"]),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
    season_summary = fields.Dict(keys=fields.Int(),
                                 values=fields.Str(),
                                 allow_none=False,
                                 required=True)


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
    episode = fields.Int(validate=Range(min=1),
                         allow_none=False,
                         required=True)
    aired = PatchDateField(allow_none=True)
    content_rating = fields.Str(allow_none=False, required=True)
    summary = fields.Str(allow_none=False, required=True)
    directors = fields.List(
        fields.Nested(PersonStrictSchema, allow_none=False, only="name"),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
    writers = fields.List(
        fields.Nested(PersonStrictSchema, allow_none=False, only="name"),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
    rating = fields.Float(validate=Range(min=0, max=10), allow_none=True)


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
    rating = fields.Float(validate=Range(min=0, max=10))
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
        fields.Nested(ActorSchema, allow_none=False, only=["name", "role"]),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
    writers = fields.List(
        fields.Nested(PersonStrictSchema, allow_none=False, only="name"),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
    directors = fields.List(
        fields.Nested(PersonStrictSchema, allow_none=False, only="name"),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )


class ArtistStrictSchema(ArtistSchema):
    """
    Strict schema for :class:`plex_schema.model.Artist`
    """

    summary = fields.Str(allow_none=False, required=True)
    similar = fields.List(fields.Str(allow_none=False), allow_none=False)
    genres = fields.List(fields.Str(allow_none=False), validate=Length(min=1))
    collections = fields.List(
        fields.Str(allow_none=False),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )


class AlbumStrictSchema(AlbumSchema):
    """
    Strict schema for :class:`plex_schema.model.Album`
    """

    summary = fields.Str(allow_none=False, required=True)
    aired = PatchDateField(allow_none=False, required=True)
    genres = fields.List(fields.Str(allow_none=False), validate=Length(min=1))
    collections = fields.List(
        fields.Str(allow_none=False),
        validate=Length(min=1),
        allow_none=False,
        required=True
    )
