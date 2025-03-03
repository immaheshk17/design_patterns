from credit_card import CreditCard
from debit_card import DebitCard

class PaymentFactory:
    strategies = {
        'credit_card': CreditCard,
        'debit_card': DebitCard
    }

    @staticmethod
    def get_strategy(mode):
        available_modes = PaymentFactory.strategies.get(mode)
        if not available_modes:
            raise ValueError(f'Unknown payment mode: {mode}')

        return available_modes()