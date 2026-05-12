# Outdated : Program that converts a date from one format to another
def main():
    data = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        i = input("Date: ").strip()
        if "/" in i:
            a, b, c = i.split("/")
            if a.isnumeric() and b.isnumeric():
                a = int(a)
                b = int(b)
                if a < 13:
                    if b < 32:
                        print(f"{c}-{a:02}-{b:02}")
                        return
            else:
                pass
        elif " " in i:
            a, b, c = i.split(" ")
            if a.isalpha():
                a = a.title()
                if "," in b:
                    b = b.replace(",", "")
                    b = int(b)
                    if a in data and b < 32:
                        print(f"{c}-{data.index(a) + 1 :02}-{b:02}")
                        return
            else:
                pass


main()
