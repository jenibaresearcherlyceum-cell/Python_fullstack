#Task 1- Simple Login System:

correct_username = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Invalid credentials. Attempts left: {attempts}")

if attempts == 0:
    print("Account locked. Too many failed attempts.")


#Task 2 - Role Based Menu Example:

role = input("Enter role (Admin/Staff): ")

print("\n===== MENU =====")

if role == "Admin":
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. View All Tasks")
elif role == "Staff":
    print("1. View Assigned Tasks")
else:
    print("Invalid role.")


#Task A3 - Access Restriction Example:


role = input("Enter role (Admin/Staff): ")

if role == "Admin":
    print("You are allowed to delete employee.")
else:
    print("Access denied. Only Admin can delete employee.")

