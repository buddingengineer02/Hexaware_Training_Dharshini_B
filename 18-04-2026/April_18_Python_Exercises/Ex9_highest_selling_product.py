# Exercise 9 – Highest Selling Product

sales = [
    {"product": "Laptop", "qty": 5},
    {"product": "Mouse", "qty": 20},
    {"product": "Laptop", "qty": 3},
    {"product": "Keyboard", "qty": 10}
]

total_sales = {}

# calculate total quantity for each product
for item in sales:
    product = item["product"]
    qty = item["qty"]

    total_sales[product] = total_sales.get(product, 0) + qty
#1. Calculate total sales per product
print("Total sales per product:", total_sales)

#2. Find highest selling product
highest_product = max(total_sales, key=total_sales.get)

print("Highest selling product:", highest_product, "-", total_sales[highest_product])