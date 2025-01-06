from flask import request, jsonify
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    return username, password