greeting = input("Please enter a greeting: ")
greeting = greeting.lstrip()  # remove leading whitespace
if greeting.lower().startswith("hello"):
    print("$0")
elif greeting.lower().startswith("h"):
    print("$20")
else:
    print("$100")
