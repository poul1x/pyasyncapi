from schema import Schema
from common import Reference, ExternalDocumentation, Tag, CorrelationId
from typing import Union, Dict, List, Any, Optional
from message_bindings import MessageBinding
from schema import Schema


class MessageTrait:

    headers: Optional[Union[Schema, Reference]]
    """Schema definition of the application headers. Schema MUST be of type "object". It MUST NOT define the protocol headers."""

    correlationId: Optional[Union[CorrelationId, Reference]]
    """Definition of the correlation ID used for message tracing or matching."""

    schemaFormat: Optional[str]
    """A string containing the name of the schema format/language used to define the message payload. If omitted, implementations should parse the payload as a Schema object."""

    contentType: Optional[str]
    """The content type to use when encoding/decoding a message's payload. The value MUST be a specific media type (e.g. application/json). When omitted, the value MUST be the one specified on the defaultContentType field."""

    name: Optional[str]
    """A machine-friendly name for the message."""

    title: Optional[str]
    """A human-friendly title for the message."""

    summary: Optional[str]
    """A short summary of what the message is about."""

    description: Optional[str]
    """A verbose explanation of the message. CommonMark syntax can be used for rich text representation."""

    tags: Optional[List[Tag]]
    """A list of tags for API documentation control. Tags can be used for logical grouping of messages."""

    externalDocs: Optional[ExternalDocumentation]
    """Additional external documentation for this message."""

    bindings: Optional[Dict[str, MessageBinding]]
    """A free-form map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the message."""

    examples: Optional[List[Dict[str, Any]]]
    """An array with examples of valid message objects."""


class Message:

    headers: Optional[Union[Schema, Reference]]
    """Schema definition of the application headers. Schema MUST be of type "object". It MUST NOT define the protocol headers"""

    payload: Any
    """Definition of the message payload. It can be of any type but defaults to Schema object"""

    correlation_id: Optional[Union[CorrelationId, Reference]]
    """Definition of the correlation ID used for message tracing or matching"""

    schema_format: Optional[str]
    """A string containing the name of the schema format used to define the message payload. If omitted, implementations should parse the payload as a Schema object. Check out the supported schema formats table for more information. Custom values are allowed but their implementation is OPTIONAL. A custom value MUST NOT refer to one of the schema formats listed in the table"""

    content_type: Optional[str]
    """The content type to use when encoding/decoding a message's payload. The value MUST be a specific media type (e.g. application/json). When omitted, the value MUST be the one specified on the defaultContentType field"""

    name: Optional[str]
    """A machine-friendly name for the message"""

    title: Optional[str]
    """A human-friendly title for the message"""

    summary: Optional[str]
    """A short summary of what the message is about"""

    description: Optional[str]
    """A verbose explanation of the message. CommonMark syntax can be used for rich text representation"""

    tags: Optional[List[Tag]]
    """A list of tags for API documentation control. Tags can be used for logical grouping of messages"""

    external_docs: Optional[ExternalDocumentation]
    """Additional external documentation for this message"""

    bindings: Optional[Dict[str, MessageBinding]]
    """A free-form map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the message"""

    examples: Optional[List[Dict[str, Any]]]
    """An array with examples of valid message objects"""

    traits: Optional[List[MessageTrait]]
    """A list of traits to apply to the message object. Traits MUST be merged into the message object using the JSON Merge Patch algorithm in the same order they are defined here. The resulting object MUST be a valid Message Object"""