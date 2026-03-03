from flask import Flask, request
from controllers.employee_controller import (
    view_employees_controller,
    add_employee_controller,
    update_employee_controller,
    delete_employee_controller
)
from controllers.task_controller import (
    view_tasks_controller,
    add_task_controller,
    update_task_controller,
    delete_task_controller
)

from database import initialize_database

app = Flask(__name__)
initialize_database()


@app.route("/")
def home():
    return {"message": "College Management API Running"}, 200


# ================= EMPLOYEE APIs =================

# GET ALL EMPLOYEES
@app.route("/employees", methods=["GET"])
def get_employees():
    response = view_employees_controller()
    return response, 200


# ADD EMPLOYEE
@app.route("/employees", methods=["POST"])
def create_employee():
    data = request.json

    if not data or "name" not in data:
        return {"status": "error", "message": "Missing required fields"}, 400

    response = add_employee_controller(
        data.get("emp_id"),
        data.get("name"),
        data.get("department"),
        data.get("designation")
    )

    return response, 201


# UPDATE EMPLOYEE
@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    data = request.json
    response = update_employee_controller(emp_id, data)
    return response, 200


# DELETE EMPLOYEE (Soft Delete)
@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    response = delete_employee_controller(emp_id)
    return response, 200

# ================= TASK APIs =================

@app.route("/tasks", methods=["GET"])
def get_tasks():
    response = view_tasks_controller()
    return response, 200


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    response = add_task_controller(data)
    return response, 201


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    response = update_task_controller(task_id, data)
    return response, 200


@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    response = delete_task_controller(task_id)
    return response, 200

if __name__ == "__main__":
    app.run(debug=True)
