with open("name.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())