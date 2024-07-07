class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdraw amount")

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Added interest: {interest}")

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.interest_rate}%")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdraw amount, exceeds overdraft limit")

    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: {self.overdraft_limit}")

# Membuat objek dari kelas SavingsAccount dan CheckingAccount
savings_account = SavingsAccount("SA123", 1000, 5)
checking_account = CheckingAccount("CA456", 500, 200)

# Menampilkan informasi akun bank dan melakukan transaksi
savings_account.display_info()
savings_account.deposit(500)
savings_account.add_interest()
savings_account.display_info()
print()

checking_account.display_info()
checking_account.withdraw(600)
checking_account.withdraw(200)
checking_account.display_info()

# Menggunakan polymorphism
accounts = [
    SavingsAccount("SA789", 1500, 3),
    CheckingAccount("CA012", 800, 300)
]

for account in accounts:
    print()
    account.display_info()
    account.deposit(200)
    account.withdraw(100)
    account.display_info()
