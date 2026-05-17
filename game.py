# Program that plays a guessing game with the user.
import random


def main():
    while True:
        n = input("Level: ")
        if n.isnumeric() and int(n) > 0:
            n = int(n)
            guess(n)
            return
        else:
            pass


def guess(i):
    m = random.randint(0, i)
    while True:
        if i > 0:
            j = input("Guess: ")
            if j.isnumeric() and int(j) > 0:
                j = int(j)
                if j < m:
                    print("Too small!")
                    pass
                elif j > m:
                    print("Too large!")
                    pass
                else:
                    print("Just right!")
                    return
            else:
                pass
        else:
            pass

main()