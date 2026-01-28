employees = {}

def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter name: ")
    dept = input("Enter Department: ")
    salary = int(input("Enter salary: "))

    employees[emp_id] = {
        "Name": name,
        "Department": dept,
        "Salary": salary
    }
    print("Employee added successfully")

def display_employee():
    if not employees:
        print("No employees found")
    else:
        for emp_id, details in employees.items():
            print("\nEmployee ID:", emp_id)
            print("Name:", details["Name"])
            print("Department:", details["Department"])
            print("Salary:", details["Salary"])

def search_employee():
    emp_id = input("Search Employee ID: ")
    if emp_id in employees:
        details = employees[emp_id]
        print("Name:", details["Name"])
        print("Department:", details["Department"])
        print("Salary:", details["Salary"])
    else:
        print("Employee not found")

while True:
    print("\n1.Add Employee")
    print("2.Display Employee")
    print("3.Search Employee")
    print("4.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employee()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
