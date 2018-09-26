import dataclasses
from dataclasses import Field, asdict, is_dataclass
from typing import Any, Dict, List

from marshmallow import Schema, post_load, pre_dump, pre_load

__all__ = ["DataClassSchema"]


class DataClassSchema(Schema):

    @pre_dump
    def convert(self, data) -> Dict[str, Any]:
        """
        Convert dataclass object to dict.

        :param data: Input data
        :type data: Any
        :return: Dictionary for dumping.
        :rtype: Dict[str, Any]
        """
        new_data = asdict(data) if is_dataclass(data) else {**data}
        self.filter_data(new_data)
        return new_data

    @pre_load
    def filter(self, data: Dict[str, Any]) -> Dict[str, Any]:
        new_data = {**data}
        self.filter_data(new_data)
        return new_data

    def filter_data(self, data: Dict[str, Any]):
        data_class = self.data_class
        # noinspection PyDataclass
        data_class_fields: List[Field] = dataclasses.fields(data_class)
        for field in data_class_fields:
            name = field.name
            if name not in data:
                continue
            f_type = field.type
            origin = getattr(f_type, "__origin__", None)
            args = getattr(f_type, "__args__", ())
            if f_type == list or origin == list:
                if data[name] is None:
                    # Convert None to empty list for List field
                    data[name] = []
                else:
                    # Filter None and empty string in list
                    data[name] = [value for value in data[name]
                                  if value is not None and value != ""]
            elif ((f_type == str or origin == str or str in args) and
                  data[name] == ""):
                # Replace empty string with None
                data[name] = None

    @post_load
    def post_load(self, data) -> Any:
        """
        Convert dict to dataclass object

        :param data: Input data
        :type data: Dict[str, Any]
        :return: Dataclass
        :rtype: Any
        """
        data_class = self.data_class
        return data_class(**data)

    @property
    def data_class(self) -> type:
        """
        Provide the dataclass of this schema.

        :return: Dataclass
        :rtype: type
        """
        raise NotImplementedError()
