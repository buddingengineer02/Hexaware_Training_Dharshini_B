# Set – does not allow duplicates
numbers = {10, 20, 30, 40}
print(numbers)

set1 = {10, 20, 20, 30, 30, 40, 40}
print(set1)

# List to Set
list1 = [10, 20, 20, 30, 30, 40, 40, 50]
unique_nums = set(list1)
print(unique_nums)

# Add element
numbers.add(60)
print(numbers)

# Update set
numbers.update([70, 80])
print(numbers)

# Union
set2 = {10, 20, 30}
set3 = {30, 40, 50}
result = set2.union(set3)
print(result)

# Difference
print(set2.difference(set3))
print(set3.difference(set2))

# Intersection
print(set2.intersection(set3))
