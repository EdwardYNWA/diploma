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
        return jsonify(TEST_QUESTIONS)

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
