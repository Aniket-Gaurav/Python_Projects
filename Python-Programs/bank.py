
class BankAccount:
    """Represents a Bank Account"""

    def __init__(self, name, balance):
        """Create a new BankAccount object

        Args:
            name (str): The name of the account holder
            balance (int): The initial balance of the account
        """
        self.account_holder = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money in the account

        Args:
            amount (int): The amount to deposit
        """
        self.balance += amount
        print(f"Deposited amount is {amount}")

    def withdraw(self, amount):
        """Withdraw money from the account

        Args:
            amount (int): The amount to withdraw

        Raises:
            ValueError: If the balance is insufficient
        """
        if self.balance >= amount:
            print("Withdrawing", amount)
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def __str__(self):
        """Return a string representation of the account"""
        return f"Account Holder: {self.account_holder}\nBalance: {self.balance}"


name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))
obj = BankAccount(name, balance)
print(obj)
amount = int(input("Enter amount to deposit: "))
obj.deposit(amount)
amount = int(input("Enter amount to withdraw: "))
obj.withdraw(amount)
print(obj)
