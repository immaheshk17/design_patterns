from payment_strgy import PaymentStrgy

class DebitCard(PaymentStrgy):
    def pay(self, amount):
        print(f"Paying {amount} via debit card")