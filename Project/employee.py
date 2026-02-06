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

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["emp_id"],
            data["name"],
            data["department"],
            data["designation"]
        )

    def display(self):
        print(self.emp_id, self.name, self.department, self.designation)
e1=Employee(101,"Jeni","CSE","Software Testing")
e1.display()