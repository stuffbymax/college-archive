class Bank:
    def __init__(self):
        self.bal = 0
        self.loan_bal = 0
        self.credit_limit = 0
        self.debit_limit = 0
        self.credit_loan = False
        self.debit_loan = False
        self.interest_rate = 0.005
        print("THE BANK ACC DEPOSIT AND WITHDRAW")

    def deposit(self, amt):
        self.bal += amt
        print(f"Your account balance is {self.bal:.2f}")

    def withdraw(self, amt):
        if self.bal >= amt:
            self.bal -= amt
            print(f"Your new balance is  {self.bal:.2f}")
        else:
            print('Insufficient balance')

    def show(self):
        print(f"Your account balance is {self.bal:.2f}")

    def enquiry(self):
        print(f"Your account balance is {self.bal:.2f}")

    def credit(self, amt):
        if self.bal + amt <= self.credit_limit:
            self.bal += amt
            print(f"Credit of {amt:.2f} applied. New balance: {self.bal:.2f}")
        else:
            print("Credit amount is greater than credit limit")

    def debit(self, amt):
        if amt <= self.debit_limit:
            if self.bal >= amt:
                self.bal -= amt
                print(f"Debit of {amt:.2f} applied. New balance: {self.bal:.2f}")
            else:
                print('Insufficient balance')
        else:
            print("Debit amount is greater than debit limit")

    def set_loan_credit(self):
      self.credit_loan = True
      print("Credit loan option enabled for this account")

    def set_loan_debit(self):
      self.debit_loan = True
      print("Debit loan option enabled for this account")

    def set_credit_limit(self, limit):
      self.credit_limit = limit
      print(f"Credit limit is now {limit:.2f}")

    def set_debit_limit(self, limit):
      self.debit_limit = limit
      print(f"Debit limit is now {limit:.2f}")

    def credit_loan_amount(self, amt):
        if self.credit_loan:
            self.loan_bal += amt
            print(f"Credit Loan amount of {amt:.2f} applied. Total Loan Balance is now: {self.loan_bal:.2f}")
        else:
            print("Credit Loan is disabled")

    def debit_loan_amount(self, amt):
      if self.debit_loan:
         if self.loan_bal >= amt:
            self.loan_bal -= amt
            print(f"Debit Loan amount of {amt:.2f} applied. Total Loan Balance is now: {self.loan_bal:.2f}")
         else:
              print("Debit Loan is enabled but there is no loan amount to remove.")
      else:
          print("Debit loan is not enabled")

    def show_balance(self):
      print(f"Current balance is: {self.bal:.2f}")

    def show_loan_detail(self):
        print(f"Current Loan Balance is: {self.loan_bal:.2f}")

    def show_all_details(self):
        print(f"Current Balance is {self.bal:.2f}, Current loan Balance is: {self.loan_bal:.2f}, Credit Limit: {self.credit_limit:.2f}, Debit Limit: {self.debit_limit:.2f}, Credit loan status: {self.credit_loan}, Debit Loan status: {self.debit_loan}")

    def show_credit_limit(self):
      print(f"Current Credit Limit is: {self.credit_limit:.2f}")

    def show_debit_limit(self):
      print(f"Current Debit Limit is: {self.debit_limit:.2f}")

    def apply_interest(self):
        """Applies monthly interest to the account balance."""
        interest_amount = self.bal * self.interest_rate
        self.bal += interest_amount
        print(f"Interest of {interest_amount:.2f} applied. New balance: {self.bal:.2f}")



class Menu:
    def __init__(self, bank):
        self.bank = bank

    def display_menu(self):
        print("\nBank Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Credit (to balance)")
        print("5. Debit (from balance)")
        print("6. Enable Credit Loan")
        print("7. Enable Debit Loan")
        print("8. Set Credit Limit")
        print("9. Set Debit Limit")
        print("10. Credit Loan Amount")
        print("11. Debit Loan Amount")
        print("12. Show Balance")
        print("13. Show Loan Detail")
        print("14. Show All Details")
        print("15. Show Credit Limit")
        print("16. Show Debit Limit")
        print("17. Apply Monthly Interest")
        print("18. Exit")


    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                amt = float(input("Enter amount to deposit: "))
                self.bank.deposit(amt)
            elif choice == '2':
                amt = float(input("Enter amount to withdraw: "))
                self.bank.withdraw(amt)
            elif choice == '3':
                self.bank.show()
            elif choice == '4':
              amt = float(input("Enter amount to Credit: "))
              self.bank.credit(amt)
            elif choice == '5':
              amt = float(input("Enter amount to debit: "))
              self.bank.debit(amt)
            elif choice == '6':
              self.bank.set_loan_credit()
            elif choice == '7':
                self.bank.set_loan_debit()
            elif choice == '8':
              limit = float(input("Enter amount for credit limit: "))
              self.bank.set_credit_limit(limit)
            elif choice == '9':
              limit = float(input("Enter amount for debit limit: "))
              self.bank.set_debit_limit(limit)
            elif choice == '10':
                amt = float(input("Enter loan amount to credit: "))
                self.bank.credit_loan_amount(amt)
            elif choice == '11':
               amt = float(input("Enter loan amount to debit: "))
               self.bank.debit_loan_amount(amt)
            elif choice == '12':
                self.bank.show_balance()
            elif choice == '13':
              self.bank.show_loan_detail()
            elif choice == '14':
              self.bank.show_all_details()
            elif choice == '15':
                self.bank.show_credit_limit()
            elif choice == '16':
              self.bank.show_debit_limit()
            elif choice == '17': # Added apply interest logic
                self.bank.apply_interest()
            elif choice == '18':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    account = Bank()
    menu = Menu(account)
    menu.run()
