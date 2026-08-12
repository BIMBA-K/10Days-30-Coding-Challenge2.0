class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def introduce(self):
        print(f"My name is {self.name}")

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")