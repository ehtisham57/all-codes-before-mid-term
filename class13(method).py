#defing method or functions of a class other than __init__
class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for x in self.marks:
            sum=sum+x
            average=sum/len(self.marks)
        return average
    def result(self):
        if self.avg()>=50:    
            print('pass')
        else:
            print('fail')
s1=student('arshad',[89,90,92,79])
print(s1.name,s1.marks)
print(s1.avg())
s1.result()
s2=student('imran',[100,90,92,79])
print(s2.name,s2.marks)
print(s2.avg())
s2.result()

            
        