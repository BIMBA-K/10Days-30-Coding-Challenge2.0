class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        print(f"Car brand is {self.brand}")

    def check_speed(self):
        if self.speed >= 100:
            print("Fast Car")
        else:
            print("Normal Speed")


car = Car("BMW", 120)

car.display()
car.check_speed()
