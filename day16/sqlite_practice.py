import sqlite3

conn = sqlite3.connect("college.db") #Create Database
cursor = conn.cursor()
# Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    designation TEXT
)
""") 

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY,
    title TEXT,
    emp_id INTEGER,
    status TEXT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
)
""")

conn.commit()

#CRUD Operations

def insert_employee(emp_id, name, department, designation):
    cursor.execute(
        "INSERT INTO employees VALUES (?, ?, ?, ?)",
        (emp_id, name, department, designation)
    )
    conn.commit()
    print("Employee inserted successfully.")

def fetch_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    print("\nEmployee Records:")
    for row in rows:
        print(row)

def update_employee(emp_id, new_department):
    cursor.execute(
        "UPDATE employees SET department = ? WHERE emp_id = ?",
        (new_department, emp_id)
    )
    conn.commit()
    print("Employee updated successfully.")

def delete_employee(emp_id):
    cursor.execute(
        "DELETE FROM employees WHERE emp_id = ?",
        (emp_id,)
    )
    conn.commit()
    print("Employee deleted successfully.")


while True:
    print("\n1. Insert Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = int(input("Employee ID: "))
        name = input("Name: ")
        department = input("Department: ")
        designation = input("Designation: ")
        insert_employee(emp_id, name, department, designation)

    elif choice == "2":
        fetch_employees()

    elif choice == "3":
        emp_id = int(input("Employee ID to update: "))
        new_dept = input("New Department: ")
        update_employee(emp_id, new_dept)

    elif choice == "4":
        emp_id = int(input("Employee ID to delete: "))
        delete_employee(emp_id)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")

conn.close()
