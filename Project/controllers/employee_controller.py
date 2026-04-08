from services.validation import validate_employee
from services import employee_service
from flask import request

# ADD EMPLOYEE
def add_employee_controller(emp_id, name, department, designation):

    name = name.strip() if name else ""
    department = department.strip() if department else ""
    designation = designation.strip() if designation else ""

    data = {
        "emp_id": emp_id,
        "name": name,
        "department": department,
        "designation": designation
    }

    

    # VALIDATION
    error = validate_employee(data)
    if error:
        return {
            "status": "error",
            "message": f"Invalid input: {error}"
        }, 400

    # DUPLICATE CHECK
    if employee_service.employee_exists(emp_id):
        return {
            "status": "error",
            "message": "Employee already exists"
        }, 400

    try:
        employee_service.add_employee(emp_id, name, department, designation)

        return {
            "status": "success",
            "message": "Employee added successfully"
        }, 201

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500


# VIEW EMPLOYEES
def view_employees_controller():

    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 5))
        department = request.args.get("department")
        search = request.args.get("search")
        sort_by = request.args.get("sort_by", "emp_id")
        order = request.args.get("order", "asc")

        if page <= 0 or limit <= 0:
            raise ValueError
        
        allowed_fields = ["emp_id", "name", "department"]
        allowed_order = ["asc", "desc"]

        if sort_by not in allowed_fields:
            return {"status": "error", "message": "Invalid sort field"}, 400

        if order.lower() not in allowed_order:
            return {"status": "error", "message": "Invalid order"}, 400

    except:
        return {
            "status": "error",
            "message": "Invalid query parameters"
        }, 400

    data, total = employee_service.view_employees(page, limit, department, search, sort_by, order)

    return {
        "status": "success",
        "data": data,
        "page": page,
        "limit": limit,
        "total": total
    }


# UPDATE
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


# DELETE
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