from util import SpecStringObject, SpecEmptyObject, SpecListObject
from common import SpecExternalDocumentationObject
from typing import Optional, List


class SpecTagObject:

    _name: SpecStringObject
    """Required. The name of the tag."""

    _description: Optional[SpecStringObject]
    """A short description for the tag. CommonMark syntax can be used for rich text representation."""

    _external_docs: Optional[SpecExternalDocumentationObject]
    """Documentation Object	Additional external documentation for this tag."""

    _validation_enabled: bool

    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        external_docs: Optional[SpecExternalDocumentationObject] = None,
        validation_enabled: bool = True,
    ):
        self._validation_enabled = validation_enabled
        self.external_docs = external_docs or SpecEmptyObject()
        self.description = description or SpecEmptyObject()
        self.name = name

    @property
    def validation_enabled(self) -> bool:
        return self._validation_enabled

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def external_docs(self) -> SpecExternalDocumentationObject:
        return self._external_docs

    @name.setter
    def name(self, value: str):
        self._name = SpecStringObject("name", value, self._validation_enabled)
        self._name.validate()

    @description.setter
    def description(self, value: str) -> str:
        self._description = SpecStringObject(
            "description", value, self._validation_enabled
        )
        self._description.validate()

    @external_docs.setter
    def external_docs(self, value: SpecExternalDocumentationObject) -> str:
        assert isinstance(value, SpecExternalDocumentationObject)
        self._external_docs = value

    def spec(self):
        return {
            "externalDocs": {
                **self._name.spec(),
                **self._description.spec(),
                **self._external_docs.spec(),
            },
        }


class SpecTagListObject(SpecListObject):
    def __init__(self, tags: Optional[List[SpecTagObject]] = None):

        super().__init__(tags)

        if tags:
            assert isinstance(tags[0], SpecTagObject)
            self._list.extend(tags)

    def append_child(self, child_object: SpecTagObject):
        assert isinstance(child_object, SpecTagObject)
        super().append_child(child_object)

    def compose(self):
        return {"tags": self._list} if self._list else {}
