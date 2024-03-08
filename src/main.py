import exchange

# TODO make it work!

"""
    Module for Overseer Data Exchange.
    This module is the "exchange" part of the project(shocking I know)..
"""

exchange_session = exchange.interface.ExchangeInterface()

print(exchange_session.get_receiver_id())
print(exchange_session.get_sender_id())