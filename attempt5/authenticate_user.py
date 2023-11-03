from user_management import authenticate_user
from location_program import calculate_distance  # Import the location function

# Main function for your program
def main():
    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Authenticate the user
    user = authenticate_user(username, password)

    if user:
        print(f"Welcome, {user.username}!")

        # Example: Calculate distance between two points
        point1 = (1, 2)
        point2 = (4, 6)
        distance = calculate_distance(point1, point2)
        print(f"Distance between point1 and point2: {distance}")

    else:
        print("Authentication failed. Access denied.")

if __name__ == "__main__":
    main()