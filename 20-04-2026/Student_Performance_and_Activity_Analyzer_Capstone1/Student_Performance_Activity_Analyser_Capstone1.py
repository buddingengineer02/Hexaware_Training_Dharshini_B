#Python Capstone Project

#Student Performance and Activity Analyzer
"""
Objective

Build a Python program that reads data from:
    students.txt
    marks.json
    attendance.csv
Then analyze the data and generate a final summary report.
"""

import json
import csv

#PART 1 - FILE HANDLING

# Task 1 - Read students.txt and print all names.
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

# Task 2 - Count the total number of entries in students.txt .
with open("students.txt", "r") as file:
    students = file.readlines()
print("Total number of Entries:", len(students))

#Task 3 - Find the unique student names using a set.
unique_students = set()
with open("students.txt", "r") as file:
    for line in file:
        unique_students.add(line.strip())
print("Unique students:", unique_students)

# Task 4 - Count how many times each student name appears using a dictionary.
name_count = {}
with open("students.txt", "r") as file:
    for line in file:
        name = line.strip()
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
print("count of student name:", name_count)

#Task 5 - Write the unique student names into a new file called unique_students.txt .
unique_students = set()

with open("students.txt", "r") as file:
    for line in file:
        unique_students.add(line.strip())
with open("unique_students.txt", "w") as file:
    for name in unique_students:
        file.write(name + "\n")

# PART 2 - JSON HANDLING

# Task 6 - Read marks.json
with open("marks.json", "r") as file:
    data = json.load(file)
print(data)
# Task 7 - Print all student names and marks
for student in data["students"]:
    print(student["name"], student["marks"])

# Task 8 - Find student with highest marks
high_marks = data["students"][0]
for student in data["students"]:
    if student["marks"] > high_marks["marks"]:
        high_marks = student
print("Topper:", high_marks["name"], high_marks["marks"])

# Task 9 - Find student with lowest marks
low = data["students"][0]
for student in data["students"]:
    if student["marks"] < low["marks"]:
        low = student
print("Lowest:", low["name"], low["marks"])

# Task 10 - Calculate average marks
total_marks = 0
for student in data["students"]:
    total_marks += student["marks"]
average = total_marks / len(data["students"])
print("Average Marks:", average)

# Task 11 - Print only students enrolled in the Python course.
print("Python students:")
for student in data["students"]:
    if student["course"] == "Python":
        print(student["name"])

# Task 12 - Count how many students are there in each course using a dictionary.
course_count = {}
for student in data["students"]:
    course = student["course"]
    if course in course_count:
        course_count[course] += 1
    else:
        course_count[course] = 1
print("Course Count:", course_count)


# PART 3 - CSV HANDLING

