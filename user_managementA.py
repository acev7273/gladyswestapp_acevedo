# user_management.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

# Create a single user
single_user = User("john", "password123")

def authenticate_user(username, password):
    if username == single_user.username and password == single_user.password:
        return single_user
    return None
