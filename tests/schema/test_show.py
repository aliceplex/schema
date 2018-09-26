from datetime import date

import pytest
from marshmallow import ValidationError

from plex_schema import Actor, Show, ShowSchema, ShowStrictSchema


def test_show_schema_load(show_schema: ShowSchema):
    schema = show_schema
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
        "season_summary": {
            1: "Season 1 Summary"
        }
    })
    assert load == Show(
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
        season_summary={1: "Season 1 Summary"}
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
        "season_summary": {}
    })
    assert load == Show()
    load = schema.load({})
    assert load == Show()


def test_show_schema_dump(show_schema: ShowSchema):
    schema = show_schema
    dump = schema.dump(Show(
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
        season_summary={1: "Season 1 Summary"}
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
            "role": "role"
        }],
        "season_summary": {
            1: "Season 1 Summary"
        }
    }
    dump = schema.dump(Show())
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
        "season_summary": {}
    }


def test_show_strict_schema_load(show_strict_schema: ShowStrictSchema):
    schema = show_strict_schema
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
        "season_summary": {
            1: "Season 1 Summary"
        }
    })
    assert load == Show(
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
        season_summary={1: "Season 1 Summary"}
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
            "season_summary": None
        })
    with pytest.raises(ValidationError):
        schema.load({})


def test_show_strict_schema_dump(show_strict_schema: ShowStrictSchema):
    schema = show_strict_schema
    dump = schema.dump(Show(
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
        season_summary={1: "Season 1 Summary"}
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
            "role": "role"
        }],
        "season_summary": {
            1: "Season 1 Summary"
        }
    }
    dump = schema.dump(Show())
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
        "season_summary": {}
    }
