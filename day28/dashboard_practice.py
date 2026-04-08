<<<<<<< HEAD
# Sample Data
employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"},
    {"id": 3, "name": "Bob", "department": "IT"},
    {"id": 4, "name": "Ramya", "department": "Finance"}
]

tasks = [
    {"id": 1, "title": "Bug Fix", "status": "Pending"},
    {"id": 2, "title": "Testing", "status": "Completed"},
    {"id": 3, "title": "Deployment", "status": "Pending"},
    {"id": 4, "title": "Report", "status": "In Progress"}
]


# Total Employees

def count_employees():
    return len(employees)

# Group by Department

def department_summary():
    summary = {}

    for emp in employees:
        dept = emp["department"]
        summary[dept] = summary.get(dept, 0) + 1

    return summary


# Task Status Count

def task_status_summary():
    summary = {}

    for task in tasks:
        status = task["status"]
        summary[status] = summary.get(status, 0) + 1

    return summary


# Dashboard Summary API

def dashboard_summary():
    return {
        "status": "success",
        "data": {
            "total_employees": count_employees(),
            "total_tasks": len(tasks),
            "department_summary": department_summary(),
            "task_status_summary": task_status_summary()
        }
    }


# Execution

if __name__ == "__main__":

    print("=== Dashboard Summary ===")
=======
# Sample Data
employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"},
    {"id": 3, "name": "Bob", "department": "IT"},
    {"id": 4, "name": "Ramya", "department": "Finance"}
]

tasks = [
    {"id": 1, "title": "Bug Fix", "status": "Pending"},
    {"id": 2, "title": "Testing", "status": "Completed"},
    {"id": 3, "title": "Deployment", "status": "Pending"},
    {"id": 4, "title": "Report", "status": "In Progress"}
]


# Total Employees

def count_employees():
    return len(employees)

# Group by Department

def department_summary():
    summary = {}

    for emp in employees:
        dept = emp["department"]
        summary[dept] = summary.get(dept, 0) + 1

    return summary


# Task Status Count

def task_status_summary():
    summary = {}

    for task in tasks:
        status = task["status"]
        summary[status] = summary.get(status, 0) + 1

    return summary


# Dashboard Summary API

def dashboard_summary():
    return {
        "status": "success",
        "data": {
            "total_employees": count_employees(),
            "total_tasks": len(tasks),
            "department_summary": department_summary(),
            "task_status_summary": task_status_summary()
        }
    }


# Execution

if __name__ == "__main__":

    print("=== Dashboard Summary ===")
>>>>>>> 22031014cf25f8636d0293228d2970b67ec231f8
    print(dashboard_summary())