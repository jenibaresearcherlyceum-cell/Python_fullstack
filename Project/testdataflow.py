from employee import Employee
from file_handler import save_employees, load_employees

emp1 = Employee(1, "Anu", "IT", "Developer")

save_employees([emp1])

employees = load_employees()

for emp in employees:
    emp.display()
