from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes import init_routes

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Разрешаем CORS для всех маршрутов

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/diploma_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Отключение CSRF-защиты (если необходимо)
app.config['WTF_CSRF_ENABLED'] = False

# Инициализация базы данных
from models import db  # Импортируем объект db из models.py
db.init_app(app)

# Регистрация маршрутов
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
