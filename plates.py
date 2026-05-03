# program that checks if a vanity plate is valid
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) < 7:
        if s.isalnum():
            y = s[0:2]
            #z = s[2:6]
            if y.isalpha():
                j = False
                for i in range(len(s)):
                    if s[i].isdigit():
                        if not j:
                            if s[i] == '0':
                                return False
                            j = True
                    elif j:
                        return False
                return True
main()
