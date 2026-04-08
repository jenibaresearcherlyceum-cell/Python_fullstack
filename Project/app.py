<<<<<<< HEAD
from auth_middleware import verify_token
import jwt
import datetime
import os
from flask import Flask, request
from flask_cors import CORS
from controllers.auth_controller import (
    register_controller,
    login_controller
)
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
from controllers.dashboard_controller import (
    dashboard_controller,
    department_dashboard_controller,
    task_dashboard_controller
)
from controllers.export_controller import (
    export_employees_controller,
    export_tasks_controller
)

from database import initialize_database

app = Flask(__name__)
CORS(app)
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")

initialize_database()

@app.route("/")
def home():
    return {"message": "College Management API Running"}, 200


# ================= EMPLOYEE APIs =================

# GET ALL EMPLOYEES 
@app.route("/employees", methods=["GET"])
def get_employees():
    response =  view_employees_controller()
    return response

# ADD EMPLOYEE
@app.route("/employees", methods=["POST"])
def create_employee():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    data = request.json

    if not data or "name" not in data:
        return {"status": "error", "message": "Missing required fields"}, 400

    response = add_employee_controller(
        data.get("emp_id"),
        data.get("name"),
        data.get("department"),
        data.get("designation")
    )

    return response


# UPDATE EMPLOYEE 
@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    data = request.json
    response = update_employee_controller(emp_id, data)
    return response

# DELETE EMPLOYEE 
@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    response = delete_employee_controller(emp_id)
    return response


# ================= TASK APIs =================

# GET TASKS
@app.route("/tasks", methods=["GET"])
def get_tasks():
    response = view_tasks_controller()
    return response


# CREATE TASK 
@app.route("/tasks", methods=["POST"])
def create_task():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    data = request.json
    response = add_task_controller(data)
    return response


# UPDATE TASK 
@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    data = request.json
    response = update_task_controller(task_id, data)
    return response


# DELETE TASK 
@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    response = delete_task_controller(task_id)
    return response


# ================= DASHBOARD APIs =================

@app.route("/dashboard", methods=["GET"])
def get_dashboard():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status
    
    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    return dashboard_controller()


@app.route("/dashboard/departments", methods=["GET"])
def get_department_dashboard():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status
    
    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    return department_dashboard_controller()


@app.route("/dashboard/tasks", methods=["GET"])
def get_task_dashboard():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status
    
    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403


    return task_dashboard_controller()

# ================= EXPORT APIs =================

@app.route("/export/employees", methods=["GET"])
def export_employees():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    return export_employees_controller()


@app.route("/export/tasks", methods=["GET"])
def export_tasks():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    return export_tasks_controller()

# ================= AUTH APIs =================

# REGISTER
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    response = register_controller(data)
    return response


# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    response, status_code = login_controller(data)

    if response["status"] == "success":

        payload = {
            "username": data["username"],
            "role": response["data"]["role"],  
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return {
            "status": "success",
            "message": "Login successful",
            "token": token,
            "user": {
                "username": data["username"]
            }
        }, 200

    return response, status_code


if __name__ == "__main__":
=======
from auth_middleware import verify_token
import jwt
import datetime
import os
from flask import Flask, request
from controllers.auth_controller import (
    register_controller,
    login_controller
)
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
from controllers.dashboard_controller import (
    dashboard_controller,
    department_dashboard_controller,
    task_dashboard_controller
)
from controllers.export_controller import (
    export_employees_controller,
    export_tasks_controller
)

from database import initialize_database

app = Flask(__name__)
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")

initialize_database()

@app.route("/")
def home():
    return {"message": "College Management API Running"}, 200


# ================= EMPLOYEE APIs =================

# GET ALL EMPLOYEES 
@app.route("/employees", methods=["GET"])
def get_employees():
    response =  view_employees_controller()
    return response

# ADD EMPLOYEE
@app.route("/employees", methods=["POST"])
def create_employee():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    data = request.json

    if not data or "name" not in data:
        return {"status": "error", "message": "Missing required fields"}, 400

    response = add_employee_controller(
        data.get("emp_id"),
        data.get("name"),
        data.get("department"),
        data.get("designation")
    )

    return response


# UPDATE EMPLOYEE 
@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    data = request.json
    response = update_employee_controller(emp_id, data)
    return response

# DELETE EMPLOYEE 
@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    response = delete_employee_controller(emp_id)
    return response


# ================= TASK APIs =================

# GET TASKS
@app.route("/tasks", methods=["GET"])
def get_tasks():
    response = view_tasks_controller()
    return response


# CREATE TASK 
@app.route("/tasks", methods=["POST"])
def create_task():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    data = request.json
    response = add_task_controller(data)
    return response


# UPDATE TASK 
@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    data = request.json
    response = update_task_controller(task_id, data)
    return response


# DELETE TASK 
@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    response = delete_task_controller(task_id)
    return response


# ================= DASHBOARD APIs =================

@app.route("/dashboard", methods=["GET"])
def get_dashboard():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status
    
    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    return dashboard_controller()


@app.route("/dashboard/departments", methods=["GET"])
def get_department_dashboard():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status
    
    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    return department_dashboard_controller()


@app.route("/dashboard/tasks", methods=["GET"])
def get_task_dashboard():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status
    
    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403


    return task_dashboard_controller()

# ================= EXPORT APIs =================

@app.route("/export/employees", methods=["GET"])
def export_employees():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    return export_employees_controller()


@app.route("/export/tasks", methods=["GET"])
def export_tasks():
    auth_response, status = verify_token()

    if status != 200:
        return auth_response, status

    user_data = auth_response.get("data", {})

    if user_data.get("role") != "admin":
        return {"status": "error", "message": "Access denied"}, 403

    return export_tasks_controller()

# ================= AUTH APIs =================

# REGISTER
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    response = register_controller(data)
    return response


# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    response, status_code = login_controller(data)

    if response["status"] == "success":

        payload = {
            "username": data["username"],
            "role": response["data"]["role"],  
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return {
            "status": "success",
            "message": "Login successful",
            "token": token,
            "user": {
                "username": data["username"]
            }
        }, 200

    return response, status_code


if __name__ == "__main__":
>>>>>>> 22031014cf25f8636d0293228d2970b67ec231f8
    app.run(host="0.0.0.0", port=5000, debug=True)