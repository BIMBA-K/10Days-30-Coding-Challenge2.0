with open("data.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to File Handling\n")

print("Data written successfully!")

with open("data.txt", "r") as file:
    print("\nReading Entire File:")
    print(file.read())

with open("data.txt", "r") as file:
    print("\nFirst Line:")
    print(file.readline())

with open("data.txt", "r") as file:
    print("\nAll Lines:")
    print(file.readlines())

with open("data.txt", "a") as file:
    file.write("Python is Awesome!\n")

print("\nNew Data Appended!")

with open("data.txt", "r") as file:
    print("\nUpdated File Content:")
    print(file.read())