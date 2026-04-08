<<<<<<< HEAD
# Sample Data
employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"},
    {"id": 3, "name": "Bob", "department": "IT"},
    {"id": 4, "name": "Eve", "department": "Finance"},
    {"id": 5, "name": "Sam", "department": "IT"},
    {"id": 6, "name": "Max", "department": "HR"},
    {"id": 7, "name": "Leo", "department": "IT"},
    {"id": 8, "name": "Nina", "department": "Finance"}
            ]


# Query Simulation

def get_employees(page=1, limit=3, department=None):

    result = employees

    # Filtering
    if department:
        result = filter_by_department (result, department)

    # Pagination
        result = paginate (result, page, limit)

        return {
        "status": "success",
        "page": page,
        "limit": limit,
        "data": result
        }

# Demo Execution

if __name__ == "__main__":

    print("=== Pagination Practice ===")

    # Page 1
    print(get_employees(page=1, limit=3))

    # Page 2
    print(get_employees(page=2, limit=3))

    # Filter IT + Pagination
=======
# Sample Data
employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"},
    {"id": 3, "name": "Bob", "department": "IT"},
    {"id": 4, "name": "Eve", "department": "Finance"},
    {"id": 5, "name": "Sam", "department": "IT"},
    {"id": 6, "name": "Max", "department": "HR"},
    {"id": 7, "name": "Leo", "department": "IT"},
    {"id": 8, "name": "Nina", "department": "Finance"}
            ]


# Query Simulation

def get_employees(page=1, limit=3, department=None):

    result = employees

    # Filtering
    if department:
        result = filter_by_department (result, department)

    # Pagination
        result = paginate (result, page, limit)

        return {
        "status": "success",
        "page": page,
        "limit": limit,
        "data": result
        }

# Demo Execution

if __name__ == "__main__":

    print("=== Pagination Practice ===")

    # Page 1
    print(get_employees(page=1, limit=3))

    # Page 2
    print(get_employees(page=2, limit=3))

    # Filter IT + Pagination
>>>>>>> 22031014cf25f8636d0293228d2970b67ec231f8
    print(get_employees(page=1, limit=2, department="IT"))