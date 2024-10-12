#adding parameters to the  __init__ function
#exapmle_1
#defing atributes of object using __init_ function
class Student():
    def __init__(self,fullname,totalmarks):
        self.name=fullname
        self.marks=totalmarks
        print(self)
        print('adding new studens to the record')
s1=Student('arshad',92.92)
print(s1)
print(s1.name,s1.marks)
s2=Student('imrankhan',804)
print(s2.name,s2.marks)
