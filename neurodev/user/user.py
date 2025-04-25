import json
import os

def register_user():
    name = input("Full Name: ")
    email = input("Email: ")
    username = input("Enter your username: ")  # Get username input
    password = input("Enter your password: ")  # Get password input

    
    if not os.path.exists("users.json"):
        with open("users.json", "w") as file:
            json.dump({}, file)

    
    with open("users.json", "r") as file:
        users = json.load(file)  # Convert JSON to Python dictionary

    
    if username in users or any(u["email"] == email for u in users.values()):
        print("Username or email already exists!")
        return None

    
    users[username] = {
        "name": name,
        "email": email,
        "password": password,
        "username": username,
        "plan": "free",
        "interests": []
    }

    
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    # 6️ Return user info
    return users[username]





def login_user():
    email_log = input('Email: ')
    username_log = input("Enter your username: ")  # Get username input
    password_log = input("Enter your password: ")  # Get password input
    
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            users = json.load(file)  # Convert JSON to Python dictionary
        
        if username_log in users:
            if users[username_log]["password"] == password_log:
                print("Login successful!")
                return users[username_log]
            else:
                print("Incorrect password!")
        else:
            print("Username not found!")
    else:
        print("No users registered yet.")