import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x, y, z = generate_integer(level)
        problem = f"{x} + {y} = "
        answer = None
        for j in range(3):
            answer = input(problem)
            try:
                answer = int(answer)
            except ValueError:
                print("EEE")
                continue
            if answer == z:
                print("Correct!")
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"The correct answer was {z}.")
    print(f"Your score is {score}/10.")


def get_level():
    while True:
        level = input("Choose a level (1, 2, or 3): ")
        if level in ("1", "2", "3"):
            return int(level)


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    z = x + y
    return x, y, z


if __name__ == "__main__":
    main()
