from ATM.models.account import Account


class Bank(object):
    def __init__(self, bank_id, bank_name):
        self.__customer_accounts = []
        self.__branches = []

    def get_customer_account_info(self, customer_id) -> Account:
        pass

    def transfer_fund(self, customer_id, receiver_info):
        pass


class SBI(Bank):
    def __init__(self, bank_id, bank_name):
        super().__init__(bank_id, bank_name)

    def get_customer_account_info(self, customer_id):
        return Account(customer_id)

