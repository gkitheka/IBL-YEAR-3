import random

while True:
    try:
        level = int(input("Enter a level (positive integer): "))
        if level <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess a number between 1 and {}: ".format(level)))
        if guess <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

while guess != number:
    if guess < number:
        print("Too small!")
    else:
        print("Too large!")
    try:
        guess = int(input("Guess again: "))
        if guess <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

print("Just right!")
