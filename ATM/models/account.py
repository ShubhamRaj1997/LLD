class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__total_balance = 0.0
        self.__available_balance = 0.0

    @property
    def available_balance(self):
        if self.__available_balance is None:
            # fetch from database service and set it
            pass
        return self.__available_balance

    @available_balance.setter
    def available_balance(self, available_balance):
        self.__available_balance = available_balance


class SavingsAccount(Account):
    def __init__(self, account_number):
        super().__init__(account_number)


class CurrentAccount(Account):
    def __init__(self, account_number):
        super().__init__(account_number)
        self.account_number = account_number
