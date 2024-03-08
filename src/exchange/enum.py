import enum


class ExchangeStatus(enum.Enum):
    DEAD = "dead"
    ALIVE = "alive"
    PENDING = "pending"


class ClientType(enum.Enum):
    REQUESTER = "requester"
    RESPONDER = "responder"