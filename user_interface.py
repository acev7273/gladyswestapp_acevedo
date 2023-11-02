# user_interface.py

def login():
    while True:
        # Ask the user for a login and a password
        email = input("Enter your email address: ")
        password = input("Enter your password: ")

        # Verify if the login is a valid email address
        if "@" in email and "." in email:
            # Return the user login (email address)
            return email

        # If the login is not a valid email address, report an error
        print("Invalid email address. Please enter a valid email.")

# You can add more user interface functions here if needed
