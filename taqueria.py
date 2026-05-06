# Simulate a cash register for a taco truck.
def main():
    sum = 0
    dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    try:
        while True:
            i = input("Item: ").title()
            if i in dict:
                sum += dict[i]
                print(f"Total: ${sum:.2f}")
            else:
                pass
    except EOFError:
        return

main()
print("")
