from services import task_service


# GET ALL TASKS
def view_tasks_controller():
    tasks = task_service.view_tasks()

    return {
        "status": "success",
        "message": "Tasks fetched successfully",
        "data": tasks
    }


# CREATE TASK
def add_task_controller(data):
    try:
        task_service.add_task(
            data["task_id"],
            data["title"],
            data["description"],
            data["assigned_to"]
        )

        return {
            "status": "success",
            "message": "Task added successfully"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# UPDATE TASK
def update_task_controller(task_id, data):
    try:
        updated = task_service.update_task(task_id, data)

        if not updated:
            return {
                "status": "error",
                "message": "Task not found"
            }

        return {
            "status": "success",
            "message": "Task updated successfully"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# DELETE TASK
def delete_task_controller(task_id):
    deleted = task_service.delete_task(task_id)

    if not deleted:
        return {
            "status": "error",
            "message": "Task not found"
        }

    return {
        "status": "success",
        "message": "Task deleted successfully"
    }