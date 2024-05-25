from validator_collection import checkers

s = input("What's your email address? ")

if checkers.is_email(s):
    print("Valid")
else:
    print("Invalid")
