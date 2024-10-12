class acount():
    def __init__(self,nam,acc_no,balance):
        self.nam=nam
        self.acc_no=acc_no
        self.balance=balance
    def credit(self,amount):
        self.balance=self.balance+amount
        print(amount,'was credited')
        print(self.netbalance(),'totalbalance')
    def debit(self,amount):
        self.balance=self.balance-amount
        print(amount,'was debited')
        print(self.netbalance(),'totalbalance')
    def netbalance(self):
        return self.balance    
acc1=acount('laraib',12345,50000)
print(acc1.nam,acc1.acc_no,acc1.balance)
acc1.credit(5000)
acc1.debit(1000)