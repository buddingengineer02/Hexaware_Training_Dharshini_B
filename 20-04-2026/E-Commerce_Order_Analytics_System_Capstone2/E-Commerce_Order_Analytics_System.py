#Python Capstone Project

#E-Commerce Order Analytics System

#Objective

#Build a Python program that analyzes data from multiple sources:
    #product catalog (JSON)
    #customer orders (CSV)
    #website visits (TXT)
#The program should generate a sales and customer report.
import csv
import json
# Part 1 — Website Visit Analysis (TXT)
# Task 1 - Read website_visits.txt
with open("website_visits.txt", "r") as file:
    visits = file.read().splitlines()

# Task 2 - Print all visitors
for name in visits:
    print(name)

# Task 3 - Find the total number of visits.
print("Total Visits:", len(visits))

# Task 4 - Find unique visitors using a set.
unique_visitors = set(visits)
print("Unique Visitors:", unique_visitors)

# Task 5 - Count how many times each visitor came to the website.
"""
Example expected structure:

{
"Rahul":3,
"Sneha":3,
"Arjun":2,
"Priya":1,
"Karan":1
}
"""
visit_count = {}
for name in visits:
    if name in visit_count:
        visit_count[name] += 1
    else:
        visit_count[name] = 1

print("Visit Count:", visit_count)

# Task 6 - Find the most frequent visitor.
top_visitor = visits[0]
for name in visit_count:
    if visit_count[name] > visit_count[top_visitor]:
        top_visitor = name

print("Most Frequent Visitor:", top_visitor)

# Part 2 — Product Catalog Analysis (JSON)

# Task 7 — Read products.json

with open("products.json", "r") as file:
    data = json.load(file)
# Task 8 — Print all product names and prices
for product in data["products"]:
    print(product["name"], product["price"])
# Task 9 — Store product information in dictionary
"""Example structure:

{
101: {"name":"Laptop","price":75000},

102: {"name":"Mouse","price":500}
}"""
product_dict = {}

for product in data["products"]:
    product_id = product["product_id"]
    product_dict[product_id] = {
        "name": product["name"],
        "price": product["price"]
    }

print(product_dict)
# Task 10 — Find the most expensive product
expensive = data["products"][0]

for product in data["products"]:
    if product["price"] > expensive["price"]:
        expensive = product

print("Most Expensive:", expensive["name"], expensive["price"])
# Task 11 — Find the least expensive product
cheap = data["products"][0]

for product in data["products"]:
    if product["price"] < cheap["price"]:
        cheap = product

print("Least Expensive:", cheap["name"], cheap["price"])

# Part 3 — Orders Analysis (CSV)
#Task 12 Read orders.csv .

with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Task 13 Print each order.
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    orders = list(reader)

for row in orders:
    print(row["order_id"], row["customer"], row["product_id"], row["quantity"])
# Task 14 Calculate the total quantity sold per product.
quantity_per_product = {}

for row in orders:
    product_id = int(row["product_id"])
    quantity = int(row["quantity"])

    if product_id in quantity_per_product:
        quantity_per_product[product_id] += quantity
    else:
        quantity_per_product[product_id] = quantity

print("Total Quantity Sold Per Product:", quantity_per_product)
# Task 15 Calculate total orders per customer.
"""
Expected structure:
{
"Rahul":3,
"Sneha":2,
"Arjun":1,
"Priya":1,
"Karan":1
}
"""
orders_per_customer = {}

for row in orders:
    customer = row["customer"]

    if customer in orders_per_customer:
        orders_per_customer[customer] += 1
    else:
        orders_per_customer[customer] = 1

print("Total Orders Per Customer:", orders_per_customer)
# Part 4 — Sales Calculation

# Using product prices and order quantities:
# Task 16 Calculate revenue for each order.
order_revenue = []

for row in orders:
    product_id = int(row["product_id"])
    quantity = int(row["quantity"])
    
    price = product_dict[product_id]["price"]
    revenue = price * quantity
    
    order_revenue.append(revenue)
    print("Order Revenue:", revenue)
# Task 17 Calculate total revenue.
total_revenue = 0

for revenue in order_revenue:
    total_revenue += revenue

print("Total Revenue:", total_revenue)
# Task 18 Calculate total revenue per product.
"""Example output structure:

{
"Laptop":150000,
"Mouse":2500,
"Keyboard":4500,
"Monitor":24000
}
"""
revenue_per_product = {}

for row in orders:
    product_id = int(row["product_id"])
    quantity = int(row["quantity"])
    
    price = product_dict[product_id]["price"]
    revenue = price * quantity
    
    product_name = product_dict[product_id]["name"]
    
    if product_name in revenue_per_product:
        revenue_per_product[product_name] += revenue
    else:
        revenue_per_product[product_name] = revenue

print("Revenue per Product:", revenue_per_product)
# Task 19 Find the highest selling product by revenue.
top_product = list(revenue_per_product.keys())[0]

