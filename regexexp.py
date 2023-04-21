import re

email = input("whats your email?").strip()

if re.search(".+@.+", email):
    print("valid")
else:
    print("Invalid")