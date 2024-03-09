EXCHANGE_GARBAGE_LIFETIME = 5 # Lifetime of a accepted/denied or timed out exchange in killed_exchanges dictionary.

import time

from uuid import uuid4, UUID
from exchange import enum

pending_exchanges = {}
killed_exchanges = []


def kill_exchange(exchange_id: str):
    exchange_session = pending_exchanges.get(exchange_id)

    if exchange_session:

        exchange_session.garbage_threshold = time.time() + EXCHANGE_GARBAGE_LIFETIME
        killed_exchanges.append(exchange_session)

        # NOTE bruh, why do I have to do this?? pending_exchanges[exchange_id] = None should work but NOOOOOOOO.
        del pending_exchanges[exchange_id]


def clean_killed_exchanges():
    for exchange_session in killed_exchanges:
        if time.time() >= exchange_session.garbage_threshold:
            killed_exchanges.remove(exchange_session)


class ExchangeInterface():
    def __init__(self, pending_lifetime: int):

        self.pending_threshold: int = time.time() + pending_lifetime
        self.garbage_threshold: int = -1

        self.exchange_status: enum.ExchangeStatus = enum.ExchangeStatus.PENDING
        
        self.responder_id: UUID = uuid4()
        self.requester_id: UUID = uuid4()

        self.exchange_id: UUID = uuid4()

        pending_exchanges[self.exchange_id.hex] = self

    
    def get_responder_id(self) -> str:
        return self.responder_id.hex
    

    def get_requester_id(self) -> str:
        return self.requester_id.hex


    def deny_exchange(self):
        self.exchange_status = enum.ExchangeStatus.DEAD
        
        kill_exchange(self.exchange_id.hex)


    def accept_exchange(self):
        if time.time() >= self.pending_threshold:
            raise Exception("Exchange has timed out!")

        self.exchange_status = enum.ExchangeStatus.COMPLETED

        kill_exchange(self.exchange_id.hex)


