#static method
class student():
    def __init(self):#default constructor
        pass#do nothing
    def __init__(self,full_name,roll_no,total_marks):#parameterized const
        self.name=full_name
        self.rollno=roll_no
        self.marks=total_marks
    @staticmethod#decorators
    def hello():#static method works with class level with no self parameter
        print('asalam o alaikum')
    def avg(self):#nonstaticmethod
        sum=0
        for x in self.marks:
            sum=sum+x
            average=sum/len(self.marks)
        print(sum,'your total marks')   
        print(average,'your average marks for each subj')
        return average        
s1=student('almas',123,[80,70,60,90,99])
print(s1.name,s1.rollno,s1.marks)
s1.hello()
s1.avg()




