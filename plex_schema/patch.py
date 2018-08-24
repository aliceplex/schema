"""
Patch module for upstream library
"""

from datetime import date, datetime

from marshmallow import fields


class PatchDateField(fields.Date):
    """
    Patched marshmallow date field to accept date object.
    """
    def _deserialize(self, value, attr, data):
        if isinstance(value, date):
            return value
        return super()._deserialize(value, attr, data)


class PatchDateTimeField(fields.DateTime):
    """
    Patched marshmallow datetime field to accept datetime object.
    """
    def _deserialize(self, value, attr, data):
        if isinstance(value, datetime):
            return value
        return super()._deserialize(value, attr, data)
