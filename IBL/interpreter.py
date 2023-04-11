expression = input("Enter an arithmetic expression (e.g. 1 + 2): ")
x, operator, z = expression.split()
x = int(x)
z = int(z)

if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
else:
    result = x / z

print("{:.1f}".format(result))