for product in revenue_per_product:
    if revenue_per_product[product] > revenue_per_product[top_product]:
        top_product = product

print("Top Product:", top_product)
# Part 5 — Customer Analysis

# Task 20 Calculate total spending per customer.
customer_spending = {}

for row in orders:
    customer = row["customer"]
    product_id = int(row["product_id"])
    quantity = int(row["quantity"])
    
    price = product_dict[product_id]["price"]
    amount = price * quantity
    
    if customer in customer_spending:
        customer_spending[customer] += amount
    else:
        customer_spending[customer] = amount

print("Customer Spending:", customer_spending)

# Task 21 Find the highest spending customer.
top_customer = list(customer_spending.keys())[0]

for name in customer_spending:
    if customer_spending[name] > customer_spending[top_customer]:
        top_customer = name

print("Top Customer:", top_customer)
# Task 22 Find customers who spent more than ₹50,000.
print("Customers spending more than 50000:")

for name in customer_spending:
    if customer_spending[name] > 50000:
        print(name)

# Part 6 — Functions

# Create functions for:

# Task 23 Load visits from TXT.
def load_visits():
    with open("website_visits.txt", "r") as file:
        return file.read().splitlines()

# Task 24 Load product catalog from JSON.
def load_products():
    with open("products.json", "r") as file:
        data = json.load(file)
    return data["products"]
# Task 25 Load orders from CSV.
def load_orders():
    with open("orders.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)

# Task 26 Calculate product revenue.
def calculate_product_revenue(orders, product_dict):
    revenue_per_product = {}

    for row in orders:
        product_id = int(row["product_id"])
        quantity = int(row["quantity"])
        product_name = product_dict[product_id]["name"]
        price = product_dict[product_id]["price"]
        revenue = price * quantity

        if product_name in revenue_per_product:
            revenue_per_product[product_name] += revenue
        else:
            revenue_per_product[product_name] = revenue

    return revenue_per_product
# Task 27 Calculate customer spending.
def calculate_customer_spending(orders, product_dict):
    customer_spending = {}

    for row in orders:
        customer = row["customer"]
        product_id = int(row["product_id"])
        quantity = int(row["quantity"])
        price = product_dict[product_id]["price"]
        amount = price * quantity

        if customer in customer_spending:
            customer_spending[customer] += amount
        else:
            customer_spending[customer] = amount

    return customer_spending
# Task 28 Find top customer.
def find_top_customer(customer_spending):
    top_customer = list(customer_spending.keys())[0]

    for name in customer_spending:
        if customer_spending[name] > customer_spending[top_customer]:
            top_customer = name

    return top_customer

# Part 7 — Data Structures

# Use:
# list → store orders
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    orders = list(reader)

print("Orders List:", orders)
# dictionary → store product prices
product_dict = {}

for product in data["products"]:
    product_id = product["product_id"]
    product_dict[product_id] = {
        "name": product["name"],
        "price": product["price"]
    }

print("Product Dictionary:", product_dict)
# set → store unique visitors
with open("website_visits.txt", "r") as file:
    visits = file.read().splitlines()

unique_visitors = set(visits)
print("Unique Visitors:", unique_visitors)
# tuple → represent (product_name, revenue) pairs
product_revenue_list = []

for product in revenue_per_product:
    pair = (product, revenue_per_product[product])
    product_revenue_list.append(pair)

print("Product Revenue Tuples:", product_revenue_list)
# Part 8 — Final Report Generation

# Create a file called sales_report.txt.
with open("sales_report.txt", "w") as file:
    file.write("E-Commerce Sales Report\n")
    file.write("Total Website Visits: " + str(len(visits)) + "\n")
    file.write("Unique Visitors: " + str(len(unique_visitors)) + "\n")
    file.write("Total Revenue: " + str(total_revenue) + "\n")
    file.write("Top Customer: " + top_customer + "\n")
    file.write("Product Sales\n")

    for product in revenue_per_product:
        file.write(product + " -> " + str(revenue_per_product[product]) + "\n")
# Example output:

# E-Commerce Sales Report
# Total Website Visits: 10
# Unique Visitors: 5
# Total Revenue: 181000

# Top Customer: Rahul
# Product Sales
# Laptop → 150000
# Mouse → 2500
# Keyboard → 4500
# Monitor → 24000

# Final Challenge

# Task 29 Find visitors who visited but never ordered anything.
ordered_customers = set()

for row in orders:
    ordered_customers.add(row["customer"])

never_ordered = unique_visitors - ordered_customers

print("Visitors who visited but never ordered:")
for name in never_ordered:
    print(name)

# Task 30 Find customers who ordered but never visited the website more than once.
ordered_customers = set()

for row in orders:
    ordered_customers.add(row["customer"])

print("Customers who ordered but visited website only once:")

for customer in ordered_customers:
    if visit_count[customer] == 1:
        print(customer)
