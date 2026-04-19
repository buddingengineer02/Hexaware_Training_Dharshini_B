import json

# READ JSON
with open("data.json","r") as file:
    data = json.load(file)
print(data)

# data.json contains:
# {
#   "students": [
#     {"name": "Rahul", "marks": 85},
#     {"name": "Priya", "marks": 90},
#     {"name": "Arjun", "marks": 88}
#   ]
# }

# Output:
# {'students': [{'name': 'Rahul', 'marks': 85}, {'name': 'Priya', 'marks': 90}, {'name': 'Arjun', 'marks': 88}]}


for student in data["students"]:
    print(student["name"], student["marks"])

# Output:
# Rahul 85
# Priya 90
# Arjun 88


#WRITE JSON
students = {
    "students": [
        {"name": "priya", "marks": 90},
        {"name": "Karen", "marks": 89}
    ]
}

with open("output.json","w") as file:
    json.dump(students, file, indent=4)

# output.json content:
# {
#     "students": [
#         {
#             "name": "priya",
#             "marks": 90
#         },
#         {
#             "name": "Karen",
#             "marks": 89
#         }
#     ]
# }