from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from routes import init_routes
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/diploma_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Замените на случайный ключ

CORS(app, resources={r"/*": {"origins": "*"}})
jwt = JWTManager(app)

# Инициализация базы данных
db.init_app(app)

# Регистрация маршрутов
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
