class Task:
    def __init__(self, task_id, title, description, assigned_to, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "assigned_to": self.assigned_to,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["task_id"],
            data["title"],
            data["description"],
            data["assigned_to"],
            data["status"]
        )

    def display(self):
        print(self.task_id, self.title, self.status)
