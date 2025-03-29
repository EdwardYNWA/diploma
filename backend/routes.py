from flask import Flask, request, jsonify
from test_data import TEST_QUESTIONS

def init_routes(app):
    @app.route('/test', methods=['GET'])
    def get_test():
        return jsonify(TEST_QUESTIONS)

    @app.route('/submit', methods=['POST'])
    def submit_test():
        data = request.json
        return jsonify({"message": "Ответы приняты", "data": data})

