s=input("enter a string: ")
def count_vowels_consonants(s):
    v=0
    c=0
    for chr in s:
        if chr in "aeiouAEIOU":
            v += 1
        elif chr.isalpha():
            c += 1
        else:
            c += 0
    return v, c
v, c=count_vowels_consonants(s)
print(f"the number of vowels in your string is {v}")
print(f"the number of consonants in your string is {c}")