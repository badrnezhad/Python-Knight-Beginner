import random

random_number = random.randint(0, 100)

for i in range(5):
    guess = int(input("Guess a number: "))
    if guess == random_number:
        print("Correct 🎉")
        break
    elif guess > random_number:
        print("Too high")
    elif guess < random_number:
        print("Too low")

print(f"Goodbye! number was {random_number}")
