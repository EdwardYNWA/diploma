from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"error": "Поля email и password обязательны"}), 400
        
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Пользователь с таким email уже существует"}), 400
        
    new_user = User(email=email, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Пользователь создан"}), 201

def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Неправильный email или пароль"}), 401
        
    return jsonify({"message": "Успешный вход"}), 200
