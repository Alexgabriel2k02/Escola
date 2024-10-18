import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicialização da base de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['HOST'] = '0.0.0.0'
    app.config['PORT'] = 8000
    app.config['DEBUG'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados com a aplicação
    db.init_app(app)

    return app
