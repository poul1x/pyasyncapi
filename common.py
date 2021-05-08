from typing import Optional
from util import SpecStringObject, SpecEmptyObject


class SpecParameterObject:

    """Describes a parameter included in a channel name"""

    _schema: Optional[SpecStringObject]
    """Definition of the parameter"""

    _description: Optional[SpecStringObject]
    """A verbose explanation of the parameter. CommonMark syntax can be used for rich text representation"""

    _location: Optional[SpecStringObject]
    """ A runtime expression that specifies the location of the parameter value.
        Even when a definition for the target field exists, it MUST NOT be used to validate this parameter but,
        instead, the schema property MUST be used
    """

    _validation_enabled: bool

    def __init__(
        self,
        schema: Optional[str] = None,
        description: str = None,
        location: Optional[str] = None,
        validation_enabled: bool = True,
    ):
        self._validation_enabled = validation_enabled
        self.schema = schema or SpecEmptyObject()
        self.description = description or SpecEmptyObject()
        self.location = location or SpecEmptyObject()

    @property
    def schema(self) -> str:
        return self._schema.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def location(self) -> str:
        return self._location.value

    @property
    def validation_enabled(self) -> bool:
        return self._validation_enabled

    @schema.setter
    def schema(self, value: str):
        self._schema = SpecStringObject("schema", value, self._validation_enabled)
        self._schema.validate()

    @description.setter
    def description(self, value: str):
        self._description = SpecStringObject(
            "description", value, self._validation_enabled
        )
        self._description.validate()

    @location.setter
    def location(self, value: str):
        self._location = SpecStringObject("location", value, self._validation_enabled)
        self._location.validate()

    def compose(self):
        return {
            **self._schema.compose(),
            **self._description.compose(),
            **self._location.compose(),
        }


class SpecExternalDocumentationObject:

    _url: SpecStringObject
    """ Required. The URL for the target documentation. Value MUST be in the format of a URL."""

    _description: Optional[SpecStringObject]
    """ A short description of the target documentation. CommonMark syntax can be used for rich text representation. """

    _validation_enabled: bool

    def __init__(
        self, url: str, description: str = None, validation_enabled: bool = True
    ):
        self._validation_enabled = validation_enabled
        self.description = description or SpecEmptyObject()
        self.url = url

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def validation_enabled(self) -> bool:
        return self._validation_enabled

    @description.setter
    def description(self, value: str):
        self._description = SpecStringObject(
            "description", value, self._validation_enabled
        )
        self._description.validate()

    @url.setter
    def url(self, value: str):
        self._url = SpecStringObject("url", value, self._validation_enabled)
        self._url.validate()

    def compose(self):
        return {
            "externalDocs": {
                **self._url.compose(),
                **self._description.compose(),
            },
        }


class SpecCorrelationIdObject:

    description: Optional[str]
    """Optional description of the identifier. CommonMark syntax can be used for rich text representation."""

    location: str
    """ Required. runtime expression that specifies the location of the correlation ID.
        $message.header#/MQMD/CorrelId
    """

    _validation_enabled: bool

    def __init__(
        self, location: str, description: str, validation_enabled: bool = True
    ):
        self._validation_enabled = validation_enabled
        self.description = description or SpecEmptyObject()
        self.location = location

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def validation_enabled(self) -> bool:
        return self._validation_enabled

    @description.setter
    def description(self, value: str):
        self._description = SpecStringObject(
            "description", value, self._validation_enabled
        )
        self._description.validate()

    @url.setter
    def url(self, value: str) -> str:
        self._url = SpecStringObject("url", value, self._validation_enabled)
        self._url.validate()

    def compose(self):
        return {
            "externalDocs": {
                self._url.compose(),
                self._description.compose(),
            },
        }
