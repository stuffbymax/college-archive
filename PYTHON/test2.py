class Bank:
    def __init__(self):
        self.bal = 0
        print ("THE BANK ACC DEPOSIT AND WITHDRWA")
    def deposit(self):
        amt= float(input ("enter ammount to deposit: "))
        self.bal = self.bal + amt
        print ("your account balance is %f" % self.bal)
    def withdraw(self):
        amt = float(input("Enter Ammount to withdraw"))
        if (self.bal >= amt):
            self.bal = self.bal - amt
            print ("your new ballance is  %f" % self.bal)
        else:
            print ('insuficent bal')
        def enqury(self):
            print ("Your account ballance is %f" % self.bal)

account = Bank()
account.deposit()
accont.withdraw()
accont.enqury()                  
