from marshmallow import ValidationError
from pytest import raises

from plex_schema import Actor, ActorSchema, ActorStrictSchema, Album, \
    AlbumSchema, Artist, ArtistSchema, Episode, EpisodeSchema, \
    EpisodeStrictSchema, Movie, MovieSchema, \
    MovieStrictSchema, Show, ShowSchema, ShowStrictSchema


def test_actor_schema_load(actor_schema: ActorSchema, actor: Actor):
    load_actor = actor_schema.load({
        "name": "name",
        "role": "role",
        "photo": "photo",
        "extra": "extra"
    })

    assert load_actor == actor


def test_actor_schema_dump(actor_schema: ActorSchema, actor: Actor):
    dump_actor = actor_schema.dump(actor)
    dict_actor = {
        "name": "name",
        "role": "role",
        "photo": "photo"
    }
    assert dump_actor == dict_actor


def test_actor_schema_load_error(actor_schema: ActorSchema):
    with raises(ValidationError):
        actor_schema.load({
            "name": 1,
            "role": 2,
            "photo": {}
        })


def test_show_schema_load(show_schema: ShowSchema, show: Show,
                          dummy_date_str: str):
    load_show = show_schema.load({
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": "tagline",
        "studio": "studio",
        "aired": dummy_date_str,
        "summary": "summary",
        "rating": 1,
        "genres": ["genres"],
        "collections": ["collections"],
        "actors": [{
            "name": "name",
            "role": "role",
            "photo": "photo"
        }]
    })

    assert load_show == show


def test_show_schema_dump(show_schema: ShowSchema, show: Show,
                          dummy_date_str: str):
    dump_show = show_schema.dump(show)
    dict_show = {
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": "tagline",
        "studio": "studio",
        "aired": dummy_date_str,
        "summary": "summary",
        "rating": 1,
        "genres": ["genres"],
        "collections": ["collections"],
        "actors": [{
            "name": "name",
            "role": "role",
            "photo": "photo"
        }]
    }
    assert dump_show == dict_show


def test_show_schema_load_error(show_schema: ShowSchema):
    with raises(ValidationError):
        show_schema.load({
            "rating": 1,
            "genres": [1],
            "collections": [2],
            "actors": [None]
        })


def test_episode_schema_load(episode_schema: EpisodeSchema, episode: Episode,
                             dummy_date_str: str):
    load_episode = episode_schema.load({
        "title": "title",
        "episode": 1,
        "content_rating": "content_rating",
        "aired": dummy_date_str,
        "summary": "summary",
        "rating": 1,
        "writers": ["writers"],
        "directors": ["directors"]
    })

    assert load_episode == episode


def test_episode_schema_dump(episode_schema: EpisodeSchema, episode: Episode,
                             dummy_date_str: str):
    dump_episode = episode_schema.dump(episode)
    dict_episode = {
        "title": "title",
        "episode": 1,
        "content_rating": "content_rating",
        "aired": dummy_date_str,
        "summary": "summary",
        "rating": 1,
        "writers": ["writers"],
        "directors": ["directors"]
    }
    assert dump_episode == dict_episode


def test_episode_schema_load_error(episode_schema: EpisodeSchema):
    with raises(ValidationError):
        episode_schema.load({
            "title": "title",
            "episode": "",
        })


def test_movie_schema_load(movie_schema: MovieSchema, movie: Movie,
                           dummy_date_str: str):
    load_movie = movie_schema.load({
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": "tagline",
        "studio": "studio",
        "aired": dummy_date_str,
        "summary": "summary",
        "rating": 1,
        "genres": ["genres"],
        "collections": ["collections"],
        "actors": [{
            "name": "name",
            "role": "role",
            "photo": "photo"
        }],
        "writers": ["writers"],
        "directors": ["directors"]
    })

    assert load_movie == movie


def test_movie_schema_dump(movie_schema: MovieSchema, movie: Movie,
                           dummy_date_str: str):
    dump_movie = movie_schema.dump(movie)
    dict_movie = {
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": "tagline",
        "studio": "studio",
        "aired": dummy_date_str,
        "summary": "summary",
        "rating": 1,
        "genres": ["genres"],
        "collections": ["collections"],
        "actors": [{
            "name": "name",
            "role": "role",
            "photo": "photo"
        }],
        "writers": ["writers"],
        "directors": ["directors"]
    }
    assert dump_movie == dict_movie


def test_movie_schema_load_error(movie_schema: MovieSchema):
    with raises(ValidationError):
        movie_schema.load({
            "rating": 1,
            "genres": [1],
            "collections": [2],
            "actors": [None]
        })


def test_artist_schema_load(artist_schema: ArtistSchema, artist: Artist):
    load_artist = artist_schema.load({
        "name": "name",
        "summary": "summary",
        "genres": ["genres"],
        "collections": ["collections"],
        "similar": ["similar"]
    })

    assert load_artist == artist


def test_artist_schema_dump(artist_schema: ArtistSchema, artist: Artist):
    dump_artist = artist_schema.dump(artist)
    dict_artist = {
        "name": "name",
        "summary": "summary",
        "genres": ["genres"],
        "collections": ["collections"],
        "similar": ["similar"]
    }
    assert dump_artist == dict_artist


def test_artist_schema_load_error(artist_schema: ArtistSchema):
    with raises(ValidationError):
        artist_schema.load({
            "name": "name",
            "summary": "summary",
            "genres": ["genres"],
            "collections": [None],
            "similar": [None]
        })


def test_album_schema_load(album_schema: AlbumSchema, album: Album,
                           dummy_date_str: str):
    load_album = album_schema.load({
            "name": "name",
            "summary": "summary",
            "genres": ["genres"],
            "collections": ["collections"],
            "aired": dummy_date_str
        })

    assert load_album == album


def test_album_schema_dump(album_schema: AlbumSchema, album: Album,
                           dummy_date_str: str):
    dump_album = album_schema.dump(album)
    dict_album = {
            "name": "name",
            "summary": "summary",
            "genres": ["genres"],
            "collections": ["collections"],
            "aired": dummy_date_str
        }
    assert dump_album == dict_album


def test_album_schema_load_error(album_schema: AlbumSchema):
    with raises(ValidationError):
        album_schema.load({
            "name": "name",
            "genres": [None],
            "collections": [None]
        })


def test_actor_strict_schema(actor_strict_schema: ActorStrictSchema):
    with raises(ValidationError):
        actor_strict_schema.load({})
    actor = Actor()
    with raises(ValidationError):
        actor_strict_schema.load(actor)


def test_show_strict_schema(show_strict_schema: ShowStrictSchema):
    with raises(ValidationError):
        show_strict_schema.load({})
    show = Show()
    with raises(ValidationError):
        show_strict_schema.load(show)


def test_episode_strict_schema(episode_strict_schema: EpisodeStrictSchema):
    with raises(ValidationError):
        episode_strict_schema.load({})
    episode = Episode()
    with raises(ValidationError):
        episode_strict_schema.load(episode)


def test_movie_strict_schema(movie_strict_schema: MovieStrictSchema):
    with raises(ValidationError):
        movie_strict_schema.load({})
    movie = Movie()
    with raises(ValidationError):
        movie_strict_schema.load(movie)
