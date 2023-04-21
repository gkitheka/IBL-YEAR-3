import argparse
import pyfiglet

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--font", help="the font to use")
args = parser.parse_args()

# If the user specified a font, check that it exists
if args.font:
    fonts = pyfiglet.FigletFont.getFonts()
    if args.font not in fonts:
        import sys
        sys.exit(f"Invalid font: {args.font}")

# Prompt the user for input
text = input("Enter some text: ")

# Determine the font to use
if args.font:
    font = args.font
else:
    import random
    fonts = pyfiglet.FigletFont.getFonts()
    font = random.choice(fonts)

# Print the output
result = pyfiglet.figlet_format(text, font=font)
print(result)
