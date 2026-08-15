class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car engine starts")

car = Car()
car.start()
