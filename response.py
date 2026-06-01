# Please enter an email address and the program will check if it's valid or not.
import validators

email = input("What's your email address? ")

if validators.email(email):
    print("Valid")
else:
    print("Invalid")
