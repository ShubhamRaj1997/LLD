import datetime

from ATM.enums.states import TxnStatus
from ATM.models.bank import Bank


class Transaction(object):
    def __init__(self, tid: int, status: TxnStatus):
        self.tid = tid
        self.status = status
        self.creation_time = datetime.datetime.now()


class SelfTransaction(object):
    pass


class CashWithdrawlTxn(Transaction):
    def __init__(self, account_id: str, amount: int, bank: Bank, tid: int, status: TxnStatus):
        super().__init__(tid, status)
        self.account_id = account_id
        self.amount = amount
        self.bank = bank

    def get_amount(self):
        return self.amount


class BalanceEnquiryTxn(Transaction):
    def __init__(self, account_id: str, tid: int, status: TxnStatus):
        super().__init__(tid, status)
        self.account_id = account_id

    def get_amount(self, bank: Bank):
        account = bank.get_customer_account_info(self.account_id)
        return account.available_balance


class DepositTxn(Transaction):
    def __init__(self, account_id: str, amount: float, tid: int, status: TxnStatus):
        super().__init__(tid, status)
        self.account_id = account_id
        self.amount = amount

    def get_amount(self):
        return self.amount


class FundTransferTxn(Transaction):
    def __init__(self, sender_id: str, receiver_info, amount: float, tid: int, status: TxnStatus):
        super().__init__(tid, status)
        self.sender_id = sender_id
        self.receiver_info = receiver_info
        self.amount = amount

    def get_amount(self):
        return self.get_amount()

    def transfer_fund(self, bank:Bank):
        bank.transfer_fund(self.sender_id, self.receiver_info)

