# Tuple – Immutable
numbers = (10, 20, 30, 40, 50)
print(numbers)

# Length
print(len(numbers))

# Printing elements using loop
for num in numbers:
    print(num)

# Accessing elements
fruits = ("Apple", "Mango", "Banana", "Pineapple")
print(fruits[0])
print(fruits[1])

# Access from last
print(fruits[-1])
print(fruits[-2])

# Tuples cannot be modified
t = (10, 20, 30, 40)
# t[1] = 100   # This will give error (tuple is immutable)

# Packing
student = ("Rahul", 22, "Python")
print(student)

# Unpacking
name, age, course = student
print(name)
print(age)
print(course)

# Multiple data types
data = ("Arjun", 25, True, 500000.00)
print(data)