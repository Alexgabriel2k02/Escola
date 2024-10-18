from flask import Blueprint, request, jsonify
from aluno.alunos_model import Aluno
from config import db

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos])

@aluno_bp.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    return jsonify(aluno.to_dict())

@aluno_bp.route('/alunos', methods=['POST'])
def adicionar_aluno():
    dados = request.get_json()
    novo_aluno = Aluno(
        nome=dados['nome'],
        idade=dados['idade'],
        data_nascimento=dados['data_nascimento'],
        nota_primeiro_semestre=dados.get('nota_primeiro_semestre'),
        nota_segundo_semestre=dados.get('nota_segundo_semestre'),
        media_final=dados.get('media_final'),
        turma_id=dados['turma_id']
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify(novo_aluno.to_dict()), 201

@aluno_bp.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    dados = request.get_json()
    aluno.nome = dados['nome']
    aluno.idade = dados['idade']
    aluno.data_nascimento = dados['data_nascimento']
    aluno.nota_primeiro_semestre = dados.get('nota_primeiro_semestre')
    aluno.nota_segundo_semestre = dados.get('nota_segundo_semestre')
    aluno.media_final = dados.get('media_final')
    aluno.turma_id = dados['turma_id']
    db.session.commit()
    return jsonify(aluno.to_dict())

@aluno_bp.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno deletado'}), 204
