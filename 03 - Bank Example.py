class Account():
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"Account owner: {self.owner} & Account balance: {self.balance}"
    
    def Deposit(self,deposit):
        self.balance = self.balance + deposit
        print("Deposit accepted.")
        
    def Withdraw(self,withdraw):
        if self.balance >= withdraw:
            self.balance = self.balance - withdraw
            print("Withdraw accepted.")
        else:
            print("Funds unavailable.")
        
        
account1 = Account("Jose",100)

print(str(account1))

print(str(account1.owner))
print(str(account1.balance))

account1.Deposit(50)
account1.Withdraw(75)
account1.Withdraw(500)