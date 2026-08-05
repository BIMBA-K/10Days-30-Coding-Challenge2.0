numbers=list(map(int,input("enter numbers: ").split()))
def listchallenge(numbers):
    if not numbers:
        return None  
    max_num = numbers[0]
    min_num = numbers[0]
    total=0
    avg=0
    for num in numbers:
        total+=num
        
    avg=total/len(numbers)
      
        
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
max_num, min_num, total, avg= listchallenge(numbers)

print(f"the maximum number is {max_num}")
print(f"the minimum number is {min_num}")
print(f"the sum of numbers is {total}")
print(f"the average of numbers is {avg}")



    