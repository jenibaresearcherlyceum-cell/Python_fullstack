from task import Task
import database
import sqlite3


# CHECK EMPLOYEE EXISTS
def employee_exists(emp_id):
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees WHERE emp_id = ?", (emp_id,))
    result = cursor.fetchone()

    conn.close()
    return result is not None


# CHECK TASK EXISTS
def task_exists(task_id):
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,))
    result = cursor.fetchone()

    conn.close()
    return result is not None


# ADD TASK
def add_task(task_id, title, description, status, assigned_to):
    task = Task(task_id, title, description, status, assigned_to)
    database.insert_task(task)


# VIEW TASKS (SEARCH + PAGINATION + SORTING)
def view_tasks(page, limit, search=None, sort_by="task_id", order="asc"):
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    offset = (page - 1) * limit

    query = "SELECT * FROM tasks WHERE 1=1"
    count_query = "SELECT COUNT(*) FROM tasks WHERE 1=1"

    params = []
    count_params = []

    # SEARCH - case-insensitive
    if search:
        query += " AND LOWER(title) LIKE ?"
        count_query += " AND LOWER(title) LIKE ?"
        value = f"%{search.lower()}%"
        params.append(value)
        count_params.append(value)

    # SORTING
    query += f" ORDER BY {sort_by} {order.upper()}"

    # PAGINATION
    query += " LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    cursor.execute(query, params)
    data = cursor.fetchall()

    cursor.execute(count_query, count_params)
    total = cursor.fetchone()[0]

    conn.close()

    return data, total


# UPDATE TASK
def update_task(task_id, data):
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET title = ?, description = ?, assigned_to = ?, status = ?
        WHERE task_id = ?
    """, (
        data.get("title"),
        data.get("description"),
        data.get("assigned_to"),
        data.get("status"),
        task_id
    ))

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    return updated > 0


# DELETE TASK
def delete_task(task_id):
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE task_id = ?
    """, (task_id,))

    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    return deleted > 0