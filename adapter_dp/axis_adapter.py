from bank_base import BankBase
from axis_bank import AxisBank

class AxisAdapter(BankBase):
    def check_balance(self, acc_id):
        AxisBank.bal_check_ax(self, acc_id)

    def send_money(self):
        AxisBank.transf_bal_ax(self)
