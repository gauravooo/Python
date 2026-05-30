# Python program that converts 12-hour time format to 24-hour time format. The program should prompt the user for a time in 12-hour format, validate the input, and then output the corresponding time in 24-hour format. The input should be in the format "HH:MM AM/PM to HH:MM AM/PM". If the input is invalid, the program should raise a ValueError.
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches:= re.search(r"^([0-1]?[0-9])(:[0-5][0-9])?(\s[AP]M)\sto\s([0-1]?[0-9])(:[0-5][0-9])?(\s[AP]M)", s):
        g2 = matches.group(2)
        g4 = matches.group(5)
        g1 = int(matches.group(1))
        g5 = int(matches.group(4))

        if matches.group(3) == " PM":
            if g5 == 12:
                g5 -= 12
            t = g1
            if  t != 12:
                t += 12

            if not g2:
                if not g4:
                    result = f"{t:02d}:00 to {int(g5):02d}:00"
                    return result
                else:
                    result = f"{t:02d}:00 to {int(g5):02d}{g4}"
                    return result
            else:
                if not g4:
                    result = f"{t:02d}{g2} to {int(g5):02d}:00"
                    return result
                else:
                    result = f"{t:02d}{g2} to {int(g5):02d}{g4}"
                    return result

        elif matches.group(6) == " PM":
            if g1 == 12:
                g1 -= 12
            t = g5
            if  t != 12:
                t += 12

            if not g2:
                if not g4:
                    result = f"{int(g1):02d}:00 to {t:02d}:00"
                    return result
                else:
                    result = f"{int(g1):02d}:00 to {t:02d}{g4}"
                    return result
            else:
                if not g4:
                    result = f"{int(g1):02d}{g2} to {t:02d}:00"
                    return result
                else:
                    result = f"{int(g1):02d}:00 to {t:02d}{g4}"
                    return result

    else:
        raise ValueError

if __name__ == "__main__":
    main()
