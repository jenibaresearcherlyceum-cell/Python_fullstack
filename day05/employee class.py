class Employee:
    
    def __init__(self,emp_id,name,department,salary):
      self.emp_id=emp_id
      self.name=name
      self.department=department
      self.salary=salary
      
    def display_employee(self):
        print("Employee ID:",self.emp_id)
        print("Name:",self.name)
        print("Department:",self.department)
        print("Salary:",self.salary)
        
e1=Employee(101,"Jeni","HR",25000)
e1.display_employee()
        

   
