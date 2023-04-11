def main():
    number = get_number()
    helloworld(number)

def  get_number():
    while True:
        x = int(input("enter the value of x"))
        if x > 0:
            break
    return x

def helloworld(n):
    for _ in range(n):
          print("hello world")

main()




