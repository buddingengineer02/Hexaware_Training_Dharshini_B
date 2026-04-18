import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    sales = list(reader)

# 1 Calculate total sales revenue.
total = 0
for s in sales:
    total += int(s["quantity"]) * int(s["price"])
print("Total revenue:", total)

# 2 Find total quantity sold per product.
qty = {}
for s in sales:
    p = s["product"]
    if p in qty:
        qty[p] += int(s["quantity"])
    else:
        qty[p] = int(s["quantity"])
print(qty)

# 3. Find the product with highest sales.
revenue = {}
for s in sales:
    p = s["product"]
    if p in revenue:
        revenue[p] += int(s["quantity"]) * int(s["price"])
    else:
        revenue[p] = int(s["quantity"]) * int(s["price"])

max_amt = 0
top_product = ""
for p in revenue:
    if revenue[p] > max_amt:
        max_amt = revenue[p]
        top_product = p
print("Product with highest sale:", top_product)

# 4. Calculate total revenue per product.
print(revenue)

# 5. Print products with sales above 50,000.
for p in revenue:
    if revenue[p] > 50000:
        print(p)