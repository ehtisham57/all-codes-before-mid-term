class car():
    brand='KIA'
    product='PICANTO'
    def __init__(self):#default contructor
        pass#do nothing
    def __init__(self,color,EN):#parameterized constructor
        self.color=color
        self.EN=EN
        print(self)
car1=car('red',553)
print(car1)
print(car1.brand,car1.product,car1.color,car1.EN,)