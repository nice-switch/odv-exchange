import time

from uuid import uuid4, UUID
from exchange import enum


pending_exchanges = {}
killed_exchanges = {}


def kill_exchange(exchange_id: str):
    if pending_exchanges.get(exchange_id):
        killed_exchanges[exchange_id] = pending_exchanges[exchange_id]

        # NOTE bruh, why do I have to do this?? pending_exchanges[exchange_id] = None should work but NOOOOOOOO.
        del pending_exchanges[exchange_id]


class ExchangeInterface():
    def __init__(self, pending_lifetime: int):

        self.timed_out_threshold = time.time() + pending_lifetime

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
        if time.time() >= self.timed_out_threshold:
            raise Exception("Exchange has timed out!")

        self.exchange_status = enum.ExchangeStatus.COMPLETED

        kill_exchange(self.exchange_id.hex)


    