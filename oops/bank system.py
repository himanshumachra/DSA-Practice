import sys

class BankAccount:
    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount, entered_pin):
        if entered_pin != self.pin:
            print("Incorrect PIN! Transaction cancelled.")
            return
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.balance}")

    def check_balance(self, entered_pin):
        if entered_pin != self.pin:
            print("Incorrect PIN! Cannot show balance.")
        else:
            print(f"Account Balance: ₹{self.balance}")


# Sample usage
if __name__ == "__main__":
    # Create a new account
    account = BankAccount("Anuj Kumar", "1234567890", "4321", 1000)

    while True:
        print("\n--- Mini Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == "2":
            amt = float(input("Enter amount to withdraw: "))
            pin = input("Enter your PIN: ")
            account.withdraw(amt, pin)
        elif choice == "3":
            pin = input("Enter your PIN: ")
            account.check_balance(pin)
        elif choice == "4":
            print("Thank you for using Mini Bank!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")