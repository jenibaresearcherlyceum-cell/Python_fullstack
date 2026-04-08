<<<<<<< HEAD
def perform_action(role):
    if role == "admin":
        return {
            "status": "success",
            "message": "Full access granted"
        }
    else:
        return {
            "status": "success",
            "message": "Limited access"
        }


# Restricted Delete

def delete_employee(emp_id, role):

    if role != "admin":
        return {
            "status": "error",
            "message": "Access denied. Only admin can delete."
        }

    global employees
    employees = [emp for emp in employees if emp["id"] != emp_id]

    return {
        "status": "success",
        "message": "Employee deleted successfully"
    }

# Demo Execution

if __name__ == "__main__":

    print("=== RBAC Practice ===")

    print("\nAdmin Access:")
    print(perform_action("admin"))

    print("\nStaff Access:")
    print(perform_action("staff"))

    print("\nDelete Attempt by Staff:")
    print(delete_employee(1, "staff"))

    print("\nDelete Attempt by Admin:")
=======
def perform_action(role):
    if role == "admin":
        return {
            "status": "success",
            "message": "Full access granted"
        }
    else:
        return {
            "status": "success",
            "message": "Limited access"
        }


# Restricted Delete

def delete_employee(emp_id, role):

    if role != "admin":
        return {
            "status": "error",
            "message": "Access denied. Only admin can delete."
        }

    global employees
    employees = [emp for emp in employees if emp["id"] != emp_id]

    return {
        "status": "success",
        "message": "Employee deleted successfully"
    }

# Demo Execution

if __name__ == "__main__":

    print("=== RBAC Practice ===")

    print("\nAdmin Access:")
    print(perform_action("admin"))

    print("\nStaff Access:")
    print(perform_action("staff"))

    print("\nDelete Attempt by Staff:")
    print(delete_employee(1, "staff"))

    print("\nDelete Attempt by Admin:")
>>>>>>> 22031014cf25f8636d0293228d2970b67ec231f8
    print(delete_employee(1, "admin"))