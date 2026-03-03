from services import employee_service


# GET Employees
def view_employees_controller():
    employees = employee_service.view_employees()

    return {
        "status": "success",
        "message": "Employees fetched successfully",
        "data": employees
    }


# ADD Employee
def add_employee_controller(emp_id, name, department, designation):
    try:
        employee_service.add_employee(emp_id, name, department, designation)

        return {
            "status": "success",
            "message": "Employee added successfully"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# UPDATE Employee
def update_employee_controller(emp_id, data):
    updated = employee_service.update_employee(emp_id, data)

    if not updated:
        return {
            "status": "error",
            "message": "Employee not found"
        }

    return {
        "status": "success",
        "message": "Employee updated successfully"
    }


# DELETE Employee (Soft Delete)
def delete_employee_controller(emp_id):
    deleted = employee_service.delete_employee(emp_id)

    if not deleted:
        return {
            "status": "error",
            "message": "Employee not found"
        }

    return {
        "status": "success",
        "message": "Employee deleted successfully"
    }