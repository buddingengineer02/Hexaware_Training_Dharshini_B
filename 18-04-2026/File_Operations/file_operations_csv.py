import csv

# READ CSV
with open("data.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# data.csv contains:
# name,marks
# Rahul,85
# Priya,90
# Arjun,88

# Output:
# ['name', 'marks']
# ['Rahul', '85']
# ['Priya', '90']
# ['Arjun', '88']


# READ CSV AS DICTIONARY
with open("data.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["marks"])

# Output:
# Rahul 85
# Priya 90
# Arjun 88


# WRITE CSV FILE
data = [
    ["name","marks"],
    ["priya",90],
    ["karen",89]
]

with open("output.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# output.csv content:
# name,marks
# priya,90
# karen,89