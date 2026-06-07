sales = [50000000, 70000000, 30000000]

max_sale = sales[0]
for sale in sales:
    if sale > max_sale:
        max_sale = sale

print(max_sale)

for sale in sales:
    salary = sale * 0.10

    if sale == max_sale:
        salary += sale * 0.05

    print(f"{sale} => salary: {salary}")
