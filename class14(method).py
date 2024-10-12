class student():
    def __init(self):#default constructor
        pass#do nothing
    def __init__(self,full_name,roll_no,total_marks):#parameterized const
        self.name=full_name
        self.rollno=roll_no
        self.marks=total_marks
    def avg(self):#method
        sum=0
        for x in self.marks:
            sum=sum+x
            average=sum/len(self.marks)
        print(sum)   
        print(average,'your average marks')
        return average
    def result(self):#method
        if self.avg()>=60:
            print('pass')
        else:
            print('fail')
        
s1=student('almas',123,[80,70,60,90,99])
print(s1)
print(s1.name,s1.rollno,s1.marks)
s1.avg()
s1.result()
s2=student('sherz',345,[90,30,50,40,20])
print(s2)
print(s2.name,s2.rollno,s2.marks)
s2.avg()
s2.result()

