from typing import Any

class ChannelBindingHttp:
    """
    Channel Binding Protocol-specific information for an HTTP server.
    This object MUST NOT contain any properties. Its name is reserved for future use.
    """

    pass


class ChannelBindingWebSocket:
    pass


class ChannelBindingKafka:
    pass


class ChannelBindingAMPQ:
    pass


class ChannelBindingAMPQ1:
    pass


class ChannelBindingMQTT:
    pass


class ChannelBindingMQTT5:
    pass


class ChannelBindingNATS:
    pass


class ChannelBindingJMS:
    pass


class ChannelBindingSNS:
    pass


class ChannelBindingSQS:
    pass


class ChannelBindingSTOMP:
    pass


class ChannelBindingRedis:
    pass


ChannelBinding = Any[
    ChannelBindingHttp,
    ChannelBindingWebSocket,
    ChannelBindingKafka,
    ChannelBindingAMPQ,
    ChannelBindingAMPQ1,
    ChannelBindingMQTT,
    ChannelBindingMQTT5,
    ChannelBindingNATS,
    ChannelBindingJMS,
    ChannelBindingSNS,
    ChannelBindingSQS,
    ChannelBindingSTOMP,
    ChannelBindingRedis,
]
