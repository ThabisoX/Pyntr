def register_user():
    name = input("Full Name: ")
    email = input("Email: ")
    username = input('Username: ')
    password = input('Password: ')
    
    user_data = {
    "username": username,
    "email": email,
    "password": password, 
    "username": username,
    "plan": "free",  # default plan
    "interests": []  
}
    return user_data





def login_user():
    email_log = input('Email: ')
    password_log = input('Password: ')
    
    print("Logging in...")  


    print("Logging in...")  

    return {
    "username": "pyntr_user",
    "email": email_log,
    "plan": "free",
    "interests": ["Backend", "DevOps"]
}