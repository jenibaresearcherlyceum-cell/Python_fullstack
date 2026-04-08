from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
employees = []
current_id = 1

# CREATE (POST)
@app.route("/employees", methods=["POST"])
def add_employee():
    global current_id

    data = request.get_json()

    if not data or "name" not in data or "department" not in data:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

    employee = {
        "id": current_id,
        "name": data["name"],
        "department": data["department"]
    }

    employees.append(employee)
    current_id += 1

    return jsonify({
        "status": "success",
        "message": "Employee created",
        "data": employee
    }), 201

# READ (GET)
@app.route("/employees", methods=["GET"])
def get_employee():
    return jsonify({
        "status": "success",
        "data": employees
    }), 200


# UPDATE (PUT)
@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    data = request.get_json()

    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = data.get("name", emp["name"])
            emp["department"] = data.get("department", emp["department"])

            return jsonify({
                "status": "success",
                "message": "Employee updated",
                "data": emp
            }), 200

    return jsonify({"status": "error", "message": "Employee not found"}), 404


# DELETE (DELETE)
@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    global employees

    employees = [emp for emp in employees if emp["id"] != emp_id]

    return jsonify({
        "status": "success",
        "message": "Employee deleted"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
