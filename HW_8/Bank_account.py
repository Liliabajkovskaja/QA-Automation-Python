class UserAccount:
    bank_name = "PRIVATE"

    @staticmethod
    def validate_iban(iban):
        if len(iban) == 12 and iban.startswith("UA"):
            return True
        else:
            return False

    @classmethod
    def print_name_bank(cls):
        print(cls.bank_name)
        return cls.bank_name

    def __init__(self, name, card_number, balance):
        self.name = name
        self._card_number = card_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):

        self.__balance = new_balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
        else:
            print("Invalid amount for deposit.")


account = UserAccount("Vova", "1234567890", 5000)

print("Balance:", account.balance)

account.withdraw(100)
account.deposit(200)
print(account.validate_iban("UA1234567890"))
account.print_name_bank()
