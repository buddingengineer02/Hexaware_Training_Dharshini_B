import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    data = {}

    for row in reader:
        p = row["product"]
        q = int(row["quantity"])
        price = int(row["price"])

        amount = q * price

        if p in data:
            data[p]["qty"] += q
            data[p]["amount"] += amount
        else:
            data[p] = {"qty": q, "amount": amount}
# Write Python code to produce this output:

    # Product Sales Summary
    # Laptop → Qty: 8 Revenue: 600000
    # Mouse → Qty: 30 Revenue: 15000
    # Keyboard → Qty: 15 Revenue: 22500
print("Product Sales Summary")

for p in data:
    print(p, "→ Qty:", data[p]["qty"], "Revenue:", data[p]["amount"])