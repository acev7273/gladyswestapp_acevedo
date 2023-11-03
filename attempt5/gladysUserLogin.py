"""
Student: Shaye Acevedo
Module: gladysUserLogin
Description: This module handles user login functionality.
"""

def login():
    """
    Ask the user for a valid email address and password to log in.
    Returns the user's email address.
    """

    while True:
        email = input("Enter your email address: ")
        password = input("Enter your password: ")

        if is_valid_email(email):
            print(f"Welcome, {email}!")
            return email
        else:
            print("Invalid email address. Please enter a valid email.")

def is_valid_email(email):
    """
    Check if the provided input is a valid email address.
    Returns True if valid, False otherwise.
    """

    # A simple check for the presence of "@" and "."
    return "@" in email and "." in email

if __name__ == "__main__":
    login()
