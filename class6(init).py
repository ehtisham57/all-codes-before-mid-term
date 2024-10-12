#adding parameters to the  __init__ function
#exapmle_2
#defing atributes of object using __init_ function
class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print(self)
        print('adding new studens to the record')
s1=Student('arshad',92.92)
print(s1)
print(s1.name,s1.marks)
s2=Student('imrankhan',100)
print(s2.name,s2.marks)
