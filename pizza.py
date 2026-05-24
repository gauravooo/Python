# Pizza menu program that reads from a CSV file and displays the menu in a tabular format. The program takes the name of the CSV file as a command-line argument and checks for the correct number of arguments, the existence of the file, and whether it is a CSV file. If any of these checks fail, it exits with an appropriate error message. If the file is valid, it reads the contents and displays them in a formatted table using the tabulate library.
import sys
from tabulate import tabulate

a = []


def main():
    if len(sys.argv) == 3:
        g = sys.argv[1]
        menu(g)
        print(tabulate(a, headers="firstrow", tablefmt="grid"))

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def menu(value):
    if value.endswith(".csv"):
        try:
            if value == "regular.csv":
                with open("regular.csv") as file:
                    for row in file:
                        Regular_Pizza, Small, Large = row.strip().split(",")
                        a.append(
                            {
                                "Regular Pizza": Regular_Pizza,
                                "Small": Small,
                                "Large": Large
                            }
                        )
                    return
            elif value == "sicilian.csv":
                with open("sicilian.csv") as file:
                    for row in file:
                        Regular_Pizza, Small, Large = row.strip().split(",")
                        a.append(
                            {
                                "Regular Pizza": Regular_Pizza,
                                "Small": Small,
                                "Large": Large
                            }
                        )
                    return
            else:
                sys.exit("File doen not exit")

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
