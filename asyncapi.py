# 2.0.0

from typing import Optional
from util import SpecEmptyObject, SpecStringObject

# from schema import Schema
# from operation_bindings import OperationBinding
# from server_bindings import ServerBinding
# from message_bindings import MessageBinding
# from server import Server
# from channel import Channel
# from components import Components

from common import SpecExternalDocumentationObject,
from tags import SpecTagListObject


class SpecContactObject:

    _name: SpecStringObject
    """The identifying name of the contact person/organization"""

    _url: SpecStringObject
    """The URL pointing to the contact information. MUST be in the format of a URL"""

    _email: SpecStringObject
    """The email address of the contact person/organization. MUST be in the format of an email address"""

    _validation_enabled: bool

    def __init__(
        self, name: str, url: str, email: str, validation_enabled: bool = True
    ) -> None:
        self._validation_enabled = validation_enabled
        self.enail = email
        self.name = name
        self.url = url

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def email(self) -> str:
        return self._email.value

    @property
    def validation_enabled(self) -> bool:
        return self._validation_enabled

    @name.setter
    def name(self, value: str):
        self._name = SpecStringObject("name", value, self._validation_enabled)
        self._name.validate()

    @url.setter
    def url(self, value: str) -> str:
        self._url = SpecStringObject("url", value, self._validation_enabled)
        self._url.validate()

    @email.setter
    def email(self, value: str) -> str:
        self._email = SpecStringObject("email", value, self._validation_enabled)
        self._email.validate()

    def compose(self):
        return {
            "contact": {
                self._name.compose(),
                self._url.compose(),
                self._email.compose(),
            },
        }


class SpecLicenseObject:

    _name: SpecStringObject
    """The identifying name of the contact person/organization"""

    _url: SpecStringObject
    """The URL pointing to the contact information. MUST be in the format of a URL"""

    _validation_enabled: bool

    def __init__(self, name: str, url: str, validation_enabled: bool = True):
        self._validation_enabled = validation_enabled
        self.name = name
        self.url = url

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def validation_enabled(self) -> bool:
        return self._validation_enabled

    @name.setter
    def name(self, value: str):
        self._name = SpecStringObject("name", value, self._validation_enabled)
        self._name.validate()

    @url.setter
    def url(self, value: str) -> str:
        self._url = SpecStringObject("url", value, self._validation_enabled)
        self._url.validate()

    def compose(self):
        return {
            "license": {
                self._name.compose(),
                self._url.compose(),
            },
        }


class SpecInfoObject:

    title: str
    """The title of the application. """

    version: str
    """Provides the version of the application API (not to be confused with the specification version). """

    description: Optional[str]
    """ A short description of the application. CommonMark syntax can be used for rich text representation. """

    terms_of_service: Optional[str]
    """ A URL to the Terms of Service for the API. MUST be in the format of a URL. """

    contact: Optional[SpecContactObject]
    """ Contact Object	The contact information for the exposed API. """

    license: Optional[SpecLicenseObject]
    """ License Object	The license information for the exposed API. """

    _validation_enabled: bool

    def __init__(
        self,
        title: str,
        version: str,
        description: Optional[str] = None,
        terms_of_service: Optional[str] = None,
        contact: Optional[SpecContactObject] = None,
        license: Optional[SpecLicenseObject] = None,
        validation_enabled: bool = True,
    ) -> None:
        self.validation_enabled = validation_enabled
        self.terms_of_service = terms_of_service
        self.description = description
        self.version = version
        self.contact = contact
        self.license = license
        self.title = title

    @property
    def validation_enabled(self) -> bool:
        return self._validation_enabled

    @property
    def title(self) -> str:
        return self._title.value

    @property
    def version(self) -> str:
        return self._version.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def terms_of_service(self) -> str:
        return self._terms_of_service.value

    @property
    def contact(self) -> str:
        return self._contact

    @property
    def license(self) -> str:
        return self._license

    @title.setter
    def title(self, value: str):
        self._title = SpecStringObject("title", value, self._validation_enabled)
        self._title.validate()

    @version.setter
    def version(self, value: str):
        self._version = SpecStringObject("version", value, self._validation_enabled)
        self._version.validate()

    @description.setter
    def description(self, value: str):
        self._description = SpecStringObject(
            "description", value, self._validation_enabled
        )
        self._description.validate()

    @terms_of_service.setter
    def terms_of_service(self, value: str):
        self._terms_of_service = SpecStringObject(
            "terms_of_service", value, self._validation_enabled
        )
        self._terms_of_service.validate()

    @contact.setter
    def contact(self, value: SpecContactObject):
        assert isinstance(value, SpecContactObject)
        self._contact = value

    @license.setter
    def license(self, value: SpecLicenseObject):
        assert isinstance(value, SpecLicenseObject)
        self._license = value

    def compose(self):
        return {
            "info": {
                self._title.compose(),
                self._version.compose(),
                self._description.compose(),
                self._terms_of_service.compose(),
                self._contact.compose(),
                self._license.compose(),
            },
        }


