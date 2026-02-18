## Task1 — Loop Optimization

task_map = {}         # Pre-group tasks by employee

for task in tasks:
    if task.emp_id not in task_map:
        task_map[task.emp_id] = []
    task_map[task.emp_id].append(task)

# Now single loop
for emp in employees:
    if emp.emp_id in task_map:
        for task in task_map[emp.emp_id]:
            print(task.title)

##Task2 — Reduce Repeated File Writes

employees = []

def add_employee(emp):
    employees.append(emp)

def delete_employee(emp_id):
    global employees
    employees = [emp for emp in employees if emp.emp_id != emp_id]

def save_all():
    with open("data.txt", "w") as f:
        for emp in employees:
            f.write(f"{emp.emp_id},{emp.name}\n")

# Perform multiple operations
add_employee(emp1)
add_employee(emp2)
delete_employee(101)

# Save once
save_all()


##Task3 — Efficient Lookup

import time

start = time.time()
# list search code
end = time.time()
print("List time:", end - start)

start = time.time()
# dictionary lookup
end = time.time()
print("Dict time:", end - start)

