from employee import Employee
import database
import sqlite3
from database import DB_NAME


# CHECK EMPLOYEE EXISTS
def employee_exists(emp_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees WHERE emp_id = ?", (emp_id,))
    result = cursor.fetchone()

    conn.close()
    return result is not None


# ADD EMPLOYEE
def add_employee(emp_id, name, department, designation):
    emp = Employee(emp_id, name, department, designation)
    database.insert_employee(emp)


# VIEW EMPLOYEES (PAGINATION + FILTER)
def view_employees(page, limit, department=None, search=None, sort_by="emp_id", order="asc"):
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    offset = (page - 1) * limit

    #  fetch all employees (active + inactive)
    query = "SELECT * FROM employees WHERE is_active = 1"
    count_query = "SELECT COUNT(*) FROM employees WHERE is_active = 1"
    params = []
    count_params = []

    # SEARCH
    if search:
        query += " AND LOWER(name) LIKE ?"
        count_query += " AND LOWER(name) LIKE ?"
        value = f"%{search.lower()}%"
        params.append(value)
        count_params.append(value)

    # FILTER
    if department:
        query += " AND department = ?"
        count_query += " AND department = ?"
        params.append(department)
        count_params.append(department)

    # SORT + PAGINATION
    query += f" ORDER BY {sort_by} {order.upper()} LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    cursor.execute(query, params)
    data = cursor.fetchall()

    cursor.execute(count_query, count_params)
    total = cursor.fetchone()[0]

    conn.close()

    return data, total


# UPDATE EMPLOYEE
def update_employee(emp_id, data):
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


# DELETE EMPLOYEE (SOFT DELETE)
def delete_employee(emp_id):
    with sqlite3.connect(database.DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE employees
            SET is_active = 0
            WHERE emp_id = ?
        """, (emp_id,))

        conn.commit()

        return cursor.rowcount > 0 