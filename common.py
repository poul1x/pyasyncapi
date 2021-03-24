from schema import Schema
from typing import Optional, List
from pydantic import BaseModel, AnyUrl


class Reference(BaseModel):

    """ A simple object to allow referencing other components in the specification, internally and externally.
    The Reference Object is defined by JSON Reference and follows the same structure, behavior and rules. """

    ref: str

class Parameter(BaseModel):

    """ Describes a parameter included in a channel name """

    description: Optional[str]
    """A verbose explanation of the parameter. CommonMark syntax can be used for rich text representation"""

    schema: Schema
    """Definition of the parameter"""

    location: Optional[str]
    """ A runtime expression that specifies the location of the parameter value.
        Even when a definition for the target field exists, it MUST NOT be used to validate this parameter but,
        instead, the schema property MUST be used
    """

class ExternalDocumentation(BaseModel):

    description: Optional[str]
    """ A short description of the target documentation. CommonMark syntax can be used for rich text representation. """

    url: AnyUrl
    """ Required. The URL for the target documentation. Value MUST be in the format of a URL."""


class Tag(BaseModel):

    name: str
    """Required. The name of the tag."""

    description: Optional[str]
    """A short description for the tag. CommonMark syntax can be used for rich text representation."""

    externalDocs: Optional[ExternalDocumentation]
    """Documentation Object	Additional external documentation for this tag."""

class CorrelationId:

    description: Optional[str]
    """Optional description of the identifier. CommonMark syntax can be used for rich text representation."""

    location: str
    """ Required. runtime expression that specifies the location of the correlation ID.
        $message.header#/MQMD/CorrelId
    """