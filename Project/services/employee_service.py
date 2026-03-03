from employee import Employee
import database


def add_employee(emp_id, name, department, designation):
    emp = Employee(emp_id, name, department, designation)
    database.insert_employee(emp)


def view_employees():
    return database.fetch_employees()


def update_employee(emp_id, data):
    import sqlite3

    with sqlite3.connect(database.DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE employees
            SET name = ?, department = ?, designation = ?
            WHERE emp_id = ?
        """, (
            data.get("name"),
            data.get("department"),
            data.get("designation"),
            emp_id
        ))

        conn.commit()
        return cursor.rowcount > 0


def delete_employee(emp_id):
    import sqlite3

    with sqlite3.connect(database.DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE employees
            SET is_active = 0
            WHERE emp_id = ?
        """, (emp_id,))

        conn.commit()
        return cursor.rowcount > 0