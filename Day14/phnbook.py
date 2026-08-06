name = input("Enter a contact name: ")
def phone_book():
    contacts = {
        "Alice": "123-456-7890",
        "Bob": "987-654-3210",
        "Charlie": "555-555-5555"
    }
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f"{name} is not in the phone book."

print(phone_book())