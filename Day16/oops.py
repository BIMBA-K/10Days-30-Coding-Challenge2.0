class Student:
    def __init__(self):
        self.name = ""
        self.marks = 0

student1 = Student()
student2 = Student()

student1.name = "Alex"
student1.marks = 95

student2.name = "John"
student2.marks = 82

print(student1.name, student1.marks)
print(student2.name, student2.marks)