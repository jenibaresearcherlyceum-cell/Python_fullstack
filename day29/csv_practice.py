import csv

# CSV EXPORT 
employees = [
    {"id": 1, "name": "Ram", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"},
    {"id": 3, "name": "John", "department": "Finance"}
]

# Create CSV

def export_employees_to_csv(filename="employees.csv"):

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["ID", "Name", "Department"])

        # Rows
        for emp in employees:
            writer.writerow([
                emp["id"],
                emp["name"],
                emp["department"]
            ])

    return {
        "status": "success",
        "message": f"{filename} generated successfully"
    }


# Download Response Simulation

def download_response():
    return {
        "status": "success",
        "headers": {
            "Content-Disposition": "attachment; filename=employees.csv"
        }
    }


# Demo Execution

if __name__ == "__main__":

    print("=== CSV Export Practice ===")

    print(export_employees_to_csv())
    print(download_response())