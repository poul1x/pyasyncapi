
from typing import Any
from schema import Schema
from pydantic import BaseModel, Field

class OperationBindingHttp(BaseModel):

    """
    Operation Binding Protocol-specific information for an HTTP operation.
    Example - https://github.com/asyncapi/bindings/blob/master/http/README.md#example
    """

    op_type: str
    """Required. Type of operation. Its value MUST be either request or response."""

    method: str = Field(
        regex=r"^(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|CONNECT|TRACE)$"
    )
    """When type is request, this is the HTTP method, otherwise it MUST be ignored. Its value MUST be one of GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, CONNECT, and TRACE."""

    query: Schema
    """Object A Schema object containing the definitions for each query parameter. This schema MUST be of type object and have a properties key."""

    bindingVersion: str
    """The version of this binding. If omitted, "latest" MUST be assumed."""



class OperationBindingWebSocket:
    pass


class OperationBindingKafka:
    pass


class OperationBindingAMPQ:
    pass


class OperationBindingAMPQ1:
    pass


class OperationBindingMQTT:
    pass


class OperationBindingMQTT5:
    pass


class OperationBindingNATS:
    pass


class OperationBindingJMS:
    pass


class OperationBindingSNS:
    pass


class OperationBindingSQS:
    pass


class OperationBindingSTOMP:
    pass


class OperationBindingRedis:
    pass


OperationBinding = Any[
    OperationBindingHttp,
    OperationBindingWebSocket,
    OperationBindingKafka,
    OperationBindingAMPQ,
    OperationBindingAMPQ1,
    OperationBindingMQTT,
    OperationBindingMQTT5,
    OperationBindingNATS,
    OperationBindingJMS,
    OperationBindingSNS,
    OperationBindingSQS,
    OperationBindingSTOMP,
    OperationBindingRedis,
]
