class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Bruno")
dog2 = Dog("Max")

dog1.bark()
dog2.bark()