from datetime import date

import pytest
from marshmallow import ValidationError

from aliceplex.schema import Album, AlbumSchema, AlbumStrictSchema


def test_album_schema_load(album_schema: AlbumSchema):
    schema = album_schema
    load = schema.load({
        "aired": "2018-01-01",
        "collections": ["collections"],
        "genres": ["genres"],
        "summary": "summary"
    })
    assert load == Album(
        aired=date(2018, 1, 1),
        collections=["collections"],
        genres=["genres"],
        summary="summary",
    )
    load = schema.load({
        "aired": None,
        "collections": [],
        "genres": [],
        "summary": None
    })
    assert load == Album()
    load = schema.load({
        "aired": None,
        "collections": None,
        "genres": None,
        "summary": None
    })
    assert load == Album()
    load = schema.load({})
    assert load == Album()


def test_album_schema_dump(album_schema: AlbumSchema):
    schema = album_schema
    dump = schema.dump(Album(
        aired=date(2018, 1, 1),
        collections=["collections"],
        genres=["genres"],
        summary="summary",
    ))
    assert dump == {
        "aired": "2018-01-01",
        "collections": ["collections"],
        "genres": ["genres"],
        "summary": "summary"
    }
    # noinspection PyTypeChecker
    dump = schema.dump(Album(collections=[""], genres=[None], summary=""))
    assert dump == {
        "aired": None,
        "collections": [],
        "genres": [],
        "summary": None
    }
    dump = schema.dump(Album())
    assert dump == {
        "aired": None,
        "collections": [],
        "genres": [],
        "summary": None
    }


def test_album_strict_schema_load(album_strict_schema: AlbumStrictSchema):
    schema = album_strict_schema
    load = schema.load({
        "aired": "2018-01-01",
        "collections": ["collections"],
        "genres": ["genres"],
        "summary": "summary"
    })
    assert load == Album(
        aired=date(2018, 1, 1),
        collections=["collections"],
        genres=["genres"],
        summary="summary",
    )

    with pytest.raises(ValidationError):
        schema.load({
            "aired": "2018-01-01",
            "collections": [],
            "genres": [],
            "summary": "summary"
        })

    with pytest.raises(ValidationError):
        schema.load({
            "aired": "2018-01-01",
            "collections": None,
            "genres": None,
            "summary": "summary"
        })
    with pytest.raises(ValidationError):
        schema.load({
            "aired": "2018-01-01",
            "collections": [""],
            "genres": [None],
            "summary": "summary"
        })
    with pytest.raises(ValidationError):
        schema.load({
            "aired": None,
            "collections": None,
            "genres": None,
            "summary": None
        })
    with pytest.raises(ValidationError):
        schema.load({})


def test_album_strict_schema_dump(album_strict_schema: AlbumStrictSchema):
    schema = album_strict_schema
    dump = schema.dump(Album(
        aired=date(2018, 1, 1),
        collections=["collections"],
        genres=["genres"],
        summary="summary",
    ))
    assert dump == {
        "aired": "2018-01-01",
        "collections": ["collections"],
        "genres": ["genres"],
        "summary": "summary"
    }
    # noinspection PyTypeChecker
    dump = schema.dump(Album(collections=[""], genres=[None]))
    assert dump == {
        "aired": None,
        "collections": [],
        "genres": [],
        "summary": None
    }
    dump = schema.dump(Album())
    assert dump == {
        "aired": None,
        "collections": [],
        "genres": [],
        "summary": None
    }
