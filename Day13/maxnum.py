numbers=list(map(int,input("enter numbers: ").split()))
def largest(numbers):
    if not numbers:
        return None  # Return None for an empty list
    max=numbers[0]
    for num in numbers[1:]:
        if num>max:
            max=num
    return max

print(largest(numbers))