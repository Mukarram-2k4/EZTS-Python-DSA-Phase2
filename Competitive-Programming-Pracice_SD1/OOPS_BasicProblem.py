'''Write a python class BankAccount with attributes like account_number,balance,date_of_opening,customer_name and methods
like deposit,withdraw, and check_balance.
'''
class BankAccount:
    acc_no='xxxx1234'
    balance=5000.00
    date_of_opening='12-8-2023'
    cust_name='Melvin'
    def withdraw(self):
        wd=float(input("Enter the money to withdraw"))
        if wd<=self.balance:
            print(wd,"is withdrawn")
            self.balance=self.balance-wd
        else:
            print("Insufficient Balance")
    def deposit(self):
        dep=float(input("Enter the deposit money:"))
        self.balance=self.balance+dep
        print(dep,"has deposited into",self.cust_name,"account")
    def check_balance(self):
        print(self.balance,"is available")
s1=BankAccount()
s1.withdraw()
s1.deposit()
s1.check_balance()