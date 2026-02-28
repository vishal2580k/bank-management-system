class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited Successfully!")
        else:
            print("Invalid Amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        elif amount <= 0:
            print("Invalid Amount!")
        else:
            self.balance -= amount
            print("Withdrawal Successful!")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_no = input("Enter Account Number: ")
        name = input("Enter Account Holder Name: ")
        if acc_no in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[acc_no] = BankAccount(acc_no, name)
            print("Account Created Successfully!")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no, None)

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            for acc in self.accounts.values():
                print(f"Account No: {acc.account_number}, Name: {acc.name}, Balance: ₹{acc.balance}")


def main():
    bank = Bank()

    while True:
        print("\n====== Bank Management System ======")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Show All Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            acc_no = input("Enter Account Number: ")
            account = bank.get_account(acc_no)
            if account:
                amount = float(input("Enter Amount to Deposit: "))
                account.deposit(amount)
            else:
                print("Account Not Found!")

        elif choice == "3":
            acc_no = input("Enter Account Number: ")
            account = bank.get_account(acc_no)
            if account:
                amount = float(input("Enter Amount to Withdraw: "))
                account.withdraw(amount)
            else:
                print("Account Not Found!")

        elif choice == "4":
            acc_no = input("Enter Account Number: ")
            account = bank.get_account(acc_no)
            if account:
                account.check_balance()
            else:
                print("Account Not Found!")

        elif choice == "5":
            bank.show_all_accounts()

        elif choice == "6":
            print("Thank you for using Bank Management System!")
            break

        else:
            print("Invalid Choice! Try Again.")


if __name__ == "__main__":
    main()