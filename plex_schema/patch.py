from datetime import date, datetime

from marshmallow import fields


class PatchDateField(fields.Date):
    def _deserialize(self, value, attr, data):
        if isinstance(value, date):
            return value
        return super()._deserialize(value, attr, data)


class PatchDateTimeField(fields.DateTime):
    def _deserialize(self, value, attr, data):
        if isinstance(value, datetime):
            return value
        return super()._deserialize(value, attr, data)
