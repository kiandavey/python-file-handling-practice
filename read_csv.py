import csv

with open("inventory.csv", "r") as file:
    reader = csv.DictReader(file)
    total_gold = 0
    for row in reader:
        item = row["Item Name"]
        qty = int(row["Quantity"])
        price = int(row["Price"])
        print(f"Found {qty} {item}(s).")
        cost = qty * price
        total_gold += cost
print(f"Total Inventory Value: {total_gold} Gold")