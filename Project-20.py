products = [
    {"id": 1000, "name": "Laptop", "defective": False},
    {"id": 1100, "name": "Mouse", "defective": True},
    {"id": 1200, "name": "Keyboard", "defective": False}
]

for product in products:
    if not product["defective"]:
        print(product["id"], product["name"])
