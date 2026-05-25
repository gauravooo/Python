# Program that converts a CSV file of names and houses into a new CSV file with first name, last name, and house. The program takes two command-line arguments: the input CSV file and the output CSV file. It checks
import sys
import csv

a = []
def main():
    if len(sys.argv) == 3:
        g = sys.argv[1]
        old(g)

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

def old(i):
    if (i.endswith(".csv")) :
        try:
            with open(i) as file:
                reader = csv.DictReader(file)
                for row in reader :
                    last, first = row["name"].split(', ')
                    house = row["house"]
                    a.append({"first": first,"last": last,"house": house})
            with open(sys.argv[2] , 'w') as out:
                write = csv.DictWriter(out, fieldnames=["first","last","house"])
                write.writeheader()
                for i in range(len(a)):
                    write.writerow({"first":a[i]["first"],"last":a[i]["last"],"house":a[i]["house"]})

        except FileNotFoundError:
            sys.exit(f"Could not read {g}")
    else:
        sys.exit("File is not csv")

main()