# Task 13 - Read attendance.csv
with open("attendance.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
with open("attendance.csv", "r") as file:
    reader = csv.DictReader(file)
    attendance_data = list(reader)
# Task 14 - Print each student's attendance details
for row in attendance_data:
    print(row["name"], row["days_present"], row["total_days"])

# Task 15 - Calculate attendance percentage for each student
attendance_percent = {}
for row in attendance_data:
    name = row["name"]
    days_present = int(row["days_present"])
    total_days = int(row["total_days"])
    percent = (days_present / total_days) * 100
    attendance_percent[name] = percent
    print(name, "Attendance % =", percent)

# Task 16 - Print students whose attendance is below 80%
print("Below 80% Attendance:")
for name in attendance_percent:
    if attendance_percent[name] < 80:
        print(name)

# Task 17 - Find student with best attendance
best_attendance = list(attendance_percent.keys())[0]
for name in attendance_percent:
    if attendance_percent[name] > attendance_percent[best_attendance]:
        best_attendance = name
print("Best Attendance:", best_attendance, attendance_percent[best_attendance])

# PART 4 - DATA STRUCTURES

# Task 18 - Store all marks in list and print highest marks, lowest marks, sum of marks
mark_list = []
for student in data["students"]:
    mark_list.append(student["marks"])

print("Highest Mark:", max(mark_list))
print("Lowest Mark:", min(mark_list))
print("Sum of Mark:", sum(mark_list))

# Task 19 - Create tuple of all courses and print it
course_tuple = ()
for student in data["students"]:
    course_tuple = course_tuple + (student["course"],)
print("Courses Tuple:", course_tuple)

# Task 20 - Create a set of all courses to show unique courses.
course_set = set(course_tuple)
print("Unique courses:", course_set)

# Task 21 - Create a dictionary where: key = student name value = marks
mark_dict = {}
for student in data["students"]:
    mark_dict[student["name"]] = student["marks"]
print("Marks dictionary:", mark_dict)

# Task 22 - Create a second dictionary where: key = student name value = attendance percentage
attendance_dict = {}
for name in attendance_percent:
    attendance_dict[name] = attendance_percent[name]
print("Attendance Dictionary:", attendance_dict)


# PART 5 - CONDITIONS AND LOOPS

# Task 23 - Using a loop, print whether each student is: "Pass" if marks >= 50 "Fail" otherwise
for student in data["students"]:
    if student["marks"] >= 50:
        print(student["name"], "Pass")
    else:
        print(student["name"], "Fail")

# Task 24 - Using conditions, assign grades:
# 90 and above → A
# 75 to 89 → B
# 50 to 74 → C
# below 50 → Fail
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"

for student in data["students"]:
    print(student["name"], "-", get_grade(student["marks"]))

# Task 25 - Print all students who have: marks above 80 attendance above 85%
print("Students with marks above 80 and attendance above 85%:")
for student in data["students"]:
    name = student["name"]
    if student["marks"] > 80 and attendance_percent[name] > 85:
        print(name)

# PART 6 - FUNCTIONS

# Task 26 - A function to read names from students.txt .
def read_names():
    with open("students.txt", "r") as file:
        return file.read().splitlines()

# Task 27 - A function to load student marks from marks.json
def load_marks():
    with open("marks.json", "r") as file:
        data = json.load(file)
    return data["students"]

# Task 28 - A function to load attendance from attendance.csv
def load_attendance():
    attendance_list = []
    with open("attendance.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            attendance_list.append(row)
    return attendance_list

# Task 29 - A function to calculate average marks
def calculate_average_marks(student_data):
    total = 0
    for student in student_data:
        total += student["marks"]
    return total / len(student_data)

# Task 30 - A function to calculate attendance percentage
def calculate_attendance_percentage(days_present, total_days):
    return (days_present / total_days) * 100

# Task 31 - A function to return topper
def return_topper(student_data):
    top = student_data[0]
    for student in student_data:
        if student["marks"] > top["marks"]:
            top = student
    return top

# Task 32 - A function to generate grade for a mark
def generate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"
    

# PART 7 - FINAL COMBINED ANALYSIS

# Task 33 - Combine marks and attendance data and create a final structure like this:
"""
{
"Rahul": {"marks": 85, "attendance": 88.0, "course": "Python"},
"Sneha": {"marks": 92, "attendance": 96.0, "course": "Data Engineerin
}
"""
final_data = {}

for student in data["students"]:
    name = student["name"]
    final_data[name] = {
        "marks": student["marks"],
        "attendance": attendance_percent[name],
        "course": student["course"]
    }

print(final_data)

# Task 34 - From this combined structure, print: name marks attendance course grade
for name in final_data:
    marks = final_data[name]["marks"]
    attendance = final_data[name]["attendance"]
    course = final_data[name]["course"]
    grade= get_grade(marks)

    print(name, "- Marks:", marks, "- Attendance:", attendance, "- Course:", course, "- Grade:", grade)

# Task 35 - Find students who are eligible for certification.
# Condition:
# marks >= 75
# attendance >= 80
eligible = []
for name in final_data:
    if final_data[name]["marks"] >= 75 and final_data[name]["attendance"] >= 80:
        eligible.append(name)
print("Eligible students:", eligible)

# Task 36 - Find students who need improvement.
#Condition:
#marks < 75 or attendance < 80
student_improve = []
for name in final_data:
    if final_data[name]["marks"] < 75 or final_data[name]["attendance"] < 80:
        student_improve.append(name)
print("Students need improvement:", student_improve)


# PART 8 - OUTPUT FILE GENERATION

# Task 37 - Write final student summary to report.txt
with open("report.txt", "w") as file:
    file.write("Student Report\n")
    for name in final_data:
        marks = final_data[name]["marks"]
        attendance = final_data[name]["attendance"]
        grade = get_grade(marks)
        file.write(name + " - Marks: " + str(marks) + " - Attendance: " + str(attendance) + "% - Grade: " + grade + "\n")

# Task 38 - Write only eligible students to eligible_students.txt
with open("eligible_students.txt", "w") as file:
    for name in eligible:
        file.write(name + "\n")


# FINAL CHALLENGE

# Task 39 - Final console output
print("Topper:",high_marks["name"])
print("Best Attendance:", best_attendance)
print("Average Marks:", round(average, 1))
print("Eligible Students:", ", ".join(eligible))
print("Students Needing Improvement:", ", ".join(student_improve))

#Task 40 Make the program modular using functions and keep the code clean.

# Function to find best attendance
def find_best_attendance(attendance_percent):
    best = list(attendance_percent.keys())[0]
    for name in attendance_percent:
        if attendance_percent[name] > attendance_percent[best]:
            best = name
    return best


# Function to get eligible students
def get_eligible(final_data):
    eligible_list = []
    for name in final_data:
        if final_data[name]["marks"] >= 75 and final_data[name]["attendance"] >= 80:
            eligible_list.append(name)
    return eligible_list


# Function to find students needing improvement
def get_improvement(final_data):
    improve_list = []
    for name in final_data:
        if final_data[name]["marks"] < 75 or final_data[name]["attendance"] < 80:
            improve_list.append(name)
    return improve_list
# print("Best Attendance:", find_best_attendance(attendance_percent))
# print("Eligible Students:", ", ".join(get_eligible(final_data)))
# print("Students Needing Improvement:", ", ".join(get_improvement(final_data)))