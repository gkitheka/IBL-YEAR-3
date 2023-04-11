def calculate_fuel_percentage(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0:
            raise ValueError
        percentage = x / y * 100
        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return round(percentage)
    except (ValueError, ZeroDivisionError):
        return False

def main():
    while True:
        fraction = input("Enter fuel gauge fraction (X/Y): ")
        percentage = calculate_fuel_percentage(fraction)
        if percentage:
            print(f"{percentage}%")
            break
        else:
            print("Invalid input. Please enter again.\n")

if __name__ == '__main__':
    main()
