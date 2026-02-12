def login():
    users = {
        "admin": {"password": "admin123", "role": "Admin"},
        "staff": {"password": "staff123", "role": "Staff"}
    }

    attempts = 3

    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            print("\nLogin successful!")
            return username, users[username]["role"]
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts left: {attempts}")

    print("Too many failed attempts. Exiting system.")
    return None, None
