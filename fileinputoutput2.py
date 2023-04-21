name = input("whats your name")

# `with open("name.text", "a") as file:` is opening a file named "name.text" in append mode ("a").
# This means that if the file already exists, any new data written to it will be added to the end of
# the file. If the file does not exist, it will be created. The `as file` part assigns the opened file
# to the variable `file`, which can then be used to read from or write to the file. The `with`
# statement ensures that the file is properly closed after the block of code is executed, even if an
# error occurs.
with open("name.text", "a") as file:
    file.write(f"{name}\n")