from bank_base import BankBase
from yes_bank import YesBank

class YesBankAdapter(BankBase):
    def check_balance(self, acc_no):
        YesBank.fetch_balance(self, acc_no)

    def send_money(self):
        YesBank.money_transfer(self)
