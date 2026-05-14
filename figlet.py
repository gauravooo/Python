# program that takes a string and prints it in ASCII art using the pyfiglet library
from pyfiglet import Figlet
import sys

figlet = Figlet()

j = figlet.getFonts()


def main():

    if len(sys.argv) == 1:
        i = input("Input:")
        f = Figlet()
        print(f.renderText(i))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in j:
                i = input("Input:")
                a1 = figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(i))
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


main()