1.Filter Employees:

print("---- CSE Employees ----")
cse_employees = [emp for emp in employees if emp["department"] == "CSE"]

for emp in cse_employees:
    print(emp)


2.Sorting:

# sorted by name
print("\n---- Employees Sorted by Name ----")
sorted_by_name = sorted(employees, key=lambda x: x["name"])
for emp in sorted_by_name:
    print(emp)

# Sort by Salary
print("\n---- Employees Sorted by Salary ----")
sorted_by_salary = sorted(employees, key=lambda x: x["salary"])
for emp in sorted_by_salary:
    print(emp)

3. Task Status Counter:

assigned = 0
in_progress = 0
completed = 0

for task in tasks:
    if task["status"] == "Assigned":
        assigned += 1
    elif task["status"] == "In Progress":
        in_progress += 1
    elif task["status"] == "Completed":
        completed += 1

print("\n---- Task Status Summary ----")
print("Assigned:", assigned)
print("In Progress:", in_progress)
print("Completed:", completed)

