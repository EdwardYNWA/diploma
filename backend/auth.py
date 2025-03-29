from flask import request, jsonify

users = {"student@example.com": "password123"}

def login():
    data = request.json
    if users.get(data["email"]) == data["password"]:
        return jsonify({"message": "Успешный вход"})
    return jsonify({"error": "Неверные данные"}), 401

