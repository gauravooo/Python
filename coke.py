# Simulate a vending machine that sells a bottle of coke for 50 cents. The machine should accept coins in the denominations of 25 cents, 10 cents, and 5 cents. The program should prompt the user to insert coins until the amount due is less than or equal to 0. If the user inserts more than the amount due, the program should calculate and display the change owed.
def main():
    print("Amount Due: 50")
    j = 50
    while j > 0:
        i = int(input("Insert Coin: "))
        if i == 25:
            j -= 25
            if j > 0:
                print("Amount Due:",j)
        elif i == 10:
            j -= 10
            if j > 0:
                print("Amount Due:",j)
        elif i == 5:
            j -= 5
            if j > 0:
                print("Amount Due:",j)
        else:
            print("Amount Due:",j)
    print("Change Owed:",abs(j))
main()