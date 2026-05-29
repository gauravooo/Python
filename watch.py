# Program that prompts the user for the URL of a YouTube video and then outputs the URL of the video in a shortened format. The program should work with any of the following formats:
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches:= re.search(r"^<iframe(.)*src=\"https?://(www\.)?youtube\.com/embed/([^\"]*)", s):
        url = "https://youtu.be/"+matches.group(3)
        return url
    else:
        return

if __name__ == "__main__":
    main()
