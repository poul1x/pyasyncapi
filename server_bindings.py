from typing import Any

class ServerBindingHttp:
    """
    Server Binding Protocol-specific information for an HTTP server.
    This object MUST NOT contain any properties. Its name is reserved for future use.
    """

    pass


class ServerBindingWebSocket:
    pass


class ServerBindingKafka:
    pass


class ServerBindingAMPQ:
    pass


class ServerBindingAMPQ1:
    pass


class ServerBindingMQTT:
    pass


class ServerBindingMQTT5:
    pass


class ServerBindingNATS:
    pass


class ServerBindingJMS:
    pass


class ServerBindingSNS:
    pass


class ServerBindingSQS:
    pass


class ServerBindingSTOMP:
    pass


class ServerBindingRedis:
    pass


ServerBinding = Any[
    ServerBindingHttp,
    ServerBindingWebSocket,
    ServerBindingKafka,
    ServerBindingAMPQ,
    ServerBindingAMPQ1,
    ServerBindingMQTT,
    ServerBindingMQTT5,
    ServerBindingNATS,
    ServerBindingJMS,
    ServerBindingSNS,
    ServerBindingSQS,
    ServerBindingSTOMP,
    ServerBindingRedis,
]
