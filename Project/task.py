class Employee:
    def __init__(self, emp_id, name, department, designation):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation
        }

    def display(self):
        print("----------- Employee Details -------------")
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Designation: {self.designation}")


# Object creation (outside the class)
e1 = Employee("E101", "Jeni", "CSE", "Developer")
e1.display()
