# SORTING + SEARCH + FILTER 

# Sample Data
employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"},
    {"id": 3, "name": "Ramesh", "department": "IT"},
    {"id": 4, "name": "Ramya", "department": "Finance"},
    {"id": 5, "name": "Joseph", "department": "IT"}
]


# Search Function

def search_employees(data, keyword):
    return [emp for emp in data if keyword.lower() in emp["name"].lower()]


# Filter Function

def filter_employees(data, name=None, department=None):

    result = data

    if name:
        result = search_employees(result, name)

    if department:
        result = [emp for emp in result if emp["department"] == department]

    return result


# Sorting Function

def sort_employees(data, sort_by="name", order="asc"):

    reverse = True if order == "desc" else False

    return sorted(data, key=lambda x: x.get(sort_by), reverse=reverse)


# Combined API Logic

def get_employees(name=None, department=None, sort_by="name", order="asc"):

    result = filter_employees(employees, name, department)

    result = sort_employees(result, sort_by, order)

    return {
        "status": "success",
        "count": len(result),
        "data": result
    }

# Demo Execution

if __name__ == "__main__":

    print("=== Sorting Practice ===")

    # Ascending
    print(get_employees(sort_by="name", order="asc"))

    # Descending
    print(get_employees(sort_by="name", order="desc"))

    # Filter + Sort
    print(get_employees(department="IT", order="desc"))

    # Search + Sort
    print(get_employees(name="ra", order="asc"))