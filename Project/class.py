class Task:

    def __init__(self, task_id, title, assigned_to, status):
        self.task_id = task_id
        self.title = title
        self.assigned_to = assigned_to
        self.status = status


    def update_status(self, new_status):
        self.status = new_status
        print("Task status updated successfully.")


    def display_task(self):
        print("------ Task Details ------")
        print(f"Task ID      : {self.task_id}")
        print(f"Title        : {self.title}")
        print(f"Assigned To  : {self.assigned_to}")
        print(f"Status       : {self.status}")
        
t1 = Task("T101", "Complete Project", "Jeni", "Pending")

t1.display_task()

t1.update_status("Completed")

t1.display_task()
