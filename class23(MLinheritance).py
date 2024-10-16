class car():
    def __init__(self):
        self.clutch = False
        self.acc = False
        self.brk = False

    def start(self):
        self.clutch = True
        self.acc = True
        print('Car started')

    def stop(self):
        self.brk = True
        print('Car stopped')


class KIACAR(car):
    def __init__(self, name, color):
        super().__init__()  # Calling the parent class constructor
        self.name = name
        self.color = color


class PICANTO(KIACAR):
    def __init__(self, name, color, size):
        super().__init__(name, color)  # Calling the KIACAR constructor
        self.size = size


car1 = PICANTO('Kia Picanto', 'Red', '600CC')  # MULTI LEVEL inheritance
print(car1.name, car1.color, car1.size)
car1.start()
car1.stop()
