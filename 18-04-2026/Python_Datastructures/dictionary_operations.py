# Dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print(student)
print(student["name"])
print(student["age"])
print(student["course"])

# Using get()
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))

# Add new key-value
student["city"] = "Hyderabad"
print(student)