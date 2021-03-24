from typing import List, Dict, Optional
from server_bindings import ServerBinding

class ServerVariable:

    """ An object representing a Server Variable for server URL template substitution."""

    enum: List[str]
    """An enumeration of string values to be used if the substitution options are from a limited set."""

    default: str
    """The default value to use for substitution, and to send, if an alternate value is not supplied."""

    description: Optional[str]
    """An optional description for the server variable. CommonMark syntax MAY be used for rich text representation."""

    examples: Optional[List[str]]
    """An array of examples of the server variable."""


class SequrityRequirement:

    """ Lists the required security schemes to execute operation.
        The name used for each property MUST correspond to a security scheme declared
        in the Security Schemes under the Components Object.
    """

    name: str
    """Each name MUST correspond to a security scheme which is declared in the Security Schemes under the Components Object. If the security scheme is of type "oauth2" or "openIdConnect", then the value is a list of scope names required for the execution. For other security scheme types, the array MUST be empty."""

    schemes: List[str]
    """Required security schemes to execute this operation"""


class Server:

    url: str
    """A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the AsyncAPI document is being served. Variable substitutions will be made when a variable is named in {brackets}."""

    protocol: str
    """The protocol this URL supports for connection. Supported protocol include, but are not limited to: amqp, amqps, http, https, jms, kafka, kafka-secure, mqtt, secure-mqtt, stomp, stomps, ws, wss."""

    protocolVersion: Optional[str]
    """The version of the protocol used for connection. For instance: AMQP 0.9.1, HTTP 2.0, Kafka 1.0.0, etc."""

    description: Optional[str]
    """An optional string describing the host designated by the URL. CommonMark syntax MAY be used for rich text representation."""

    variables: Optional[Dict[str, ServerVariable]]
    """A map between a variable name and its value. The value is used for substitution in the server's URL template."""

    security: List[SequrityRequirement]
    """A declaration of which security mechanisms can be used with this server. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a connection or operation."""

    bindings: Optional[Dict[str, ServerBinding]]
    """A free-form map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the server."""