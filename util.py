from typing import Dict, List, Any


class SpecEmptyObject:
    def compose(self):
        return {}


class SpecStringObject:

    _validation_enabled: bool
    _value: str
    _name: str

    def __init__(self, name: str, value: str, validation_enabled: bool = True):
        self._validation_enabled = validation_enabled
        self._value = value
        self._name = name

    @property
    def validation_enabled(self):
        return self._validation_enabled

    @property
    def value(self):
        return self._value

    @property
    def name(self):
        return self._name

    def validate(self):
        return True

    def __repr__(self):
        return f"SpecStringObject(name={self._name}, value={self._value}, \
            validation_enabled={self._validation_enabled})"

    def __str__(self):
        return repr(self)

    def compose(self):
        return {self._name: self._value}


class SpecUrlObject(SpecStringObject):
    def validate(self):

        if self._validation_enabled:
            pass

        return super().validate()

    def __repr__(self):
        return f"SpecUrlObject(name={self._name}, value={self._value}, \
            validation_enabled={self._validation_enabled})"

    def __str__(self):
        return repr(self)


# class SpecEmailObject(SpecStringObject):
# class SpecAsyncAPIVersionObject(SpecStringObject):
# class SpecReferenceStringObject(SpecStringObject):
# class SpecRuntimeExpressionResultObject(SpecStringObject):


class SpecMapObject:

    _map: Dict[Any]

    def __init__(self):
        self._map = {}

    def add_child(self, child_name: str, child_object: Any):

        if child_name in self._map.keys():
            raise ValueError(f"Child object with name '{child_name}' already exists")

        self._map[child_name] = child_object

    def remove_child(self, child_name: str, ignore_errors: bool = False):

        if child_name not in self._map.keys() and ignore_errors:
            raise ValueError(f"Child object with name '{child_name}' does not exist")

        del self._map[child_name]

    def replace_child(self, child_name, new_object):
        self.remove_child(child_name)
        self.add_child(child_name, new_object)

    def find_child(self, child_name):

        try:
            res = self._map[child_name]
        except KeyError:
            raise ValueError(f"Child object with name '{child_name}' does not exist")

        return res

    # def __repr__

    # def __str__


class SpecListObject:

    _list: List[Any]

    def __init__(self) -> None:
        self._list = {}

    def append_child(self, child_object: Any):

        if child_object in self._list:
            raise ValueError(
                f"Child object with name '{repr(child_object)}' already exists"
            )

        self._list.append(child_object)