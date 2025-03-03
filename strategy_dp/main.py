from payment_factory import PaymentFactory

if __name__  == "__main__":
    user_choice = input("Enter your choice: credit_card/debit_card: ")

    try:
        mode = PaymentFactory.get_strategy(user_choice)
        mode.pay(100)
    except Exception as err:
        print("err: ", err)