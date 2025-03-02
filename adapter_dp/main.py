from yes_bank_adapter import YesBankAdapter
from axis_adapter import AxisAdapter


if __name__ == "__main__":
    yad = YesBankAdapter()
    yad.check_balance(123)
    yad.send_money()

    print("--------- changing the bank now ----------")

    aad = AxisAdapter()
    aad.check_balance(332)
    aad.send_money()