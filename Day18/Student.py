class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def introduce(self):
        super().introduce()
        print("I am a student")

student = Student()
student.introduce()
