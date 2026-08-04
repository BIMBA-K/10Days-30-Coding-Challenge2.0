# Creating a list
numbers = [10, 20, 30]

print("Original List:", numbers)

# append()
numbers.append(40)
print("After append:", numbers)

# insert()
numbers.insert(1, 15)
print("After insert:", numbers)

# remove()
numbers.remove(20)
print("After remove:", numbers)

# pop()
numbers.pop()
print("After pop:", numbers)

# extend()
numbers.extend([50, 60])
print("After extend:", numbers)

# sort()
numbers.sort()
print("After sort:", numbers)

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# index()
print("Index of 30:", numbers.index(30))

# count()
numbers.append(30)
print("After adding another 30:", numbers)
print("Count of 30:", numbers.count(30))