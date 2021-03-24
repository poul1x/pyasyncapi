from pydantic.class_validators import root_validator
from pydantic.main import BaseModel
from schema import Schema
from typing import Dict, Union, Optional
from common import Reference, Parameter, CorrelationId

from security_scheme import SecurityScheme

from message import Message, MessageTrait
from message_bindings import MessageBinding

from operation import OperationTrait
from operation_bindings import OperationBinding

from server import ServerBinding
from server_bindings import ServerBinding

from channel import ChannelBinding
from channel_bindings import ChannelBinding
import re

BaseModel.schema

class Components:

    """
    Holds a set of reusable objects for different aspects of the AsyncAPI specification.
    All objects defined within the components object will have no effect on the API
    unless they are explicitly referenced from properties outside the components object.
    """

    schemas: Optional[Dict[str, Union[Schema, Reference]]]
    """	An object to hold reusable Schema Objects. """

    messages: Optional[Dict[str, Union[Message, Reference]]]
    """	An object to hold reusable Message Objects. """

    securitySchemes: Optional[Dict[str, Union[SecurityScheme, Reference]]]
    """	An object to hold reusable Security Scheme Objects. """

    parameters: Optional[Dict[str, Union[Parameter, Reference]]]
    """	An object to hold reusable Parameter Objects. """

    correlationIds: Optional[Dict[str, CorrelationId]]
    """	An object to hold reusable Correlation ID Objects. """

    operationTraits: Optional[Dict[str, OperationTrait]]
    """	An object to hold reusable Operation Trait Objects. """

    messageTraits: Optional[Dict[str, MessageTrait]]
    """An object to hold reusable Message Trait Objects. """

    serverBindings: Optional[Dict[str, ServerBinding]]
    """An object to hold reusable Server Binding Objects. """

    channelBindings: Optional[Dict[str, ChannelBinding]]
    """An object to hold reusable Channel Binding Objects."""

    operationBindings: Optional[Dict[str, OperationBinding]]
    """	An object to hold reusable Operation Binding Objects. """

    messageBindings: Optional[Dict[str, MessageBinding]]
    """An object to hold reusable Message Binding Objects."""

    @root_validator
    def validate(cls, items):
        regex = re.compile(r"^[A-Za-z0-9_\-]+$")
        for name, _map in items.values():
            for key in _map.keys():
                if not regex.match(key):
                    err = f"Map {name}: key {key} does not match the regex {regex}"
                    raise ValueError(err)

        return items