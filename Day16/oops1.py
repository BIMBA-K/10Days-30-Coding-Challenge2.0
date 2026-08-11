class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0

employee1 = Employee()
employee2 = Employee()

employee1.name = "Rahul"
employee1.salary = 30000

employee2.name = "Priya"
employee2.salary = 40000

print(employee1.name, employee1.salary)
print(employee2.name, employee2.salary)
