names = []
while True:
    try:
        name = input().strip()
    except EOFError:
        break
    if name:
        names.append(name)

count = len(names)
if count == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif count == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
elif count > 2:
    names[-1] = "and " + names[-1]
    if count == 3:
        print(f"Adieu, adieu, to {', '.join(names)}")
    else:
        print(f"Adieu, adieu, to {', '.join(names[:-1])}, {names[-1]}")