class SpecAsyncApiObject:

    _asyncapi: SpecStringObject
    """ Required. AsyncAPI Version String.
        Specifies the AsyncAPI Specification version being used.
        It can be used by tooling Specifications and clients to interpret the version.
        The structure shall be major.minor.patch, where patch versions
        must be compatible with the existing major.minor tooling.
        Typically patch versions will be introduced to address errors in the documentation,
        and tooling should typically be compatible with the corresponding major.minor (1.0.*).
        Patch versions will correspond to patches of this document.
    """

    _id: Optional[SpecStringObject]
    """ Identifier Identifier of the application the AsyncAPI document is defining. """

    _info: SpecInfoObject
    """	Required. Provides metadata about the API. The metadata can be used by the clients if needed. """

    # servers: Optional[Dict[str,Server]]
    # """	Servers Object	Provides connection details of servers. """

    # channels: Dict[str, Channel]
    # """ Required. Channels Object	Required The available channels and messages for the API. """

    # components: Optional[Components]  # $checked, here
    # """	Components Object	An element to hold various schemas for the specification. """

    _tags: Optional[SpecTagListObject]
    """A list of tags used by the specification with additional metadata. Each tag name in the list MUST be unique. """

    _external_docs: Optional[SpecExternalDocumentationObject]
    """Additional external documentation. """

    _validation_enabled: bool

    def __init__(
        self,
        asyncapi_ver: str,
        info: SpecInfoObject,
        channels: dict,
        components: Optional[dict] = None,
        servers: Optional[dict] = None,
        app_id: Optional[str] = None,
        tags: Optional[SpecTagListObject] = None,
        external_docs: Optional[SpecExternalDocumentationObject] = None,
        validation_enabled: bool = True,
    ):
        self._validation_enabled = validation_enabled
        self.external_docs = external_docs or SpecEmptyObject()
        self.components = components or SpecEmptyObject()
        self.servers = servers or SpecEmptyObject()
        self.app_id = app_id or SpecEmptyObject()
        self.tags = tags or SpecEmptyObject()
        self.asyncapi_ver = asyncapi_ver
        self.channels = channels
        self.info = info

    @property
    def asyncapi_ver(self) -> str:
        return self._asyncapi_ver.value

    @property
    def app_id(self) -> str:
        return self._app_id.value

    @property
    def info(self) -> SpecInfoObject:
        return self._info

    @property
    def channels(self) -> str:
        return self._channels

    @property
    def components(self) -> str:
        return self._components

    @property
    def servers(self) -> str:
        return self._servers

    @property
    def tags(self) -> SpecTagListObject:
        return self._tags

    @property
    def external_docs(self) -> SpecExternalDocumentationObject:
        return self._external_docs

    @property
    def validation_enabled(self) -> bool:
        return self._validation_enabled

    @asyncapi_ver.setter
    def asyncapi_ver(self, value: str):
        self._asyncapi_ver = SpecStringObject(
            "asyncapi", value, self._validation_enabled
        )
        self._asyncapi_ver.validate()

    @app_id.setter
    def app_id(self, value: str):
        self._app_id = SpecStringObject("id", value, self._validation_enabled)
        self._app_id.validate()

    @info.setter
    def info(self, value: str):
        assert isinstance(value, str)
        self._info = value

    @channels.setter
    def channels(self, value: str):
        assert isinstance(value, str)
        self._channels = value

    @components.setter
    def components(self, value: str):
        assert isinstance(value, str)
        self._components = value

    @servers.setter
    def servers(self, value: str):
        assert isinstance(value, str)
        self._servers = value

    @tags.setter
    def tags(self, value: str):
        assert isinstance(value, str)
        self._tags = value

    @external_docs.setter
    def external_docs(self, value: str):
        assert isinstance(value, str)
        self._external_docs = value

    def compose(self):
        return {
            **self._asyncapi_ver.compose(),
            **self._external_docs.compose(),
            **self._components.compose(),
            **self._channels.compose(),
            **self._servers.compose(),
            **self._app_id.compose(),
            **self._tags.compose(),
            **self._info.compose(),
        }
