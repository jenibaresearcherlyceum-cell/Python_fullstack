import jwt
import datetime

SECRET_KEY = "my_secret_key"

# Generate JWT Token

def generate_token(username):

    payload = {
        "user": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return {
        "status": "success",
        "token": token
    }


# Verify Token

def verify_token(token):

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        return {
            "status": "success",
            "message": "Token is valid",
            "data": decoded
        }

    except jwt.ExpiredSignatureError:
        return {
            "status": "error",
            "message": "Token expired"
        }

    except jwt.InvalidTokenError:
        return {
            "status": "error",
            "message": "Invalid token"
        }


# Demo Execution

if __name__ == "__main__":

    print("=== JWT Authentication Practice ===")

    # Generate Token
    response = generate_token("admin")
    print("Generated Token:")
    print(response)

    token = response["token"]

    print("\nVerifying Token...")
    print(verify_token(token))