# simulating database
employees = []
tasks = []

# GET - View Employees

def get_employees():
    return {
        "status": "success",
        "data": employees
    }

# POST - Add Employee

def add_employee(data):
    employees.append(data)

    return {
        "status": "success",
        "message": "Employee added successfully",
        "data": data
    }


# PUT - Update Task

def update_task(task_id, new_status):
    for task in tasks:
        if task["task_id"] == task_id:
            task["status"] = new_status
            return {
                "status": "success",
                "message": "Task updated",
                "data": task
            }

    return {
        "status": "error",
        "message": "Task not found"
    }


# DELETE - Delete Employee

def delete_employee(emp_id):
    global employees
    employees = [emp for emp in employees if emp["emp_id"] != emp_id]

    return {
        "status": "success",
        "message": "Employee deleted"
    }


# DEMO EXECUTION

if __name__ == "__main__":

    print("=== API Simulation ===")

    # POST
    print("\nAdding Employee...")
    response = add_employee({
        "emp_id": 1,
        "name": "John",
        "department": "IT"
    })
    print(response)

    # GET
    print("\nFetching Employees...")
    print(get_employees())

    # DELETE
    print("\nDeleting Employee...")
    print(delete_employee(1))

    # GET again
    print("\nFetching Employees Again...")
    print(get_employees())