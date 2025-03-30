from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes import init_routes

app = Flask(__name__)
CORS(app)  # Разрешаем CORS, если требуется

# Конфигурация подключения к базе данных (замени username и password на свои данные)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/diploma_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных
from models import db  # Импортируем объект db из models.py
db.init_app(app)

# Регистрация маршрутов
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
