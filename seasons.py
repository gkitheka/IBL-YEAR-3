from datetime import date, datetime
import sys


def get_date_of_birth():
    while True:
        date_str = input("Please enter your date of birth in YYYY-MM-DD format: ")
        try:
            date_of_birth = datetime.strptime(date_str, "%Y-%m-%d").date()
            return date_of_birth
        except ValueError:
            print("Invalid date format. Please try again.")


def calculate_age_in_minutes(date_of_birth):
    now = datetime.now().date()
    age_in_minutes = int((now - date_of_birth).total_seconds() / 60)
    return age_in_minutes


def print_age_in_words(age_in_minutes):
    hours = age_in_minutes // 60
    minutes = age_in_minutes % 60
    if hours == 0:
        age_str = f"{minutes} minute{'s' if minutes != 1 else ''}"
    elif hours == 1:
        if minutes == 0:
            age_str = "1 hour"
        else:
            age_str = f"1 hour and {minutes} minute{'s' if minutes != 1 else ''}"
    else:
        age_str = f"{hours} hours and {minutes} minute{'s' if minutes != 1 else ''}"
    print(f"You are {age_str} old.")


def main():
    date_of_birth = get_date_of_birth()
    age_in_minutes = calculate_age_in_minutes(date_of_birth)
    print_age_in_words(age_in_minutes)


if __name__ == "__main__":
    main()
