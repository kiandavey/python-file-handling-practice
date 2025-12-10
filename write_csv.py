import csv

data = [
    ["Item Name", "Quantity", "Price"],
    ["Health Potion", 5, 50],
    ["Iron Sword", 1, 150],
    ["Wooden Shield", 2, 30]
]

with open("inventory.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)