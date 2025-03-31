from flask import request, jsonify, g
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Student, Material, Question, TestResult, Recommendation

def init_routes(app):
    # Базовые маршруты
    @app.route('/')
    def home():
        return "Приложение работает!"

    # Административная панель
    @app.route('/admin', methods=['GET'])
    @jwt_required()
    def admin_panel():
        if not User.query.get(g.user_id).is_admin:
            return jsonify({"error": "Доступ запрещен"}), 403
        return jsonify({"message": "Добро пожаловать в админку"}), 200

    # Управление материалами
    @app.route('/admin/materials', methods=['GET', 'POST'])
    @jwt_required()
    def manage_materials():
        if not User.query.get(g.user_id).is_admin:
            return jsonify({"error": "Доступ запрещен"}), 403
            
        if request.method == 'GET':
            materials = Material.query.all()
            return jsonify([{"id": m.id, "title": m.title, "level": m.competence_level} for m in materials])
            
        elif request.method == 'POST':
            data = request.json
            new_material = Material(
                title=data['title'],
                description=data['description'],
                competence_level=data['level']
            )
            db.session.add(new_material)
            db.session.commit()
            return jsonify({"message": "Материал добавлен"}), 201

    # Управление вопросами
    @app.route('/admin/questions', methods=['GET', 'POST'])
    @jwt_required()
    def manage_questions():
        if not User.query.get(g.user_id).is_admin:
            return jsonify({"error": "Доступ запрещен"}), 403
            
        if request.method == 'GET':
            questions = Question.query.all()
            return jsonify([{"id": q.id, "text": q.text, "options": q.options} for q in questions])
            
        elif request.method == 'POST':
            data = request.json
            new_question = Question(
                text=data['text'],
                options=data['options'],
                correct_answer=data['correct']
            )
            db.session.add(new_question)
            db.session.commit()
            return jsonify({"message": "Вопрос добавлен"}), 201

    # Регистрация и вход
    @app.route('/register', methods=['POST'])
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

    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        email = data.get("email")
        password = data.get("password")
        
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"error": "Неправильный email или пароль"}), 401
            
        return jsonify({"token": "ваш_токен"}), 200  # Реализуйте JWT здесь

    # Остальные маршруты (исправлены)
    @app.route('/test', methods=['GET'])
    def get_test():
        questions = Question.query.all()
        return jsonify([{"text": q.text, "options": q.options} for q in questions]), 200

    @app.route('/submit', methods=['POST'])
    def submit_test():
        data = request.json
        score = data.get("score", 0)
        level = classify_student(score)
        
        # Сохраняем результат
        student = Student(name=data['name'], email=data['email'], competence_level=level)
        db.session.add(student)
        db.session.commit()
        
        return jsonify({"message": "Ответы приняты", "score": score, "level": level}), 200

    @app.route('/recommendations', methods=['POST'])
    def generate_recommendations():
        data = request.json
        student_id = data['student_id']
        student = Student.query.get(student_id)
        competence_level = student.competence_level
        
        materials = Material.query.filter_by(competence_level=competence_level).all()
        recommendations = []
        
        for material in materials:
            recommendation = Recommendation(
                student_id=student_id,
                material_id=material.id
            )
            db.session.add(recommendation)
            recommendations.append({
                "title": material.title,
                "description": material.description
            })
            
        db.session.commit()
        return jsonify(recommendations), 200
