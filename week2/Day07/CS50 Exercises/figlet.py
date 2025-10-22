'''
 implement a program that:

    Expects zero or two command-line arguments:
        Zero if the user would like to output text in a random font.
        Two if the user would like to output text in a specific font, 
        in which case the first of the two should be -f or --font, and 
        the second of the two should be the name of the font.
    Prompts the user for a str of text.
    Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or 
the second is not the name of a font, the program should exit via sys.exit with an error message.
'''

# import required packages and libraries
import sys
import pyfiglet
import random # if the user likes the output in a random format

# define main
def main():
    # check command line argument
    if len(sys.argv) == 1:
        text = input("Enter text to convert: ")
        font = random.choice(pyfiglet.FigletFont.getFonts())
        print(pyfiglet.figlet_format(text, font=font))
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f","--font"]:
        font = sys.argv[2]
        if font not in pyfiglet.FigletFont.getFonts():
            print(f"ERROR: font {font} not found")
            sys.exit(1)
        text = input("Enter text to convert: ")
        print(pyfiglet.figlet_format(text, font=font))

# call main
if __name__ == "__main__":
    main()