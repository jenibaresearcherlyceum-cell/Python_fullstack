# Task1-safe_delete example:

employees = [
    {"id": 1, "name": "Arun"},
    {"id": 2, "name": "Divya"}
]

tasks = [
    {"task_id": 101, "emp_id": 1},
    {"task_id": 102, "emp_id": 2}
]


def delete_employee(emp_id):
    # Check if tasks exist
    for task in tasks:
        if task["emp_id"] == emp_id:
            print("Cannot delete employee. Tasks are assigned!")
            return

    # Safe to delete
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted successfully!")
            return

    print("Employee not found.")

#Task2 — Soft Delete Simulation:
def soft_delete_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            emp["is_active"] = False
            print("Employee marked as inactive.")
            return

    print("Employee not found.")


#Task3 — Orphan Prevention:
def delete_employee_with_tasks(emp_id):
    global tasks

    # Remove employee
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted.")

            # Remove related tasks
            tasks = [t for t in tasks if t["emp_id"] != emp_id]

            print("Associated tasks removed.")
            return

    print("Employee not found.")


