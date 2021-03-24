from typing import Optional, Union
from channel_bindings import ChannelBinding
from typing import Dict
from common import Parameter, Reference
from operation import Operation
from pydantic import BaseModel, validator
import re


class Channel(BaseModel):

    ref: Optional[str]
    """Allows for an external definition of this channel item. The referenced structure MUST be in the format of a Channel Item Object. If there are conflicts between the referenced definition and this Channel Item's definition, the behavior is undefined."""

    description: Optional[str]
    """An optional description of this channel item. CommonMark syntax can be used for rich text representation."""

    subscribe: Optional[Operation]
    """A definition of the SUBSCRIBE operation."""

    publish: Optional[Operation]
    """A definition of the PUBLISH operation."""

    parameters: Optional[Dict[str, Union[Parameter, Reference]]]
    """A map of the parameters included in the channel name. It SHOULD be present only when using channels with expressions (as defined by RFC 6570 section 2.2)."""

    bindings: Optional[Dict[str, ChannelBinding]]
    """A free-form map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the channel."""

    @validator("parameters")
    def validate_parameters(cls, val: dict):
        regex = re.compile(r"^[A-Za-z0-9_\-]+$")
        for name in val.keys():
            if not regex.match(name):
                raise ValueError(f"Does not match the regex {regex}")

        return val