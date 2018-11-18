from datetime import date

import pytest
from marshmallow import ValidationError

from plex_schema import Actor, Movie, MovieSchema, MovieStrictSchema, Person


def test_movie_schema_load(movie_schema: MovieSchema):
    schema = movie_schema
    load = schema.load({
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": ["tagline"],
        "studio": ["studio"],
        "aired": "2018-01-01",
        "summary": "summary",
        "rating": 1,
        "genres": ["genres"],
        "collections": ["collections"],
        "actors": [{
            "name": "name",
            "role": "role"
        }],
        "writers": ["person"],
        "directors": ["person"]
    })
    assert load == Movie(
        title="title",
        sort_title="sort_title",
        original_title="original_title",
        content_rating="content_rating",
        tagline=["tagline"],
        studio=["studio"],
        aired=date(2018, 1, 1),
        summary="summary",
        rating=1,
        genres=["genres"],
        collections=["collections"],
        actors=[Actor(name="name", role="role")],
        writers=[Person(name="person")],
        directors=[Person(name="person")]
    )
    load = schema.load({
        "title": "",
        "sort_title": "",
        "original_title": None,
        "content_rating": "",
        "tagline": [""],
        "studio": [None],
        "aired": None,
        "summary": None,
        "rating": None,
        "genres": [],
        "collections": None,
        "actors": [],
        "writers": [""],
        "directors": None
    })
    assert load == Movie()
    load = schema.load({})
    assert load == Movie()


def test_movie_schema_dump(movie_schema: MovieSchema):
    schema = movie_schema
    dump = schema.dump(Movie(
        title="title",
        sort_title="sort_title",
        original_title="original_title",
        content_rating="content_rating",
        tagline=["tagline"],
        studio=["studio"],
        aired=date(2018, 1, 1),
        summary="summary",
        rating=1,
        genres=["genres"],
        collections=["collections"],
        actors=[Actor(name="name", role="role")],
        writers=[Person(name="person")],
        directors=[Person(name="person")]
    ))
    assert dump == {
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": ["tagline"],
        "studio": ["studio"],
        "aired": "2018-01-01",
        "summary": "summary",
        "rating": 1,
        "genres": ["genres"],
        "collections": ["collections"],
        "actors": [{
            "name": "name",
            "role": "role",
            "photo": None
        }],
        "writers": ["person"],
        "directors": ["person"]
    }
    dump = schema.dump(Movie())
    assert dump == {
        "title": None,
        "sort_title": None,
        "original_title": None,
        "content_rating": None,
        "tagline": [],
        "studio": [],
        "aired": None,
        "summary": None,
        "rating": None,
        "genres": [],
        "collections": [],
        "actors": [],
        "writers": [],
        "directors": []
    }


def test_movie_strict_schema_load(movie_strict_schema: MovieStrictSchema):
    schema = movie_strict_schema
    load = schema.load({
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": ["tagline"],
        "studio": ["studio"],
        "aired": "2018-01-01",
        "summary": "summary",
        "rating": 1,
        "genres": ["genres"],
        "collections": ["collections"],
        "actors": [{
            "name": "name",
            "role": "role"
        }],
        "writers": ["person"],
        "directors": ["person"]
    })
    assert load == Movie(
        title="title",
        sort_title="sort_title",
        original_title="original_title",
        content_rating="content_rating",
        tagline=["tagline"],
        studio=["studio"],
        aired=date(2018, 1, 1),
        summary="summary",
        rating=1,
        genres=["genres"],
        collections=["collections"],
        actors=[Actor(name="name", role="role")],
        writers=[Person(name="person")],
        directors=[Person(name="person")]
    )
    with pytest.raises(ValidationError):
        schema.load({
            "title": None,
            "sort_title": None,
            "original_title": None,
            "content_rating": None,
            "tagline": None,
            "studio": None,
            "aired": None,
            "summary": None,
            "rating": None,
            "genres": None,
            "collections": None,
            "actors": None,
            "writers": None,
            "directors": None
        })
    with pytest.raises(ValidationError):
        schema.load({})


def test_movie_strict_schema_dump(movie_strict_schema: MovieStrictSchema):
    schema = movie_strict_schema
    dump = schema.dump(Movie(
        title="title",
        sort_title="sort_title",
        original_title="original_title",
        content_rating="content_rating",
        tagline=["tagline"],
        studio=["studio"],
        aired=date(2018, 1, 1),
        summary="summary",
        rating=1,
        genres=["genres"],
        collections=["collections"],
        actors=[Actor(name="name", role="role")],
        writers=[Person(name="person")],
        directors=[Person(name="person")]
    ))
    assert dump == {
        "title": "title",
        "sort_title": "sort_title",
        "original_title": "original_title",
        "content_rating": "content_rating",
        "tagline": ["tagline"],
        "studio": ["studio"],
        "aired": "2018-01-01",
        "summary": "summary",
        "rating": 1,
        "genres": ["genres"],
        "collections": ["collections"],
        "actors": [{
            "name": "name",
            "role": "role",
            "photo": None
        }],
        "writers": ["person"],
        "directors": ["person"]
    }
    dump = schema.dump(Movie())
    assert dump == {
        "title": None,
        "sort_title": None,
        "original_title": None,
        "content_rating": None,
        "tagline": [],
        "studio": [],
        "aired": None,
        "summary": None,
        "rating": None,
        "genres": [],
        "collections": [],
        "actors": [],
        "writers": [],
        "directors": []
    }
