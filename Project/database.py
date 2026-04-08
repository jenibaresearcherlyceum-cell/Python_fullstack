<<<<<<< HEAD
import sqlite3

DB_NAME = "college.db"


def initialize_database():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
               emp_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                designation TEXT NOT NULL,
                is_active INTEGER DEFAULT 1
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                task_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                assigned_to TEXT,
                status TEXT DEFAULT 'Pending',
                FOREIGN KEY (assigned_to) REFERENCES employees(emp_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)

# ---------------- EMPLOYEE OPERATIONS ----------------

def insert_employee(employee):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO employees VALUES (?, ?, ?, ?, ?)
        """, (employee.emp_id, employee.name,
              employee.department, employee.designation,
              int(employee.is_active)))


def fetch_employees():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        return cursor.fetchall()


def soft_delete_employee(emp_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE employees
            SET is_active = 0
            WHERE emp_id = ?
        """, (emp_id,))


# ---------------- TASK OPERATIONS ----------------

def insert_task(task):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks VALUES (?, ?, ?, ?, ?)
        """, (task.task_id, task.title,
              task.description, task.assigned_to,
              task.status))


def fetch_tasks():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        return cursor.fetchall()


def update_task_status(task_id, new_status):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tasks
            SET status = ?
            WHERE task_id = ?
=======
import sqlite3

DB_NAME = "college.db"


def initialize_database():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
               emp_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                designation TEXT NOT NULL,
                is_active INTEGER DEFAULT 1
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                task_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                assigned_to TEXT,
                status TEXT DEFAULT 'Pending',
                FOREIGN KEY (assigned_to) REFERENCES employees(emp_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)

# ---------------- EMPLOYEE OPERATIONS ----------------

def insert_employee(employee):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO employees VALUES (?, ?, ?, ?, ?)
        """, (employee.emp_id, employee.name,
              employee.department, employee.designation,
              int(employee.is_active)))


def fetch_employees():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        return cursor.fetchall()


def soft_delete_employee(emp_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE employees
            SET is_active = 0
            WHERE emp_id = ?
        """, (emp_id,))


# ---------------- TASK OPERATIONS ----------------

def insert_task(task):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks VALUES (?, ?, ?, ?, ?)
        """, (task.task_id, task.title,
              task.description, task.assigned_to,
              task.status))


def fetch_tasks():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        return cursor.fetchall()


def update_task_status(task_id, new_status):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tasks
            SET status = ?
            WHERE task_id = ?
>>>>>>> 22031014cf25f8636d0293228d2970b67ec231f8
        """, (new_status, task_id))