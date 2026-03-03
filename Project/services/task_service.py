from task import Task
import database
import sqlite3

# ADD TASK
def add_task(task_id, title, description, assigned_to):
    task = Task(task_id, title, description, assigned_to)
    database.insert_task(task)


# VIEW TASKS
def view_tasks():
    return database.fetch_tasks()


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