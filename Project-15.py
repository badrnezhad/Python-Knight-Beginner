expression = input("عبارت را وارد کنید: ")

num1 = int(expression[0])
operator = expression[1]
num2 = int(expression[2])

result = 0
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print(f"{num1} {operator} {num2} = {result}")
