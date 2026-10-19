class BankAccount:
  def __init__(self, accountnumber: int, balance: float):
    self.__accountnumber = None
    self.__balance = 0.0

    self.set_accountnumber(account_number)
    self.set_balance(balance)

  @property
  def accountnumber(self):
    return self.__accountnumber

  @accountnumber.setter
  def accountnumber(self, value: int):
    self.__accountnumber= value

  @property
  def balance(self):
    return self.__balance

  @balance.setter
  def balance(self, value: float): 
    if value<0:
      print("The balance must not be a negative number.")
    else:
      self.__balance=value

if __name__=="__main__":
  a1=BankAccount(12345,1000)

print("Account 1")
print(f"Account Number: {a1.accountnumber}")
print(f"Balance: {al.balance: .2f}/n")

print("Update balance to -100")
a1.balance=-100

print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance: .2f}")

