class car():
    def __init__(self):
        self.clutch=False
        self.acc=False
        self.brk=False
    def start(self):
        self.clutch=True
        self.acc=True
        print('car started')
    def stop(self):
        self.brk=True
        print('car stopped')
class KIACAR(car):
    def __init__(self,name,color):
        super().__init__()
        self.name=name
        self.color=color
class PICANTO(KIACAR):
    def __init__(self,name,color,size):
        super().__init__(name,color)
        self.size=size
        
car1=PICANTO('kiapicanto','red','600cc')#MULTI LEVEL inheritance
print(car1.name,car1.color,car1.size)
car1.start()
car1.stop()