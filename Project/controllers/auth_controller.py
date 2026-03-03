from auth import login


def login_controller():
    username, role = login()

    if username:
        return {
            "status": "success",
            "message": "Login successful",
            "data": {
                "username": username,
                "role": role
            }
        }
    else:
        return {
            "status": "error",
            "message": "Login failed"
        }
