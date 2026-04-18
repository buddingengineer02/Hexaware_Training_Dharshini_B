numbers=[10,20,30,40,50]
print(numbers)
fruit=["apple","banana","mango","orange"]

#Acess Element
print(fruit[0])
print(fruit[2])

#Acess from last
print(fruit[-1])
print(fruit[-2])

#Modify Element
numbers=[10,20,30]
numbers[2]=100
print(numbers)

#Add Element
numbers.append(40)
print(numbers)

#Insert
list1=[10,20,30]
list1.insert(2,50)
print(list1)

#Remove
list2=[10,20,30]
list2.remove(20)
print(list2)

#Remove Last Element
list3=[10,20,30,40]
list3.pop()
print(list3)

#Length of List
print(len(list3))

#Printing elements using For loop
list4=[10,20,30,40]
for item in list4:
    print(item)

#Checking the Existence of Element
fruits=["apple","banana","mango","orange"]
if "banana" in fruits:
    print("Banana Exists")

#Slicing
list5=[10,20,30,40,50]
print(list5[1:3])

#Reverse
list5.reverse()
print(list5)

#Sorting
list5.sort()
print(list5)

#Maximum Element
print(max(list5))

#Minimum Element
print(min(list5))

#Sum of Elements
print(sum(list5))
