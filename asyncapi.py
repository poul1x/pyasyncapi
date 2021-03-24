# 2.0.0

from pydantic import BaseModel, root_validator, validator
from pydantic.fields import Field
from pydantic.networks import AnyHttpUrl, AnyUrl, EmailStr

from typing import Any, Dict, List, Union, Optional, Tuple

from schema import Schema
from operation_bindings import OperationBinding
from server_bindings import ServerBinding
from message_bindings import MessageBinding
from server import Server
from channel import Channel
from components import Components

from common import Tag, ExternalDocumentation

import re


class ISerializable:

    def serialize():
        pass

    def deserialize():
        pass


class Contact:

    """ Contact information for the exposed API """

    name: str
    """The identifying name of the contact person/organization"""

    url: Optional[AnyUrl]
    """The URL pointing to the contact information. MUST be in the format of a URL"""

    email: Optional[EmailStr]
    """The email address of the contact person/organization. MUST be in the format of an email address"""


class License:

    name: str
    """Required. The license name used for the API."""

    url: Optional[AnyUrl]
    """A URL to the license used for the API. MUST be in the format of a URL."""


class Info:

    title: str
    """The title of the application. """

    version: str
    """Provides the version of the application API (not to be confused with the specification version). """

    description: Optional[str]
    """ A short description of the application. CommonMark syntax can be used for rich text representation. """

    terms_of_service: Optional[str]
    """ A URL to the Terms of Service for the API. MUST be in the format of a URL. """

    contact: Optional[Contact]
    """ Contact Object	The contact information for the exposed API. """

    license: Optional[License]
    """ License Object	The license information for the exposed API. """


class AsyncAPI(BaseModel):

    asyncapi: str = Field(regex=r"\d+.\d+.\d+")
    """ AsyncAPI Version String.
        Specifies the AsyncAPI Specification version being used.
        It can be used by tooling Specifications and clients to interpret the version.
        The structure shall be major.minor.patch, where patch versions must be compatible with the existing major.minor tooling.
        Typically patch versions will be introduced to address errors in the documentation,
        and tooling should typically be compatible with the corresponding major.minor (1.0.*).
        Patch versions will correspond to patches of this document.
    """

    id: Optional[str]
    """ Identifier Identifier of the application the AsyncAPI document is defining. """

    info: Info
    """	Info Object	Required. Provides metadata about the API. The metadata can be used by the clients if needed. """

    servers: Optional[Dict[str,Server]]
    """	Servers Object	Provides connection details of servers. """

    channels: Dict[str, Channel]
    """	Channels Object	Required The available channels and messages for the API. """

    components: Optional[Components]  # $checked, here
    """	Components Object	An element to hold various schemas for the specification. """

    tags: Optional[List[Tag]]
    """A list of tags used by the specification with additional metadata. Each tag name in the list MUST be unique. """

    externalDocs: Optional[ExternalDocumentation]
    """Additional external documentation. """

    @validator('servers')
    def validate_servers(cls, val):
        regex = re.compile(r'^[A-Za-z0-9_\-]+$')
        for name in val.keys():
            if not regex.match(name):
                raise ValueError(f'Does not match the regex {regex}')

        return val

# Producer

# Consumer

# Message

# Channel

# Protocol