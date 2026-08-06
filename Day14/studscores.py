name=input("Enter your student name: ")
def student_score():
    students = {
        "Alex": 85,
        "John": 92,
        "Sara": 76
    }
    if name in students:
        return f"{name}'s score is {students[name]}"
    else:
        return f"{name} is not in the student records."

print(student_score())