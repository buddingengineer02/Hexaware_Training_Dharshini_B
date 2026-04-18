# Exercise 11 – E-commerce Order Analysis

orders = [
    {"order_id": 1, "customer": "Rahul", "amount": 2500},
    {"order_id": 2, "customer": "Sneha", "amount": 1800},
    {"order_id": 3, "customer": "Rahul", "amount": 3200},
    {"order_id": 4, "customer": "Amit", "amount": 1500}
]

spending = {}
orders_count = {}

for order in orders:
    customer = order["customer"]
    amount = order["amount"]

    if customer in spending:
        spending[customer] += amount
    else:
        spending[customer] = amount

    if customer in orders_count:
        orders_count[customer] += 1
    else:
        orders_count[customer] = 1

top_customer = ""
top_amount = 0

for customer in spending:
    if spending[customer] > top_amount:
        top_amount = spending[customer]
        top_customer = customer
#1. Calculate total spending per customer
print("Spending per customer:", spending)
#2. Find highest spending customer
print("Top customer:", top_customer, "-", top_amount)
#3. Count total orders per customer
print("Orders count:", orders_count)