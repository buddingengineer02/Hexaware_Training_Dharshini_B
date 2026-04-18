import json

with open("students.json", "r") as file:
    data = json.load(file)

students = data["students"]

# 1. Print all student names.
for s in students:
    print(s["name"])

# 2. Print students enrolled in Python course.
for s in students:
    if s["course"] == "Python":
        print(s["name"])

# 3 Top student (normal way)
max_marks = 0
top_student = ""
for s in students:
    if s["marks"] > max_marks:
        max_marks = s["marks"]
        top_student = s["name"]
print("Top student:", top_student)

# 4. Calculate average marks.
total = 0
for s in students:
    total += s["marks"]

avg = total / len(students)
print("Average:", avg)

# 5. Count how many students are enrolled in each course.
course_count = {}
for s in students:
    course = s["course"]
    if course in course_count:
        course_count[course] += 1
    else:
        course_count[course] = 1
print(course_count)