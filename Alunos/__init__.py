# aluno/__init__.py
from flask import Blueprint

aluno_bp = Blueprint('aluno', __name__)

# Aqui você pode importar as rotas, se necessário
from .alunos_routes import *
