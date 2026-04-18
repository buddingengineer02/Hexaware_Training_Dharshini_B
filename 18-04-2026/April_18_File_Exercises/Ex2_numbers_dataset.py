#Read all numbers
with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

# 1. Read all numbers from the file.
print(numbers)

# 2. Calculate the sum of all numbers.
print("Sum:", sum(numbers))

# 3. Find the maximum number.
print("Max:", max(numbers))

# 4. Find the minimum number.
print("Min:", min(numbers))

# 5. Count how many numbers are greater than 50.
count = 0
for n in numbers:
    if n > 50:
        count += 1
print("Count greater than 50:", count)