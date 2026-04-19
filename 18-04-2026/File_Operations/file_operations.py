with open("data.txt","r") as file:
    for line in file:
        print(line.strip())

# Output:
# (prints all lines from data.txt one by one)
# Example:
# Rahul
# Priya
# Arjun
# Neha
# Kiran


with open("data.txt","r") as file:
    students=file.readlines()
print("Total Students: ",len(students))

# Output:
# Total Students: 5


total=0
with open("data1.txt","r") as file:
    for line in file:
        total+=int(line.strip())
print("Total =",total)

# data1.txt contains:
# 10
# 20
# 30
# 40
# 50

# Output:
# Total = 150


#WRITE MODE-override
with open("data.txt","w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Rachel\n")

# File content after this:
# Rahul
# Priya
# Rachel


#APPEND MODE-it will not override
with open("data.txt","a") as file:
    file.write("Neha\n")

# File content after this:
# Rahul
# Priya
# Rachel
# Neha


languages=["Python\n","Java\n","C++\n"]
with open("data2.txt","w") as file:
    file.writelines(languages)

# File content of data2.txt:
# Python
# Java
# C++