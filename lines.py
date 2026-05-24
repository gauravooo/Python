# Python program that counts the number of lines of code in a Python file, excluding comments and blank lines.
import sys

def main():
    if len(sys.argv) == 2:
        g = sys.argv[1]
        print(f"{count(g)}")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

def count(value):
    c = 0
    if (value.endswith(".py")) :
        try:
            with open(value, "r") as fi:
                lines = fi.readlines()

            for line in lines:
                if line.strip().startswith("#"):
                    pass
                elif len(line.strip()) == 0:
                    pass
                else:
                    c += 1
            return c

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")


if __name__=="__main__":
    main()
