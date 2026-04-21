# Return the amount of money a person will receive based on their greeting.
def main():
    i = input("Enter the greeting ").strip().lower()
    print(greet(i))

def greet(value):
    if value.startswith("hello"):
        return "$0"
    elif value.startswith("h"):
        return "$20"
    else:
        return "$100"
main()