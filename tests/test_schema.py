from datetime import datetime

from marshmallow import ValidationError
from pytest import raises

from plex_schema.model import Actor, Episode, Movie, Show
from plex_schema.schema import ActorSchema, EpisodeSchema, MovieSchema, ShowSchema

actor_schema = ActorSchema()
show_schema = ShowSchema()
movie_schema = MovieSchema()
episode_schema = EpisodeSchema()

date = datetime(2018, 1, 2).date()
date_str = "2018-01-02"


def test_actor_schema_load():
    actor = Actor(name="name", role="role", photo="photo")
    load_actor = actor_schema.load({
        "name": "name",
        "role": "role",
        "photo": "photo",
        "extra": "extra"
    })

    assert load_actor == actor


def test_actor_schema_dump():
    actor = Actor(name="name", role="role", photo="photo")
    dump_actor = actor_schema.dump(actor)
    dict_actor = {
        "name": "name",
        "role": "role",
        "photo": "photo"
    }
    assert dump_actor == dict_actor


def test_actor_schema_load_error():
    with raises(ValidationError):
        actor_schema.load({
            "name": 1,
            "role": 2,
            "photo": {}
        })


def test_show_schema_load():
    actor = Actor(name="name", role="role", photo="photo")
    show = Show(
        title="title",
        sort_title="sort_title",
        original_title="original_title",
        content_rating="content_rating",
        tagline="tagline",
        studio="studio",
        aired=date,
        summary="summary",
        rating=1,
        genres=["genres"],
        collections=["collections"],
        actors=[actor]
    )
    load_show = show_schema.load({
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": "tagline",
        "studio": "studio",
        "aired": date_str,
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


def test_show_schema_dump():
    actor = Actor(name="name", role="role", photo="photo")
    show = Show(
        title="title",
        sort_title="sort_title",
        original_title="original_title",
        content_rating="content_rating",
        tagline="tagline",
        studio="studio",
        aired=date,
        summary="summary",
        rating=1,
        genres=["genres"],
        collections=["collections"],
        actors=[actor]
    )
    dump_show = show_schema.dump(show)
    dict_show = {
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": "tagline",
        "studio": "studio",
        "aired": date_str,
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


def test_show_schema_load_error():
    with raises(ValidationError):
        show_schema.load({
            "rating": 1,
            "genres": [1],
            "collections": [2],
            "actors": [None]
        })


def test_episode_schema_load():
    episode = Episode(
        title="title",
        episode=1,
        content_rating="content_rating",
        aired=date,
        summary="summary",
        rating=1,
        writers=["writers"],
        directors=["directors"]
    )
    load_episode = episode_schema.load({
        "title": "title",
        "episode": 1,
        "content_rating": "content_rating",
        "aired": date_str,
        "summary": "summary",
        "rating": 1,
        "writers": ["writers"],
        "directors": ["directors"]
    })

    assert load_episode == episode


def test_episode_schema_dump():
    episode = Episode(
        title="title",
        episode=1,
        content_rating="content_rating",
        aired=date,
        summary="summary",
        rating=1,
        writers=["writers"],
        directors=["directors"]
    )
    dump_episode = episode_schema.dump(episode)
    dict_episode = {
        "title": "title",
        "episode": 1,
        "content_rating": "content_rating",
        "aired": date_str,
        "summary": "summary",
        "rating": 1,
        "writers": ["writers"],
        "directors": ["directors"]
    }
    assert dump_episode == dict_episode


def test_episode_schema_load_error():
    with raises(ValidationError):
        episode_schema.load({
            "title": "title",
            "episode": "",
        })


def test_movie_schema_load():
    actor = Actor(name="name", role="role", photo="photo")
    movie = Movie(
        title="title",
        sort_title="sort_title",
        original_title="original_title",
        content_rating="content_rating",
        tagline="tagline",
        studio="studio",
        aired=date,
        summary="summary",
        rating=1,
        genres=["genres"],
        collections=["collections"],
        actors=[actor],
        writers=["writers"],
        directors=["directors"]
    )
    load_movie = movie_schema.load({
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": "tagline",
        "studio": "studio",
        "aired": date_str,
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


def test_movie_schema_dump():
    actor = Actor(name="name", role="role", photo="photo")
    movie = Movie(
        title="title",
        sort_title="sort_title",
        original_title="original_title",
        content_rating="content_rating",
        tagline="tagline",
        studio="studio",
        aired=date,
        summary="summary",
        rating=1,
        genres=["genres"],
        collections=["collections"],
        actors=[actor],
        writers=["writers"],
        directors=["directors"]
    )
    dump_movie = movie_schema.dump(movie)
    dict_movie = {
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": "tagline",
        "studio": "studio",
        "aired": date_str,
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


def test_movie_schema_load_error():
    with raises(ValidationError):
        movie_schema.load({
            "rating": 1,
            "genres": [1],
            "collections": [2],
            "actors": [None]
        })
