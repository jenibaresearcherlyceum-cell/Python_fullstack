 #Task1– Refactor Long Function:

# AFTER REFACTOR (Clean & Structured)

def get_employee_input():
    emp_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    return emp_id, name, department


def is_duplicate(emp_id, employee_list):
    for emp in employee_list:
        if emp["id"] == emp_id:
            return True
    return False


def create_employee(emp_id, name, department):
    return {
        "id": emp_id,
        "name": name,
        "department": department
    }


def add_employee_new(employee_list):
    emp_id, name, department = get_employee_input()

    if is_duplicate(emp_id, employee_list):
        print("Duplicate ID!")
        return

    employee = create_employee(emp_id, name, department)
    employee_list.append(employee)

    print("Employee Added Successfully!")
    print(employee_list)


# Task2– Clean Naming Exercise:

# BEFORE (Bad Naming)

a = 101
b = "Anu"
x = []
y = "CSE"

# AFTER (Good Naming)

employee_id = 101
employee_name = "Anu"
employee_list = []
department_name = "CSE"


# Task3 – Remove Repeated Code:

# BEFORE (Repeated Save Logic)

def save_employees():
    print("Saving employees...")

def save_tasks():
    print("Saving tasks...")


# AFTER (Reusable Function)

def save_all_data():
    save_employees()
    save_tasks()
