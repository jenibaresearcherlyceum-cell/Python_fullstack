import json
from employee import Employee
from task import Task

EMP_FILE = "project/data/employees.json"
TASK_FILE = "project/data/tasks.json"

def save_employees(employees):
    with open(EMP_FILE, "w") as file:
        json.dump([emp.to_dict() for emp in employees], file, indent=4)

def load_employees():
    try:
        with open(EMP_FILE, "r") as file:
            data = json.load(file)
            return [Employee.from_dict(emp) for emp in data]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            data = json.load(file)
            return [Task.from_dict(task) for task in data]
    except FileNotFoundError:
        return []
