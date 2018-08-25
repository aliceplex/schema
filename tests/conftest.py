from datetime import date

from pytest import fixture

from plex_schema import Actor, ActorSchema, ActorStrictSchema, Album, \
    AlbumSchema, AlbumStrictSchema, Artist, ArtistSchema, ArtistStrictSchema, \
    Episode, EpisodeSchema, EpisodeStrictSchema, Movie, MovieSchema, \
    MovieStrictSchema, Show, ShowSchema, ShowStrictSchema


@fixture
def actor() -> Actor:
    return Actor(name="name", role="role", photo="photo")


@fixture
def show(actor: Actor, dummy_date: date) -> Show:
    return Show(
        title="title",
        sort_title="sort_title",
        original_title="original_title",
        content_rating="content_rating",
        tagline="tagline",
        studio="studio",
        aired=dummy_date,
        summary="summary",
        rating=1,
        genres=["genres"],
        collections=["collections"],
        actors=[actor]
    )


@fixture
def episode(dummy_date: date) -> Episode:
    return Episode(
        title="title",
        episode=1,
        content_rating="content_rating",
        aired=dummy_date,
        summary="summary",
        rating=1,
        writers=["writers"],
        directors=["directors"]
    )


@fixture
def movie(actor: Actor, dummy_date: date) -> Movie:
    return Movie(
        title="title",
        sort_title="sort_title",
        original_title="original_title",
        content_rating="content_rating",
        tagline="tagline",
        studio="studio",
        aired=dummy_date,
        summary="summary",
        rating=1,
        genres=["genres"],
        collections=["collections"],
        actors=[actor],
        writers=["writers"],
        directors=["directors"]
    )


@fixture
def artist(actor: Actor, dummy_date: date) -> Artist:
    return Artist(
        name="name",
        summary="summary",
        collections=["collections"],
        genres=["genres"],
        similar=["similar"]
    )


@fixture
def album(actor: Actor, dummy_date: date) -> Album:
    return Album(
        name="name",
        aired=dummy_date,
        collections=["collections"],
        genres=["genres"],
        summary="summary",
    )


@fixture
def dummy_date() -> date:
    return date(2018, 1, 2)


@fixture
def dummy_date_str() -> str:
    return "2018-01-02"


@fixture
def actor_schema() -> ActorSchema:
    return ActorSchema()


@fixture
def show_schema() -> ShowSchema:
    return ShowSchema()


@fixture
def movie_schema() -> MovieSchema:
    return MovieSchema()


@fixture
def episode_schema() -> EpisodeSchema:
    return EpisodeSchema()


@fixture
def artist_schema() -> ArtistSchema:
    return ArtistSchema()


@fixture
def album_schema() -> AlbumSchema:
    return AlbumSchema()


@fixture
def actor_strict_schema() -> ActorStrictSchema:
    return ActorStrictSchema()


@fixture
def show_strict_schema() -> ShowStrictSchema:
    return ShowStrictSchema()


@fixture
def movie_strict_schema() -> MovieStrictSchema:
    return MovieStrictSchema()


@fixture
def episode_strict_schema() -> EpisodeStrictSchema:
    return EpisodeStrictSchema()


@fixture
def artist_strict_schema() -> ArtistStrictSchema:
    return ArtistStrictSchema()


@fixture
def album_strict_schema() -> AlbumStrictSchema:
    return AlbumStrictSchema()
