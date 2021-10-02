import datetime


class Card(object):
    def __init__(self, card_id: str, customer_name: str, card_expiry: datetime.datetime, pin: int):
        self.card_id = card_id
        self.customer_name = customer_name
        self.card_expiry = card_expiry
        self.pin = pin


