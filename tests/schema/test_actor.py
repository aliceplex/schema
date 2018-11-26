import pytest
from marshmallow import ValidationError

from aliceplex.schema import Actor, ActorSchema, ActorStrictSchema


def test_actor_schema_load(actor_schema: ActorSchema):
    schema = actor_schema
    load = schema.load({"name": "name", "photo": "photo", "role": "role"})
    assert load == Actor(name="name", photo="photo", role="role")
    load = schema.load({"name": None, "photo": None, "role": None})
    assert load == Actor()
    load = schema.load({})
    assert load == Actor()


def test_actor_schema_dump(actor_schema: ActorSchema):
    schema = actor_schema
    dump = schema.dump(Actor(name="name", photo="photo", role="role"))
    assert dump == {"name": "name", "photo": "photo", "role": "role"}
    dump = schema.dump(Actor())
    assert dump == {"name": None, "photo": None, "role": None}


def test_actor_strict_schema_load(actor_strict_schema: ActorStrictSchema):
    schema = actor_strict_schema
    load = schema.load({"name": "name", "photo": "photo", "role": "role"})
    assert load == Actor(name="name", photo="photo", role="role")
    load = schema.load({"name": "name", "role": "role"})
    assert load == Actor(name="name", role="role")
    with pytest.raises(ValidationError):
        schema.load({"name": None, "photo": None, "role": None})
    with pytest.raises(ValidationError):
        schema.load({})


def test_actor_strict_schema_dump(actor_strict_schema: ActorStrictSchema):
    schema = actor_strict_schema
    dump = schema.dump(Actor(name="name", photo="photo", role="role"))
    assert dump == {"name": "name", "photo": "photo", "role": "role"}
    dump = schema.dump(Actor())
    assert dump == {"name": None, "photo": None, "role": None}
