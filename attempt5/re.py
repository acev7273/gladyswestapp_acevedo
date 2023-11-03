import re

def is_valid_email(email):
    # Regular expression pattern for a valid email address
    email_pattern = r'^[\w\.-]+@[\w\.-]+(\.[\w]+)+$'

    if re.match(email_pattern, email):
        return True
    else:
        return False
        email = input("Enter your email address: ")
if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address. Please enter a valid email.")

