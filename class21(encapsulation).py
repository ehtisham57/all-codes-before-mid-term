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
        self.name=name
        self.color=color
        
car1=KIACAR('picanto','blue')#inheritance
print(car1.name,car1.color)
car1.start()
car1.stop()