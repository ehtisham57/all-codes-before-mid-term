#defing method or functions of a class other than __init__
#alternate_method
class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for x in self.marks:
            #sum+=sum
            sum=sum+x
        print('hi',self.name,'your avg is:',sum/len(self.marks))
s1=student('arshad',[89,90,92])
s1.avg()
            
        