from datetime import date

import pytest
from marshmallow import ValidationError

from plex_schema import Episode, EpisodeSchema, EpisodeStrictSchema, Person


def test_episode_schema_load(episode_schema: EpisodeSchema):
    schema = episode_schema
    load = schema.load({
        "title": ["title"],
        "content_rating": "content_rating",
        "aired": "2018-01-01",
        "summary": "summary",
        "rating": 1,
        "writers": ["person"],
        "directors": ["person"]
    })
    assert load == Episode(
        title=["title"],
        content_rating="content_rating",
        aired=date(2018, 1, 1),
        summary="summary",
        rating=1,
        writers=[Person(name="person")],
        directors=[Person(name="person")]
    )
    load = schema.load({
        "title": [],
        "content_rating": None,
        "aired": None,
        "summary": "",
        "rating": None,
        "writers": [None],
        "directors": [""]
    })
    assert load == Episode()
    load = schema.load({
        "title": None,
        "content_rating": None,
        "aired": None,
        "summary": None,
        "rating": None,
        "writers": None,
        "directors": None
    })
    assert load == Episode()
    load = schema.load({})
    assert load == Episode()


def test_episode_schema_dump(episode_schema: EpisodeSchema):
    schema = episode_schema
    dump = schema.dump(Episode(
        title=["title"],
        content_rating="content_rating",
        aired=date(2018, 1, 1),
        summary="summary",
        rating=1,
        writers=[Person(name="person")],
        directors=[Person(name="person")]
    ))
    assert dump == {
        "title": ["title"],
        "content_rating": "content_rating",
        "aired": "2018-01-01",
        "summary": "summary",
        "rating": 1,
        "writers": ["person"],
        "directors": ["person"]
    }
    dump = schema.dump(Episode())
    assert dump == {
        "title": [],
        "content_rating": None,
        "aired": None,
        "summary": None,
        "rating": None,
        "writers": [],
        "directors": []
    }


def test_episode_strict_schema_load(
        episode_strict_schema: EpisodeStrictSchema
):
    schema = episode_strict_schema
    load = schema.load({
        "title": ["title"],
        "content_rating": "content_rating",
        "aired": "2018-01-01",
        "summary": "summary",
        "rating": 1,
        "writers": ["person"],
        "directors": ["person"]
    })
    assert load == Episode(
        title=["title"],
        content_rating="content_rating",
        aired=date(2018, 1, 1),
        summary="summary",
        rating=1,
        writers=[Person(name="person")],
        directors=[Person(name="person")]
    )
    load = schema.load({
        "title": ["title"],
        "content_rating": "content_rating",
        "aired": "2018-01-01",
        "summary": "summary",
        "rating": 1,
        "writers": [None],
        "directors": [""]
    })
    assert load == Episode(
        title=["title"],
        content_rating="content_rating",
        aired=date(2018, 1, 1),
        summary="summary",
        rating=1,
        writers=[],
        directors=[]
    )
    with pytest.raises(ValidationError):
        schema.load({
            "title": None,
            "content_rating": None,
            "aired": None,
            "summary": None,
            "rating": None,
            "writers": None,
            "directors": None
        })
    with pytest.raises(ValidationError):
        schema.load({})


def test_episode_strict_schema_dump(
        episode_strict_schema: EpisodeStrictSchema
):
    schema = episode_strict_schema
    dump = schema.dump(Episode(
        title=["title"],
        content_rating="content_rating",
        aired=date(2018, 1, 1),
        summary="summary",
        rating=1,
        writers=[Person(name="person")],
        directors=[Person(name="person")]
    ))
    assert dump == {
        "title": ["title"],
        "content_rating": "content_rating",
        "aired": "2018-01-01",
        "summary": "summary",
        "rating": 1,
        "writers": ["person"],
        "directors": ["person"]
    }
    dump = schema.dump(Episode())
    assert dump == {
        "title": [],
        "content_rating": None,
        "aired": None,
        "summary": None,
        "rating": None,
        "writers": [],
        "directors": []
    }
