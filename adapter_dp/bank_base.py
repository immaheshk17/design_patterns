from abc import ABC, abstractmethod

class BankBase(ABC):

    @abstractmethod
    def send_money(self):
        pass

    @abstractmethod
    def check_balance(self, acc_id):
        pass