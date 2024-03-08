from uuid import uuid4, UUID
from exchange import enum


class ExchangeInterface():
    def __init__(self):
        self.exchange_status: enum.ExchangeStatus = enum.ExchangeStatus.PENDING
        
        self.responder_id: UUID = uuid4()
        self.requester_id: UUID = uuid4()

    
    def get_responder_id(self) -> str:
        return self.sender_id.hex
    

    def get_requester_id(self) -> str:
        return self.receiver_id.hex
