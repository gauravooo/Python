# Program that counts the number of times the interjection "um" appears in a string, ignoring case and ensuring that "um" is not part of another word.
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"((\s|,)um(\s|,|\.|\?)|(^um(\s|,|\.|\?)?))", s, re.IGNORECASE)
    return len(match)

if __name__ == "__main__":
    main()
