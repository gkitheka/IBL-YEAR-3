def convert(time):
    """Converts time string in 24-hour format to corresponding number of hours."""
    hours, minutes = time.split(':')
    return int(hours) + int(minutes) / 60


def main():
    """Prompts user for a time and outputs whether it's breakfast time, lunch time, or dinner time."""
    time = input('What time is it? (in 24-hour format HH:MM) ')
    hours = convert(time)

    if 7.0 <= hours < 8.0:
        print('It\'s breakfast time!')
    elif 12.0 <= hours < 13.0:
        print('It\'s lunch time!')
    elif 18.0 <= hours < 19.0:
        print('It\'s dinner time!')


if __name__ == '__main__':
    main()