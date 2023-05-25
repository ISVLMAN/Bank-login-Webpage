# User database
users = {}


def signup():
    print("Please sign up:")
    username = input("Username: ")
    password = input("Password: ")
    confirm_password = input("Reconfirm Password: ")
    if confirm_password == password:
        print("Account Created Successfuly")

    # Check if the username already exists
    if username in users:
        print("Username already exists. Please try again.")
    else:
        # Add the new user to the database
        users[username] = password
        print("Sign up successful!")


def login():
    print("Please log in:")
    username = input("Username: ")
    password = input("Password: ")

    # Check if the username and password match
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")


# Main program loop
while True:
    print("Skipper mobile banking app ")
    print("1. Create account")
    print("2. Login/Signin")
    print("3. Quit app")

    choice = input("choose (1-3): ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

print("THANK YOU FOR BANK WITH US")
