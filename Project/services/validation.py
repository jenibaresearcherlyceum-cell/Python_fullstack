<<<<<<< HEAD
def validate_employee(data):
    if not data.get("emp_id"):
        return "emp_id is required"

    if not isinstance(data.get("emp_id"), int):
        return "emp_id must be integer"

    name = data.get("name", "").strip()
    if not name:
        return "name is required"

    department = data.get("department", "").strip()
    if not department:
        return "department is required"

    designation = data.get("designation", "").strip()
    if not designation:
        return "designation is required"

    return None

def validate_task(data):
    if not data.get("task_id"):
        return "task_id is required"

    if not isinstance(data.get("task_id"), int):
        return "task_id must be integer"

    title = data.get("title", "").strip()
    if not title:
        return "title is required"

    if not data.get("assigned_to"):
        return "assigned_to is required"
    
    if not isinstance(data.get("assigned_to"), int):
        return "assigned_to must be integer"

=======
def validate_employee(data):
    if not data.get("emp_id"):
        return "emp_id is required"

    if not isinstance(data.get("emp_id"), int):
        return "emp_id must be integer"

    name = data.get("name", "").strip()
    if not name:
        return "name is required"

    department = data.get("department", "").strip()
    if not department:
        return "department is required"

    designation = data.get("designation", "").strip()
    if not designation:
        return "designation is required"

    return None

def validate_task(data):
    if not data.get("task_id"):
        return "task_id is required"

    if not isinstance(data.get("task_id"), int):
        return "task_id must be integer"

    title = data.get("title", "").strip()
    if not title:
        return "title is required"

    if not data.get("assigned_to"):
        return "assigned_to is required"
    
    if not isinstance(data.get("assigned_to"), int):
        return "assigned_to must be integer"

>>>>>>> 22031014cf25f8636d0293228d2970b67ec231f8
    return None