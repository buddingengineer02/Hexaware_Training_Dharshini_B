# Exercise 6 – Common Students in Two Classes
classA = {"Rahul", "Sneha", "Amit", "Neha"}
classB = {"Sneha", "Amit", "Karan", "Riya"}
#1. Students in both classes
print("Students in both classes:", classA.intersection(classB))
#2. Students only in Class A
print("Students only in Class A:", classA.difference(classB))
#3. All unique students
print("All unique students:", classA.union(classB))