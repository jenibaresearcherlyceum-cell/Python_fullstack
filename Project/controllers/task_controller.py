from services.validation import validate_task
from services import task_service
from flask import request

# ADD TASK
def add_task_controller(data):

    # VALIDATION
    error = validate_task(data)
    if error:
        return {
            "status": "error",
            "message": f"Invalid input: {error}"
        }, 400
    
    
    #  DUPLICATE CHECK
    if task_service.task_exists(data["task_id"]):
        return {
        "status": "error",
        "message": "Task already exists"
    }, 400

    # CHECK EMPLOYEE EXISTS
    if not task_service.employee_exists(data["assigned_to"]):
        return {
            "status": "error",
            "message": "Assigned employee not found"
        }, 400

    try:
        task_service.add_task(
            data["task_id"],
            data["title"],
            data.get("description"),
            data.get("status"),
            data["assigned_to"]
        )

        return {
            "status": "success",
            "message": "Task added successfully"
        }, 201

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500

# VIEW TASKS
def view_tasks_controller():

    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 5))
        search = request.args.get("search")
        sort_by = request.args.get("sort_by", "task_id")
        order = request.args.get("order", "asc")

        if page <= 0 or limit <= 0:
            raise ValueError
        
        allowed_fields = ["task_id", "title", "status"]

        if sort_by not in allowed_fields:
            return {"status": "error", "message": "Invalid sort field"}, 400

        if order.lower() not in ["asc", "desc"]:
            return {"status": "error", "message": "Invalid order"}, 400

    except:
        return {
            "status": "error",
            "message": "Invalid query parameters"
        }, 400

    data, total = task_service.view_tasks(page, limit, search, sort_by, order)

    return {
        "status": "success",
        "data": data,
        "page": page,
        "limit": limit,
        "total": total
    }

# UPDATE
def update_task_controller(task_id, data):
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


# DELETE
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