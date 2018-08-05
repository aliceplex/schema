Usage
=====

Model
-----

Model classes use dataclass from Python 3.7. You can pass parameters to create the model class.

.. code-block:: python

    from plex_schema.model import Actor

    actor = Actor(name="Test", role="Role", photo="http://example.com/avator.jpg")


Schema
------

Schema classes is inherited from marshmallow.
Please refer to `its documentation <https://marshmallow.readthedocs.io/en/3.0/api_reference.html#schema>`_.