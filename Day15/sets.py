# Creating Sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set 1:", set1)
print("Set 2:", set2)

# add()
set1.add(70)
print("\nAfter add(70):", set1)

# remove()
set1.remove(20)
print("After remove(20):", set1)

# discard()
set1.discard(100)      # No error even though 100 doesn't exist
print("After discard(100):", set1)

# union()
print("\nUnion:", set1.union(set2))

# intersection()
print("Intersection:", set1.intersection(set2))

# difference()
print("Difference (set1 - set2):", set1.difference(set2))

# Length
print("\nLength of set1:", len(set1))

# Membership
print("Is 30 present?", 30 in set1)

# Looping through a set
print("\nElements in set1:")
for item in set1:
    print(item)

# Removing duplicates from a list
numbers = [10, 20, 10, 30, 40, 20, 50, 30]

unique_numbers = list(set(numbers))

print("\nOriginal List:", numbers)
print("Unique List:", unique_numbers)