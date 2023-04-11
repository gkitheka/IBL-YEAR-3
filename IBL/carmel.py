def main():
    variable_name = input("Enter a variable name in camel case: ")
    snake_case_name = ""

    for i in range(len(variable_name)):
        if i == 0:
            snake_case_name += variable_name[i].lower()
        elif variable_name[i].isupper():
            snake_case_name += "_" + variable_name[i].lower()
        else:
            snake_case_name += variable_name[i]

    print("Snake case name:", snake_case_name)


if __name__ == "__main__":
    main()
