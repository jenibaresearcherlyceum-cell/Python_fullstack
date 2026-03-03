from database import initialize_database
from controllers.employee_controller import (
    add_employee_controller,
    delete_employee_controller,
    view_employees_controller
)
from controllers.task_controller import (
    add_task_controller,
    update_task_status_controller,
    view_tasks_controller
)
from controllers.auth_controller import login_controller


def main():
    initialize_database()

    login_response = login_controller()

    if login_response["status"] == "error":
        print(login_response["message"])
        return

    while True:
        print("\n1. Add Employee")
        print("2. Delete Employee")
        print("3. Add Task")
        print("4. Update Task Status")
        print("5. View Employees")
        print("6. View Tasks")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            emp_id = input("Employee ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            desig = input("Designation: ")

            response = add_employee_controller(emp_id, name, dept, desig)
            print(response["message"])

        elif choice == "2":
            emp_id = input("Employee ID: ")
            response = delete_employee_controller(emp_id)
            print(response["message"])

        elif choice == "3":
            task_id = input("Task ID: ")
            title = input("Title: ")
            desc = input("Description: ")
            assigned = input("Assigned To: ")

            response = add_task_controller(task_id, title, desc, assigned)
            print(response["message"])

        elif choice == "4":
            task_id = input("Task ID: ")
            status = input("New Status: ")

            response = update_task_status_controller(task_id, status)
            print(response["message"])

        elif choice == "5":
            response = view_employees_controller()
            for emp in response["data"]:
                print(emp)

        elif choice == "6":
            response = view_tasks_controller()
            for task in response["data"]:
                print(task)

        elif choice == "7":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
