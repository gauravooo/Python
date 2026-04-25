#Program to tell what to eat between breakfast / Lunch / Dinner
def main():
    i = input("What time it is? ")
    j = (convert(i))
    if 7 <= j <= 8:
        print("breakfast time")
    elif 12 <= j <= 13:
        print("lunch time")
    elif 18 <= j <= 19:
        print("dinner time")


def convert(time):
    h, m = time.split(":")
    m = float(m)/60
    h = float(h)
    time = h+m
    return time


if __name__ == "__main__":
    main()
