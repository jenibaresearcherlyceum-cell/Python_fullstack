import jwt
from flask import request

SECRET_KEY = "mysecretkey"

def verify_token():

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return {"status": "error", "message": "Token missing"}, 401

    try:
        parts = auth_header.strip().split(" ")

        if len(parts) != 2 or parts[0] != "Bearer":
            return {"status": "error", "message": "Invalid header format"}, 401

        token = parts[1]

        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        return {
                "status": "success",
                "data": decoded
                }, 200

    except jwt.ExpiredSignatureError:
        return {"status": "error", "message": "Token expired"}, 401

    except jwt.InvalidTokenError:
        return {"status": "error", "message": "Invalid token"}, 401