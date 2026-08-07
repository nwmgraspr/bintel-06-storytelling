import csv
from pathlib import Path

rows = [
    [
        "TransactionID",
        "SaleDate",
        "ProductID",
        "ProductName",
        "Category",
        "Region",
        "QuantitySold",
        "UnitPrice",
        "InventoryBeforeSale",
    ],
    [
        1001,
        "2025-01-05",
        "P001",
        "Wireless Mouse",
        "Electronics",
        "East",
        15,
        25.99,
        120,
    ],
    [1002, "2025-01-08", "P002", "Office Chair", "Furniture", "West", 4, 199.99, 40],
    [1003, "2025-01-12", "P003", "Notebook", "Office Supplies", "South", 30, 5.99, 300],
    [1004, "2025-01-20", "P004", "Keyboard", "Electronics", "North", 12, 45.99, 80],
    [
        1005,
        "2025-02-03",
        "P001",
        "Wireless Mouse",
        "Electronics",
        "East",
        22,
        25.99,
        105,
    ],
    [
        1006,
        "2025-02-10",
        "P005",
        "Desk Lamp",
        "Office Supplies",
        "West",
        18,
        29.99,
        150,
    ],
    [1007, "2025-02-15", "P002", "Office Chair", "Furniture", "South", 6, 199.99, 36],
    [1008, "2025-03-02", "P003", "Notebook", "Office Supplies", "East", 45, 5.99, 270],
    [1009, "2025-03-12", "P004", "Keyboard", "Electronics", "North", 25, 45.99, 68],
    [
        1010,
        "2025-03-20",
        "P001",
        "Wireless Mouse",
        "Electronics",
        "West",
        35,
        25.99,
        83,
    ],
    [
        1011,
        "2025-04-05",
        "P005",
        "Desk Lamp",
        "Office Supplies",
        "South",
        20,
        29.99,
        132,
    ],
    [1012, "2025-04-18", "P004", "Keyboard", "Electronics", "East", 30, 45.99, 43],
    [
        1013,
        "2025-05-04",
        "P001",
        "Wireless Mouse",
        "Electronics",
        "North",
        40,
        25.99,
        48,
    ],
    [1014, "2025-05-15", "P002", "Office Chair", "Furniture", "East", 8, 199.99, 30],
    [1015, "2025-05-25", "P003", "Notebook", "Office Supplies", "West", 60, 5.99, 225],
]

output = Path("data/raw/retail_inventory_case.csv")
output.parent.mkdir(parents=True, exist_ok=True)

with output.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print(f"Created: {output}")
