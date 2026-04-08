<<<<<<< HEAD
# Sample Data
employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"},
    {"id": 3, "name": "Ramesh", "department": "IT"},
    {"id": 4, "name": "Ramya", "department": "Finance"},
    {"id": 5, "name": "Joseph", "department": "IT"}
]


# Search Function like this format

def search_employees(data, keyword):
    return [
        emp for emp in data
        if keyword.lower() in emp["name"].lower()
    ]


# Multi-Filter Logic like this format


def filter_employees(data, name=None, department=None):

    result = data

    if name:
        result = search_employees(result, name)

    if department:
        result = [emp for emp in result if emp["department"] == department]

    return result


# Combined API Logic
def get_employees(name=None, department=None):

    result = filter_employees(employees, name, department)

    return {
        "status": "success",
        "count": len(result),
        "data": result
    }


# Demo Execution

if __name__ == "__main__":

    print("=== filter by name or department ===")

    # Search by name
    print(get_employees(name="ram"))

    # Filter by department
    print(get_employees(department="IT"))

    # Both filters
    print(get_employees(name="jo", department="IT"))
=======
# Sample Data
employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"},
    {"id": 3, "name": "Ramesh", "department": "IT"},
    {"id": 4, "name": "Ramya", "department": "Finance"},
    {"id": 5, "name": "Joseph", "department": "IT"}
]


# Search Function like this format

def search_employees(data, keyword):
    return [
        emp for emp in data
        if keyword.lower() in emp["name"].lower()
    ]


# Multi-Filter Logic like this format


def filter_employees(data, name=None, department=None):

    result = data

    if name:
        result = search_employees(result, name)

    if department:
        result = [emp for emp in result if emp["department"] == department]

    return result


# Combined API Logic
def get_employees(name=None, department=None):

    result = filter_employees(employees, name, department)

    return {
        "status": "success",
        "count": len(result),
        "data": result
    }


# Demo Execution

if __name__ == "__main__":

    print("=== filter by name or department ===")

    # Search by name
    print(get_employees(name="ram"))

    # Filter by department
    print(get_employees(department="IT"))

    # Both filters
    print(get_employees(name="jo", department="IT"))
>>>>>>> 22031014cf25f8636d0293228d2970b67ec231f8
    #if we want add like the designation ,status like that