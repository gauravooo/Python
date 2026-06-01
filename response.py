# Please enter an email address and the program will check if it's valid or not.
import validators

i = input("What's your email address? ")

if validators.email(i):
    print("Valid")
else:
    print("Invalid")
