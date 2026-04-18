# Read file
with open("logins.txt", "r") as file:
    names = [line.strip() for line in file]

#1. Read the file and print all names.
print(names)

# 2. Count the total number of login records.
print("Total logins:", len(names))

# 3. Find how many times each user logged in.
count = {}
for name in names:
    count[name] = count.get(name, 0) + 1
print(count)

# 4. Find the user who logged in the most.
max_user = max(count, key=count.get)
print("Most active user:", max_user)

# 5. Print the unique users.
print("Unique users:", set(names))