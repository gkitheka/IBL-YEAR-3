x = int(input("enter the value of x "))
y = int(input("enter the value of y "))

#function for addition
def addition():
    print(x + y)

addition()



#working with string
name = input("what is your name")
def hello(z):
    print("hello, " , z)

hello(name)




#working with string
# `name = input("what is your name")` is asking the user to input their name and storing it in the
# variable `name`.
name = input("what is your name")
def hello(z="world"):
    """
    The function "hello" takes an optional argument "z" with a default value of "world".
    
    :param z: a string representing the name of the person or thing to greet. If no argument is
    provided, the default value "world" will be used, defaults to world (optional)
    """
    print("hello, " , z)

hello()


#working with string
name = input("what is your name").strip()
def hello(z="world"):
    print("hello, " , z)

hello(name)