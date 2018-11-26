Usage
=====

Model
-----

Model classes use dataclass from Python 3.7. You can pass parameters to create the model class.

.. code-block:: python

    from aliceplex.schema import Actor

    actor = Actor(name="Test", role="Role", photo="http://example.com/avator.jpg")


Schema
------

Schema classes is created for serialization between dictionary and model classes.
For example, you can use schema classes to deserialize dictionary from JSON to a model classes valid values.

.. code-block:: python

    from aliceplex.schema import ActorSchema

    schema = ActorSchema()
    # Deserialize from JSON
    schema.load({"name": "name", "photo": "photo", "role": "role"})
    # Serialize to JSON
    actor = Actor(name="Test", role="Role", photo="http://example.com/avator.jpg")
    json = schema.dump(actor)

Schema classes is inherited from marshmallow.
For more usage, please refer to `its documentation <https://marshmallow.readthedocs.io/en/3.0/api_reference.html#schema>`_.