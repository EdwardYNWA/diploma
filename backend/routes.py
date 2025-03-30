from flask import request, jsonify
from test_data import TEST_QUESTIONS
from auth import login, register
from utils import classify_student

def init_routes(app):
    @app.route('/')
    def home():
        return "Приложение работает!"

    @app.route('/test', methods=['GET'])
    def get_test():
        return jsonify(TEST_QUESTIONS), 200

    @app.route('/submit', methods=['POST'])
    def submit_test():
        data = request.json
        # Предположим, что в data приходит ключ "score"
        score = data.get("score", 0)
        level = classify_student(score)
        return jsonify({"message": "Ответы приняты", "score": score, "level": level})

    @app.route('/login', methods=['POST'])
    def login_route():
        return login()

    @app.route('/register', methods=['POST'])
    def register_route():
        return register()

    @app.route('/recommendations', methods=['POST'])
    def generate_recommendations():
    data = request.json
    student_id = data['student_id']
    student = Student.query.get(student_id)
    competence_level = student.competence_level
    
    # Сопоставьте уровень компетенций с учебными материалами
    materials = Material.query.filter_by(competence_level=competence_level).all()
    
    return jsonify([{"title": m.title, "description": m.description} for m in materials])
