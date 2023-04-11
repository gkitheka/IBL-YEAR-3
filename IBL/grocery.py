from collections import defaultdict

# create a defaultdict to store the count of each item
grocery_items = defaultdict(int)

# read input from user
print("Enter your grocery list (one item per line):")
while True:
    try:
        item = input().strip().lower()
        if not item:
            continue
        # increment the count for the entered item
        grocery_items[item] += 1
    except EOFError:
        break

# sort the items alphabetically and print the output
for item in sorted(grocery_items):
    count = grocery_items[item]
    print(f"{count} {item.upper()}")
