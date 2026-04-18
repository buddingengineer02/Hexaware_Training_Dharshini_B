import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

# 1. Print all employee names.
for e in employees:
    print(e["name"])

# 2 Find employees working in IT department.
for e in employees:
    if e["department"] == "IT":
        print(e["name"])

# 3. Calculate the average salary.
total = 0
for e in employees:
    total += int(e["salary"])

avg = total / len(employees)
print("Average salary:", avg)

# 4 Find the highest salary employee.
max_salary = 0
top_employee = ""
for e in employees:
    if int(e["salary"]) > max_salary:
        max_salary = int(e["salary"])
        top_employee = e["name"]
print("Highest salary:", top_employee)

# 5. Count how many employees belong to each department.
dept_count = {}
for e in employees:
    dept = e["department"]
    if dept in dept_count:
        dept_count[dept] += 1
    else:
        dept_count[dept] = 1
print(dept_count)