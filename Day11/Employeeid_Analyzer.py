
def analyze_string(text):
    low=0
    upp=0
    dig=0
    spc=0
    for ch in text:
        if ch.isupper():
            upp+=1
        elif ch.islower():
            low+=1
        elif ch.isdigit():
            dig+=1
        else:
            spc+=1
    return low, upp, dig, spc
x=analyze_string("Hello, World! 123")
print(f"Lowercase letters: {x[0]}")
print(f"Uppercase letters: {x[1]}")
print(f"Digits: {x[2]}")
print(f"Special characters: {x[3]}")
