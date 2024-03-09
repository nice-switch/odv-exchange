import exchange

# TODO make it work!

"""
    Module for Overseer Data Exchange.
    This module is the "exchange" part of the project(shocking I know)..

    What this module is suppose to do:
        - Create a interface class that handles an exchange of data between two clients.
        - Two pipelines of data are created, one that the server can decrypt and one for relaying data for P2P data.
            - P2P data pipeline will not be accessible at all, only the requesting client and the response client can decrypt the data.
                (diffie-hellman exchange or attempt crystals kyber implementation?)
        
            
"""

exchange_session = exchange.interface.ExchangeInterface()

print(exchange_session.get_requester_id())
print(exchange_session.get_responder_id())

exchange_session.deny_exchange()

print(exchange.interface.killed_exchanges)
print(exchange.interface.pending_exchanges)