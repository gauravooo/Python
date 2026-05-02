# Twttr : Write a program that prompts the user for a string and then outputs that same string with all of the vowels removed. For the purposes of this exercise, assume that the letters "a", "e", "i", "o", and "u" are vowels, whether they are uppercase or lowercase.
def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(text):
    new = ""
    pair = ["a","e","i","o","u","A","E","I","O","U"]
    for i in text:
        if i.isalpha():
            if i in pair:
                pass
            else:
                new += i
        else:
            pass
    return new


if __name__=="__main__":
    main()