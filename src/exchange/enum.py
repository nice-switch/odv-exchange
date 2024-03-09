import enum


class ExchangeStatus(enum.Enum):
    DEAD = "dead"
    ALIVE = "alive"
    PENDING = "pending"
    COMPLETED = "completed"


class ClientType(enum.Enum):
    REQUESTER = "requester"
    RESPONDER = "responder"