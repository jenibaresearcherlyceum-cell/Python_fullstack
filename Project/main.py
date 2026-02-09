from employee import Employee
from task import Task
from file_handler import save_employees, load_employees, save_tasks, load_tasks


def main():
    # Load data at startup
    employees = load_employees()
    tasks = load_tasks()
    while True:
        print("\n---- MAIN MENU ----")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Add Task")
        print("4. Update Task Status")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            designation = input("Enter Designation: ")

            emp = Employee(emp_id, name, department, designation)
            employees.append(emp)
            save_employees(employees)

            print("Employee Added Successfully ")

        elif choice == "2":
            for emp in employees:
                emp.display()

        elif choice == "3":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            assigned_to = input("Enter Employee ID to assign: ")

            # Check if employee exists
            emp_exists = any(emp.emp_id == assigned_to for emp in employees)

            if not emp_exists:
                print("Employee not found ")
            else:
                task = Task(task_id, title, description, assigned_to, "Assigned")
                tasks.append(task)
                save_tasks(tasks)
                print("Task Assigned Successfully ")

        elif choice == "4":
            task_id = input("Enter Task ID: ")

            for task in tasks:
                if task.task_id == task_id:
                    new_status = input("Enter New Status (Assigned/In Progress/Completed): ")
                    task.status = new_status
                    save_tasks(tasks)
                    print("Status Updated ")
                    break
            else:
                print("Task not found ")

        elif choice == "5":
            print("Saving data and exiting...")
            save_employees(employees)
            save_tasks(tasks)
            break

        else:
            print("Invalid Choice ")


if __name__ == "__main__":
    main()
