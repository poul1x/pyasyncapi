from typing import Any
from schema import Schema

class MessageBindingHttp:

    """
    Message Binding	Protocol-specific information for an HTTP message, i.e., a request or a response.
    This object contains information about the message representation in HTTP.

    Example - https://github.com/asyncapi/bindings/blob/master/http/README.md#message-binding-object
    """

    headers: Schema
    """Object	A Schema object containing the definitions for HTTP-specific headers. This schema MUST be of type object and have a properties key."""

    bindingVersion: str
    """The version of this binding. If omitted, "latest" MUST be assumed."""


class MessageBindingWebSocket:
    pass


class MessageBindingKafka:
    pass


class MessageBindingAMPQ:
    pass


class MessageBindingAMPQ1:
    pass


class MessageBindingMQTT:
    pass


class MessageBindingMQTT5:
    pass


class MessageBindingNATS:
    pass


class MessageBindingJMS:
    pass


class MessageBindingSNS:
    pass


class MessageBindingSQS:
    pass


class MessageBindingSTOMP:
    pass


class MessageBindingRedis:
    pass


MessageBinding = Any[
    MessageBindingHttp,
    MessageBindingWebSocket,
    MessageBindingKafka,
    MessageBindingAMPQ,
    MessageBindingAMPQ1,
    MessageBindingMQTT,
    MessageBindingMQTT5,
    MessageBindingNATS,
    MessageBindingJMS,
    MessageBindingSNS,
    MessageBindingSQS,
    MessageBindingSTOMP,
    MessageBindingRedis,
]
