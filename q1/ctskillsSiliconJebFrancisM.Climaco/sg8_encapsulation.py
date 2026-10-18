class BankAccount:
  def __init__(self, account_number: int, balance: float):
    self.__account_number = None
    self.__balance = 0.0

    self.set_account_number(account_number)
    self.set_balance(balance)

