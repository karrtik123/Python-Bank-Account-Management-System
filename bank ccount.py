class BankAccount:
    #constructor
    def __init__(self,name,account_number,balance):
        #store account details 

        self.name = name
        self.account_number = account_number
        self.balance = balance
        #deposite money 

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("amount deposted:",amount)
    #withdrawl 
    def withdraw(self,amount):
       if amount <= self.balance:
           self.balance = self.balance - amount
           print("Amount withdrawn:",amount)
       else:
           print("insufficient balance!")
    def show_balance(self):
        print("\n=====Account Details========")
        print("name",self.name)
        print("account number:",self.account_number)
        print("final balance:",self.balance)
name = input("enter your name:")
account_number = input("enter account number:")
balance = int(input("enter initial balance:"))
 # create object
b1 = BankAccount(name,account_number,balance)
deposit_amount = int(input("enter deposit amount:"))
b1.deposit(deposit_amount)
#ask user for withdrawl amount
withdraw_amount = int(input("enter the withdrawl amount:"))
b1.withdraw(withdraw_amount)
 #display final balance 
b1.show_balance()





    

        