from config import create_app, db

app = create_app()

# Registrar Blueprints
app.register_blueprint(aluno_bp, url_prefix='/api')
app.register_blueprint(professor_bp, url_prefix='/api')
app.register_blueprint(turma_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
