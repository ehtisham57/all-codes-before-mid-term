class account():
    def __init__(self,name,acc_no,pwd):
        self.name=name
        self.acc_no=acc_no
#         self.pwd=pwd
        self._pwd=pwd
    def showpwd(self):
        print(self._pwd)
acc1=account('laiba',123,456)
print(acc1.name,acc1.acc_no)
acc1.showpwd()