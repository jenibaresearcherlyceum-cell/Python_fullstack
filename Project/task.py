class Task:

    def __init__(self, task_id, title, description, assigned_to, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = status

   