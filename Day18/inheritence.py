class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog1 = Dog()

dog1.eat()
dog1.bark()