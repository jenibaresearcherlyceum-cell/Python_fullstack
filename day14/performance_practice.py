import json
employees = [
    {"emp_id": 1, "name": "Arun"},
    {"emp_id": 2, "name": "Meena"},
    {"emp_id": 3, "name": "Karthik"}
]

tasks = [
    {"task_id": 101, "title": "Design UI", "emp_id": 1},
    {"task_id": 102, "title": "Backend API", "emp_id": 2},
    {"task_id": 103, "title": "Testing", "emp_id": 1}
]

# Pre-group tasks by employee using dictionary
task_map = {}

for task in tasks:
    emp_id = task["emp_id"]
    if emp_id not in task_map:
        task_map[emp_id] = []
    task_map[emp_id].append(task)

print("Employee Tasks (Optimized Lookup):")

for emp in employees:
    emp_id = emp["emp_id"]
    print(f"\nEmployee: {emp['name']}")
    if emp_id in task_map:
        for task in task_map[emp_id]:
            print(" -", task["title"])
    else:
        print(" No tasks assigned")

# Convert employee list to dictionary
employee_dict = {emp["emp_id"]: emp for emp in employees}

print("\nDictionary Lookup Example:")
search_id = 2
if search_id in employee_dict:
    print("Found Employee:", employee_dict[search_id]["name"])

def save_data():
    data = {
        "employees": employees,
        "tasks": tasks
    }
    with open("project_data.json", "w") as f:
        json.dump(data, f, indent=4)

# Perform multiple operations in memory
employees.append({"emp_id": 4, "name": "Divya"})
tasks.append({"task_id": 104, "title": "Deployment", "emp_id": 3})

# Save once (Batch Save)
save_data()

print("\nData saved successfully using batch save.")
