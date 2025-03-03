from payment_strgy import PaymentStrgy

class CreditCard(PaymentStrgy):
    def pay(self, amount):
        print(f"Paying {amount} via credit card")