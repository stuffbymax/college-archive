class BankAccount:
	
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def display_balance(self):
        print(f"Your current balance is: £{self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited £{amount:.2f}. New balance: £{self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
         if amount <= 0:
             print("Invalid withdraw amount. Please enter a positive value.")
             return
         if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew £{amount:.2f}. New balance: £{self.balance:.2f}")
         else:
            print("Insufficient funds. Cannot withdraw this amount.")

def main():
    account = BankAccount()

    while True:
        print("\nBanking Menu:")
        print("1. Display Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            account.display_balance()
        elif choice == '2':
            try:
               amount = float(input("Enter the amount to deposit: £"))
               account.deposit(amount)
            except ValueError:
                 print("Invalid input. Please enter a number")
        elif choice == '3':
            try:
               amount = float(input("Enter the amount to withdraw: £"))
               account.withdraw(amount)
            except ValueError:
                 print("Invalid input. Please enter a number")
        elif choice == '4':
            print("Exiting banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
