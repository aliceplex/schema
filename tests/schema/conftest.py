from pytest import fixture

from aliceplex.schema import ActorSchema, ActorStrictSchema, AlbumSchema, \
    AlbumStrictSchema, ArtistSchema, ArtistStrictSchema, EpisodeSchema, \
    EpisodeStrictSchema, MovieSchema, MovieStrictSchema, PersonSchema, \
    PersonStrictSchema, ShowSchema, ShowStrictSchema


@fixture
def actor_schema() -> ActorSchema:
    return ActorSchema()


@fixture
def actor_strict_schema() -> ActorStrictSchema:
    return ActorStrictSchema()


@fixture
def album_schema() -> AlbumSchema:
    return AlbumSchema()


@fixture
def album_strict_schema() -> AlbumStrictSchema:
    return AlbumStrictSchema()


@fixture
def artist_schema() -> ArtistSchema:
    return ArtistSchema()


@fixture
def artist_strict_schema() -> ArtistStrictSchema:
    return ArtistStrictSchema()


@fixture
def episode_schema() -> EpisodeSchema:
    return EpisodeSchema()


@fixture
def episode_strict_schema() -> EpisodeStrictSchema:
    return EpisodeStrictSchema()


@fixture
def movie_schema() -> MovieSchema:
    return MovieSchema()


@fixture
def movie_strict_schema() -> MovieStrictSchema:
    return MovieStrictSchema()


@fixture
def person_schema() -> PersonSchema:
    return PersonSchema()


@fixture
def person_strict_schema() -> PersonStrictSchema:
    return PersonStrictSchema()


@fixture
def show_schema() -> ShowSchema:
    return ShowSchema()


@fixture
def show_strict_schema() -> ShowStrictSchema:
    return ShowStrictSchema()
