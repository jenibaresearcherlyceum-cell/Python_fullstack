import sqlite3
import database
import io
import csv


def export_employees_csv(department=None, search=None):
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    query = """
        SELECT emp_id, name, department, designation
        FROM employees
        WHERE is_active = 1
    """

    params = []

    if department:
        query += " AND department = ?"
        params.append(department)

    if search:
        query += " AND LOWER(name) LIKE ?"
        params.append(f"%{search.lower()}%")

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["emp_id", "name", "department", "designation"])
    writer.writerows(rows)

    return output.getvalue()


def export_tasks_csv(search=None):
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    query = """
        SELECT task_id, title, description, status, assigned_to
        FROM tasks
        WHERE 1=1
    """

    params = []

    if search:
        query += " AND LOWER(title) LIKE ?"
        params.append(f"%{search.lower()}%")

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["task_id", "title", "description", "status", "assigned_to"])
    writer.writerows(rows)

    return output.getvalue()