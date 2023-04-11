def main():
    text = input("Enter some text: ")
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    print(result)

if __name__ == "__main__":
    main()
