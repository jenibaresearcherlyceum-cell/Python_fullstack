import sqlite3

DB_NAME = "college.db"

# DATA LAYER

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            designation TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_employee_db(emp_id, name, department, designation):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees VALUES (?, ?, ?, ?)",
        (emp_id, name, department, designation)
    )

    conn.commit()
    conn.close()


def get_all_employees_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    conn.close()
    return data


def update_employee_db(emp_id, new_department):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE employees SET department=? WHERE emp_id=?",
        (new_department, emp_id)
    )

    conn.commit()
    conn.close()


def delete_employee_db(emp_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    conn.commit()
    conn.close()

# BUSINESS LAYER

def add_employee_service(emp_id, name, dept, desig):
    if not name.strip():
        print("Name cannot be empty.")
        return

    insert_employee_db(emp_id, name, dept, desig)
    print("Employee added successfully.")


def view_employees_service():
    employees = get_all_employees_db()

    if not employees:
        print("No employees found.")
        return

    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Dept: {emp[2]}, Desig: {emp[3]}")


def update_employee_service(emp_id, new_dept):
    update_employee_db(emp_id, new_dept)
    print("Employee updated successfully.")


def delete_employee_service(emp_id):
    delete_employee_db(emp_id)
    print("Employee deleted successfully.")


# PRESENTATION LAYER

def main():
    create_table()

    while True:
        print("\n===== Employee Management =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            emp_id = int(input("Employee ID: "))
            name = input("Name: ")
            dept = input("Department: ")
            desig = input("Designation: ")
            add_employee_service(emp_id, name, dept, desig)

        elif choice == "2":
            view_employees_service()

        elif choice == "3":
            emp_id = int(input("Employee ID to update: "))
            new_dept = input("New Department: ")
            update_employee_service(emp_id, new_dept)

        elif choice == "4":
            emp_id = int(input("Employee ID to delete: "))
            delete_employee_service(emp_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
