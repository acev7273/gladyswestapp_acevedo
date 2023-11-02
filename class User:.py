class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

class UserManagement:
    def __init__(self):
        self.users = {}  # Store users in a dictionary

    def register_user(self, username, password):
        if username in self.users:
            return False  # User already exists
        self.users[username] = User(username, password)
        return True

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None

    def get_user(self, username):
        return self.users.get(username)

# Example usage:

user_management = UserManagement()

# Register a user
user_management.register_user("shaye", "test")

# Authenticate a user
authenticated_user = user_management.authenticate_user("shaye", "test")
if authenticated_user:
    print(f"Authenticated user: {authenticated_user}")
else:
    print("Authentication failed.")

# Get a user
user = user_management.get_user("shaye")
if user:
    print(f"Found user: {user}")
else:
    print("User not found.")
