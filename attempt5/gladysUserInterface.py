"""
Student: Shaye Acevedo
Module: gladysUserInterface
Description: This module is the main user interface for the application.
"""

import gladysUserLogin as userLogin

def start():
    """
    Start the application and display the main menu.
    """
    print("Welcome to Gladys West Map App")
    user = userLogin.login()
    while True:
        print("Main Menu:")
        print("Type 1 to set current position (future GPS longitude input)")
        print("Type 2 to set destination position (future GPS latitude input)")
        print("Type 3 to calculate distance (calculate the distance)")
        print("Type 4 to run tests (view test results)")
        print("Type q to quit")

        choice = input("Enter a command: ")

        if choice == "1":
            print("This is a future GPS longitude input.")
        elif choice == "2":
            print("This is a future GPS latitude input.")
        elif choice == "3":
            print("Calculating distance...")
        elif choice == "4":
            print("Running tests...")
        elif choice == "q":
            print("Thank you for using Gladys West Map App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    start()


