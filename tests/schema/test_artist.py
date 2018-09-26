import pytest
from marshmallow import ValidationError

from plex_schema import Artist, ArtistSchema, ArtistStrictSchema


def test_artist_schema_load(artist_schema: ArtistSchema):
    schema = artist_schema
    load = schema.load({
        "summary": "summary",
        "collections": ["collections"],
        "genres": ["genres"],
        "similar": ["similar"]
    })
    assert load == Artist(
        summary="summary",
        collections=["collections"],
        genres=["genres"],
        similar=["similar"]
    )
    load = schema.load({
        "summary": "",
        "collections": [],
        "genres": [""],
        "similar": [None]
    })
    assert load == Artist()
    load = schema.load({
        "summary": None,
        "collections": None,
        "genres": None,
        "similar": None
    })
    assert load == Artist()
    load = schema.load({})
    assert load == Artist()


def test_artist_schema_dump(artist_schema: ArtistSchema):
    schema = artist_schema
    dump = schema.dump(Artist(
        summary="summary",
        collections=["collections"],
        genres=["genres"],
        similar=["similar"]
    ))
    assert dump == {
        "summary": "summary",
        "collections": ["collections"],
        "genres": ["genres"],
        "similar": ["similar"]
    }
    dump = schema.dump(Artist())
    assert dump == {
        "summary": None,
        "collections": [],
        "genres": [],
        "similar": []
    }


def test_artist_strict_schema_load(artist_strict_schema: ArtistStrictSchema):
    schema = artist_strict_schema
    load = schema.load({
        "summary": "summary",
        "collections": ["collections"],
        "genres": ["genres"],
        "similar": ["similar"]
    })
    assert load == Artist(
        summary="summary",
        collections=["collections"],
        genres=["genres"],
        similar=["similar"]
    )
    with pytest.raises(ValidationError):
        schema.load({
            "summary": "summary",
            "collections": [],
            "genres": [""],
            "similar": [None]
        })
    with pytest.raises(ValidationError):
        schema.load({
            "summary": "",
            "collections": None,
            "genres": None,
            "similar": None
        })
    with pytest.raises(ValidationError):
        schema.load({
            "summary": "",
            "collections": [],
            "genres": [],
            "similar": []
        })
    with pytest.raises(ValidationError):
        schema.load({})


def test_artist_strict_schema_dump(artist_strict_schema: ArtistStrictSchema):
    schema = artist_strict_schema
    dump = schema.dump(Artist(
        summary="summary",
        collections=["collections"],
        genres=["genres"],
        similar=["similar"]
    ))
    assert dump == {
        "summary": "summary",
        "collections": ["collections"],
        "genres": ["genres"],
        "similar": ["similar"]
    }
    dump = schema.dump(Artist())
    assert dump == {
        "summary": None,
        "collections": [],
        "genres": [],
        "similar": []
    }
