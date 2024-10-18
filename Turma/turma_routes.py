from flask import Blueprint, request, jsonify
from turma.turmas_model import Turma
from config import db

turma_bp = Blueprint('turma', __name__)

@turma_bp.route('/turmas', methods=['GET'])
def listar_turmas():
    turmas = Turma.query.all()
    return jsonify([turma.to_dict() for turma in turmas])

@turma_bp.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    turma = Turma.query.get_or_404(id)
    return jsonify(turma.to_dict())

@turma_bp.route('/turmas', methods=['POST'])
def adicionar_turma():
    dados = request.get_json()
    nova_turma = Turma(
        descricao=dados['descricao'],
        professor_id=dados['professor_id'],
        ativo=dados.get('ativo', True)
    )
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify(nova_turma.to_dict()), 201

@turma_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    turma = Turma.query.get_or_404(id)
    dados = request.get_json()
    turma.descricao = dados['descricao']
    turma.professor_id = dados['professor_id']
    turma.ativo = dados.get('ativo', True)
    db.session.commit()
    return jsonify(turma.to_dict())

@turma_bp.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    turma = Turma.query.get_or_404(id)
    db.session.delete(turma)
    db.session.commit()
    return jsonify({'message': 'Turma deletada'}), 204
