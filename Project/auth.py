from logger import log_info, log_warning, log_error


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
            role = users[username]["role"]
            log_info(f"Login success for user: {username} with role: {role}")
            return username, role
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts left: {attempts}")
            log_warning(f"Failed login attempt for username: {username}")

    log_error("User locked out due to multiple failed login attempts")
    print("Too many failed attempts. Exiting system.")
    return None, None
