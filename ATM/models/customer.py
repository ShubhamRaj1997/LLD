from ATM.enums.states import CustomerStatus
from ATM.models.account import Account
from ATM.models.bank import Bank
from ATM.models.card import Card


class Customer(object):
    def __init__(self, card: Card, name: str, dob: str, email: str, phone: str, status: CustomerStatus, bank: Bank,
                 account: Account):
        self.name = name
        self.card = card
        self.dob = dob
        self.email = email
        self.phone = phone
        self.status = status
        self.bank = bank
        self.account = account

    def make_transaction(self):
        pass


