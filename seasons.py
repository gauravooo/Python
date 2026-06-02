# Program that prompts the user for their date of birth and then outputs their age in minutes, formatted in English words. For example, if the user was born on 2000-01-01 and today is 2024-06-01, the program should output "Twenty-three million, seven hundred and sixty thousand minutes". The program should also validate the input to ensure it is a valid date in the format YYYY-MM-DD.
from datetime import date
import inflect
import re
import sys
def main():
    print(get_age(input("Date of Birth(YYYY-MM-DD): ").strip()))


def get_age(d_o_b):
    p = inflect.engine()
    pattern = r"^[1-9][0-9]{3}-[0-9][0-9]-[0-9][0-9]$"
    if re.match(pattern , d_o_b):
        year , month , day = (d_o_b.split("-"))
        birthdate = date(int(year) , int(month) , int(day))
        today = date.today()
        age = (today - birthdate).days
        minutes =(age*24*60)
        result = p.number_to_words(minutes , andword="")
        return f"{result.capitalize()} minutes"
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
