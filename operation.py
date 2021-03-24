from typing import Dict, Optional
from typing import List
from common import ExternalDocumentation, Tag
from operation_bindings import OperationBinding
from message import Message

class OperationTrait:

    operationId: str
    """Unique string used to identify the operation. The id MUST be unique among all operations described in the API. The operationId value is case-sensitive. Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to follow common programming naming conventions."""

    summary: str
    """A short summary of what the operation is about."""

    description: Optional[str]
    """A verbose explanation of the operation. CommonMark syntax can be used for rich text representation."""

    tags: Optional[List[Tag]]
    """A list of tags for API documentation control. Tags can be used for logical grouping of operations."""

    externalDocs: Optional[ExternalDocumentation]
    """Additional external documentation for this operation."""

    bindings: Optional[Dict[str,OperationBinding]]
    """A free-form map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the operation."""


class Operation:

    operation_id: str
    """Unique string used to identify the operation. The id MUST be unique among all operations described in the API. The operationId value is case-sensitive. Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to follow common programming naming conventions."""

    summary: str
    """A short summary of what the operation is about."""

    description: Optional[str]
    """A verbose explanation of the operation. CommonMark syntax can be used for rich text representation."""

    tags: Optional[List[Tag]]
    """A list of tags for API documentation control. Tags can be used for logical grouping of operations."""

    externalDocs: Optional[ExternalDocumentation]
    """Documentation Object	Additional external documentation for this operation."""

    bindings: Optional[Dict[str, OperationBinding]]
    """A free-form map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the operation."""

    traits: Optional[List[OperationTrait]]
    """A list of traits to apply to the operation object. Traits MUST be merged into the operation object using the JSON Merge Patch algorithm in the same order they are defined here."""

    # one | oneOf!
    message: List[Message]
    """A definition of the message that will be published or received on this channel. oneOf is allowed here to specify multiple messages, however, a message MUST be valid only against one of the referenced message objects."""