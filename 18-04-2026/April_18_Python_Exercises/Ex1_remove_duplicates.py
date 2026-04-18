# Exercise 1 – Remove Duplicates from a List
customers = [101, 102, 103, 101, 104, 102, 105]
#1. Remove duplicate IDs
unique_customers = list(set(customers))
#2. Print unique customers
print("Unique customers:", unique_customers)
#3. Print total number of unique customers
print("Total unique customers:", len(unique_customers))