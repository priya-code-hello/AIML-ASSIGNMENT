import re

print("Create a Strong Password")
password = input("Enter password: ")

# Conditions
length = len(password) >= 8
upper = re.search("[A-Z]", password)
lower = re.search("[a-z]", password)
digit = re.search("[0-9]", password)
special = re.search("[@#$%^&*!]", password)

if length and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")
    print("Password must contain:")
    print("- At least 8 characters")
    print("- One uppercase letter")
    print("- One lowercase letter")
    print("- One number")
    print("- One special character (@#$%^&*!)")