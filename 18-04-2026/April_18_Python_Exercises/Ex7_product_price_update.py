# Exercise 7 – Product Price Update
products = {
    "Laptop": 75000,
    "Mobile": 30000,
    "Tablet": 25000
}
#1. Increase all prices by 10%
for item in products:
    products[item] = products[item] + (products[item] * 10 / 100)
#2.Print updated prices
print("Updated prices:")
for item in products:
    print(item, ":", products[item])
