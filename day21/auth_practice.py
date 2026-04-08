<<<<<<< HEAD
import bcrypt

users = {}

# Register Function (Hash Password)

def register(username, password):
    if username in users:
        return {
            "status": "error",
            "message": "User already exists"
        }

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed

    return {
        "status": "success",
        "message": "User registered successfully"
    }


# Login Function (Check Hashed Password)

def login(username, password):

    if username not in users:
        return {
            "status": "error",
            "message": "User not found"
        }

    stored_hash = users[username]

    if bcrypt.checkpw(password.encode(), stored_hash):
        return {
            "status": "success",
            "message": "Login successful"
        }
    else:
        return {
            "status": "error",
            "message": "Invalid credentials"
        }



=======
import bcrypt

users = {}

# Register Function (Hash Password)

def register(username, password):
    if username in users:
        return {
            "status": "error",
            "message": "User already exists"
        }

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed

    return {
        "status": "success",
        "message": "User registered successfully"
    }


# Login Function (Check Hashed Password)

def login(username, password):

    if username not in users:
        return {
            "status": "error",
            "message": "User not found"
        }

    stored_hash = users[username]

    if bcrypt.checkpw(password.encode(), stored_hash):
        return {
            "status": "success",
            "message": "Login successful"
        }
    else:
        return {
            "status": "error",
            "message": "Invalid credentials"
        }



>>>>>>> 22031014cf25f8636d0293228d2970b67ec231f8
