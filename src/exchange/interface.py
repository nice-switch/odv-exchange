from uuid import uuid4, UUID
from exchange import enum


class ExchangeInterface():
    def __init__(self):
        self.exchange_status: enum.ExchangeStatus = enum.ExchangeStatus.PENDING
        
        self.sender_id: UUID = uuid4()
        self.receiver_id: UUID = uuid4()

    
    def get_sender_id(self):
        return self.sender_id.hex
    

    def get_receiver_id(self):
        return self.receiver_id.hex
