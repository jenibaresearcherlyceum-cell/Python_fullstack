from services import auth_service


# ================= REGISTER =================
def register_controller(data):
    try:
        auth_service.register_user(
            data["username"],
            data["password"],
            data["role"]
        )

        return {
            "status": "success",
            "message": "User registered successfully"
        }, 201

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 400


# ================= LOGIN =================
def login_controller(data):
    if not data.get("username"):
        return {"status": "error", "message": "username required"}, 400

    if not data.get("password"):
        return {"status": "error", "message": "password required"}, 400
    
    role = auth_service.login_user(
        data["username"],
        data["password"]
    )

    if role:
        return {
            "status": "success",
            "message": "Login successful",
            "data": {
                "role": role
            }
        }, 200

    return {
        "status": "error",
        "message": "Invalid credentials"      
        }, 401