# Exercise 2 – Frequency Counter
numbers = [10, 20, 10, 30, 20, 10, 40]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
#1. Count how many times each number appears
#2. Store the result in a dictionary
print("Frequency:", frequency)