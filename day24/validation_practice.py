<<<<<<< HEAD
#sample storage
employees = []

# Validation Function

def validate_employee(data):

    # Required Field Validation
    if "name" not in data:
        return {"status": "error", "message": "Name is required"}

    if "emp_id" not in data:
        return {"status": "error", "message": "Employee ID is required"}

    name = data.get("name")
    emp_id = data.get("emp_id")

    # Data Type Validation
    if not isinstance(emp_id, int):
        return {"status": "error", "message": "emp_id must be integer"}

    # String Length Validation
    if len(name) < 3:
        return {"status": "error", "message": "Name must be at least 3 characters"}

    return {"status": "success"}


# Add Employee with Validation

def add_employee(data):

    validation = validate_employee(data)

    if validation["status"] == "error":
        return validation

    # Data Sanitization
    clean_data = {
        "emp_id": data["emp_id"],
        "name": data["name"].strip()
    }

    employees.append(clean_data)

    return {
        "status": "success",
        "message": "Employee added successfully",
        "data": clean_data
    }

# Demo Execution

if __name__ == "__main__":

    print("=== Validation Practice ===")

    # Invalid Data (missing name)
    print(add_employee({"emp_id": 1}))

    # Invalid Data (wrong type)
    print(add_employee({"emp_id": "abc", "name": "Jo"}))

    # Invalid Data (short name)
    print(add_employee({"emp_id": 2, "name": "Jo"}))

    # Valid Data
=======
#sample storage
employees = []

# Validation Function

def validate_employee(data):

    # Required Field Validation
    if "name" not in data:
        return {"status": "error", "message": "Name is required"}

    if "emp_id" not in data:
        return {"status": "error", "message": "Employee ID is required"}

    name = data.get("name")
    emp_id = data.get("emp_id")

    # Data Type Validation
    if not isinstance(emp_id, int):
        return {"status": "error", "message": "emp_id must be integer"}

    # String Length Validation
    if len(name) < 3:
        return {"status": "error", "message": "Name must be at least 3 characters"}

    return {"status": "success"}


# Add Employee with Validation

def add_employee(data):

    validation = validate_employee(data)

    if validation["status"] == "error":
        return validation

    # Data Sanitization
    clean_data = {
        "emp_id": data["emp_id"],
        "name": data["name"].strip()
    }

    employees.append(clean_data)

    return {
        "status": "success",
        "message": "Employee added successfully",
        "data": clean_data
    }

# Demo Execution

if __name__ == "__main__":

    print("=== Validation Practice ===")

    # Invalid Data (missing name)
    print(add_employee({"emp_id": 1}))

    # Invalid Data (wrong type)
    print(add_employee({"emp_id": "abc", "name": "Jo"}))

    # Invalid Data (short name)
    print(add_employee({"emp_id": 2, "name": "Jo"}))

    # Valid Data
>>>>>>> 22031014cf25f8636d0293228d2970b67ec231f8
    print(add_employee({"emp_id": 3, "name": "  John  "}))