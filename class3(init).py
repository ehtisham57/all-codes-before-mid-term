#constructor or __init__ function
#exapmle_1
#built_in constructor/special-funtionofclass/special method
class car():
    brand='KIA'
    def __init__(self):
        print(self)
        print('adding new car to the showroom')
car1=car()
print(car1)
print(car1.brand)