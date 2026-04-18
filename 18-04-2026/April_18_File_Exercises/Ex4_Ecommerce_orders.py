import json

with open("orders.json", "r") as file:
    data = json.load(file)

orders = data["orders"]

# 1 Print all orders.
print(orders)

# 2 Calculate total revenue.
total = 0
for o in orders:
    total += o["amount"]
print("Total revenue:", total)

# 3 Find total spending per customer.
spend = {}
for o in orders:
    c = o["customer"]
    if c in spend:
        spend[c] += o["amount"]
    else:
        spend[c] = o["amount"]
print(spend)

# 4 Find the highest spending customer.
max_amt= 0
top_customer = ""
for cust in spend:
    if spend[cust] > max_amt:
        max_amt= spend[cust]
        top_customer = cust
print("Highest spender:", top_customer)

# 5 Count total orders per customer.
order_count = {}
for o in orders:
    cust = o["customer"]
    if cust in order_count:
        order_count[cust] += 1
    else:
        order_count[cust] = 1
print(order_count)