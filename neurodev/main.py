from user import user

def main_menu(current_user):
    while True:
        print(f"\n👋 Welcome {current_user['username']}! What would you like to do?")
        print("[1] Connect with another dev (Synapse)")
        print("[2] Post a Pulse")
        print("[3] Join a Caucus")
        print("[4] See Notifications")
        print("[5] Upgrade Plan")
        print("[6] Logout")

        option = int(input('Enter Option (1-6): '))

        if option == 1:
            print("Feature under construction: Synapse.")
        elif option == 2:
            print("Feature under construction: Pulse.")
        elif option == 3:
            print("Feature under construction: Caucus.")
        elif option == 4:
            print("Feature under construction: Notifications.")
        elif option == 5:
            print("Feature under construction: Upgrade Plan.")
        elif option == 6:
            break

print("Hello World! Welcome to PYNTR")
print("A developers playground!")
print("Would you like to:")
print("1. Register         2. Login        3. Exit")
reg_log = int(input('Enter number: '))

if reg_log == 1:
    current_user = user.register_user()
    if current_user:  # Check if registration was successful
        print('User registered successfully!\n')
        main_menu(current_user)
    else:
        print("Registration failed. Please try again.")
elif reg_log == 2:
    current_user = user.login_user()
    if current_user:  # Check if login was successful
        main_menu(current_user)
    else:
        print("Login failed. Please try again.")
elif reg_log == 3:
    exit()
else:
    exit()

