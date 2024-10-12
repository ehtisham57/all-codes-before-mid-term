class acount():
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
    def debit(self,amount):
        self.balance=self.balance-amount
        print(amount,'was debited')
        print(self.netbalance(),'totalbalance')
    def credit(self,amount):
        self.balance=self.balance+amount
        print(amount,'was credited')
        print(self.netbalance(),'totalbalance')
    def netbalance(self):
        return self.balance
anfal=acount(12345,50000)
print(anfal.acc_no,anfal.balance)
anfal.credit(20000)
anfal.debit(40000)
print(anfal.netbalance())