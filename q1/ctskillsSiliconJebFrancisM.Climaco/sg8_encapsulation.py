class BankAccount:
    def __init__(self, accountnumber: int, balance: float):
        # Initialize private attributes that prevents external code from accessing or modifying sensitive fields directly
        self.__accountnumber = None
        self.__balance = 0.0

        # Assigns parameters via property setterst at initialization which ensures starting values undergo the exact same validation as future updates.
        self.accountnumber = accountnumber
        self.balance = balance

    # Returns the private account number allowing safe read-only access from outside the class.
    @property
    def accountnumber(self):
        return self.__accountnumber

    # Updates the private account number attribute when assigned a new integer value.
    @accountnumber.setter
    def accountnumber(self, value: int):
        self.__accountnumber = value

    # Returns the private balance allowing safe read-only access from outside the class.
    @property
    def balance(self):
        return self.__balance

    # Validates that the input value is non-negative before updating the private balance attribute.
    @balance.setter
    def balance(self, value: float): 
        if value < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = value

# Demonstrates class functionality and verifies validation logic against the sample output.
if __name__ == "__main__":
  # Creates a new BankAccount instance with valid initial details. 
  a1 = BankAccount(12345, 1000)

    # Displays initial account number and formatted balance.
    print("Account 1")
    print(f"Account Number: {a1.accountnumber}")
    print(f"Balance: {a1.balance:.2f}\n")

    # Attempts an invalid balance update to trigger validation error messaging.
    print("Update balance to -100")
    a1.balance = -100

    # Confirms account number and balance remained unchanged after invalid assignment.
    print(f"Account Number: {a1.accountnumber}")
    print(f"Balance: {a1.balance:.2f}")
