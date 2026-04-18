# Exercise 3 – Student Marks Analyzer
students = {
    "Rahul": 85,
    "Sneha": 92,
    "Arjun": 78,
    "Priya": 88
}

topper = max(students, key=students.get)
average = sum(students.values()) / len(students)
#1. Print the topper
print("Topper:", topper, "-", students[topper])
#2. Print average marks
print("Average marks:", average)
#3. Print students scoring above 85
print("Students scoring above 85:")
for name, marks in students.items():
    if marks > 85:
        print(name,'-', marks)