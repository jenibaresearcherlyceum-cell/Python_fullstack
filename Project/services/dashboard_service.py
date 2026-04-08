import sqlite3
import database


# DASHBOARD MAIN SUMMARY
def get_dashboard_summary():
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    # total employees
    cursor.execute("SELECT COUNT(*) FROM employees WHERE is_active = 1")
    total_employees = cursor.fetchone()[0]

    # total tasks
    cursor.execute("SELECT COUNT(*) FROM tasks")
    total_tasks = cursor.fetchone()[0]

    # completed tasks
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE LOWER(status) = 'completed'")
    completed_tasks = cursor.fetchone()[0]

    # pending tasks
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE LOWER(status) = 'pending'")
    pending_tasks = cursor.fetchone()[0]

    conn.close()

    return {
        "total_employees": total_employees,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks
    }


# DEPARTMENT WISE EMPLOYEE COUNT
def get_department_summary():
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT department, COUNT(*)
        FROM employees
        WHERE is_active = 1
        GROUP BY department
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {"department": row[0], "count": row[1]}
        for row in rows
    ]


# TASK STATUS SUMMARY
def get_task_status_summary():
    conn = sqlite3.connect(database.DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status, COUNT(*)
        FROM tasks
        GROUP BY status
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {"status": row[0], "count": row[1]}
        for row in rows

    ]