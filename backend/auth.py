from flask import request, jsonify

# Простое хранилище пользователей для примера
users = {
    "student@example.com": "password123"
}

def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    if email in users and users[email] == password:
        return jsonify({"message": "Успешный вход"}), 200
    return jsonify({"error": "Неверные данные"}), 401

def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")
    if email in users:
        return jsonify({"error": "Пользователь уже существует"}), 400
    # В данном примере просто добавляем в словарь.
    users[email] = password
    return jsonify({"message": "Регистрация успешна"}), 201
