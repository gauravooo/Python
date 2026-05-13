# program that takes a string and outputs the emojized version of that string
import emoji


def main():
    i = input("Input: ")
    print(emoji.emojize(i , language="alias"))


main()