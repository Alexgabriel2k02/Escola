from flask import Flask
from config import db
from aluno.alunos_routes import aluno_bp
from professor.professor_routes import professor_bp
from turma.turmas_routes import turma_bp

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Registrando os blueprints
app.register_blueprint(aluno_bp, url_prefix='/api')
app.register_blueprint(professor_bp, url_prefix='/api')
app.register_blueprint(turma_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
