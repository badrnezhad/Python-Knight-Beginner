# name = input("What is your name? ")
# print(f"Hello, {name}!")

numbers = [20, 15, 18, 16, 20, 20, 15, 16, 20, 4]
print(numbers[2])
print(numbers[-1])
# zero-base index

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[1])
print(matrix[1][2])

my_list = [1, 2.4, "Ali", True]
print(my_list)

my_list.append(5)
print(my_list)

my_list[1] = 8.5
print(my_list)

my_tupple = (1, 2, 3)
print(my_tupple)

print("====================================")

print(numbers)

numbers_set = {20, 15, 18, 16, 20, 20, 15, 16, 20, 4}
print(numbers_set)

print("====================================")

my_information = {
    "first_name": "Hossein",
    "last_name": "Badrnezhad",
    "age": 32,
}
print(my_information)
print(f"first name: {my_information["first_name"]}")
print(f"last name: {my_information["last_name"]}")
print(f"age: {my_information["age"]}")
