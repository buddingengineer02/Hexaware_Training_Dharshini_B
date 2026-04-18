# Exercise 4 – Inventory Management
inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15
}
#1. Add "monitor":8
inventory["monitor"] = 8
#2. Reduce laptop stock by 2
inventory["laptop"] = inventory["laptop"] - 2
print(inventory)
#3. Print items with stock less than 10
print("Items with stock less than 10:")
for item in inventory:
    if inventory[item] < 10:
        print(item, inventory[item])
