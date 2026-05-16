# Adieu
import inflect

p = inflect.engine()
a = []


def main():
    try:
        while True:
            i = input("Name: ").strip()
            if i.isalpha():
                a.append(i)
            else:
                pass
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(a)}")
        return


main()
