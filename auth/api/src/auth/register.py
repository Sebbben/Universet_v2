from flask import request
import requestDefs
from db import getDB
import bcrypt
import re


def is_password_strong(password):
    """
    A strong password:
    - At least 9 characters
    - Contains uppercase and lowercase letters
    - Contains digits
    - Contains special characters
    """

    if len(password) < 9:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def register():
    if request.method != "POST": return requestDefs.method_not_allowed()
    json = request.get_json()
    
    if not json: return requestDefs.bad_request("Request body must be JSON")

    required_fields = ["username", "password", "confirmPassword", "terms"]
    for field in required_fields:
        if field not in json:
            return requestDefs.bad_request(f"Missing required field: {field}")

    if json["password"] != json["confirmPassword"]:
        return requestDefs.bad_request("Passwords do not match")

    if not json["terms"]:     
        return requestDefs.bad_request("You must accept the terms and conditions")
    
    if not is_password_strong(json["password"]):
        return requestDefs.bad_request("Password is not strong enough")

    with getDB().connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE username = %s", (json["username"],))
            if cur.fetchone():
                return requestDefs.conflict("Username already exists")
            
            hashed_password = bcrypt.hashpw(json["password"].encode(), bcrypt.gensalt())
            cur.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (json["username"], hashed_password))
            conn.commit()

    return "Register"