products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]

# Writing on file
file = open("products.txt", "w")
for product in products:
    file.write(f"{product}\n")
file.close()

# Reading from file
file = open("products.txt", "r")
content = file.read()
print(content)
file.close()
