from flask import Blueprint, request, jsonify
from professor.professor_model import Professor
from config import db

professor_bp = Blueprint('professor', __name__)

@professor_bp.route('/professores', methods=['GET'])
def listar_professores():
    professores = Professor.query.all()
    return jsonify([prof.to_dict() for prof in professores])

@professor_bp.route('/professores/<int:id>', methods=['GET'])
def obter_professor(id):
    professor = Professor.query.get_or_404(id)
    return jsonify(professor.to_dict())

@professor_bp.route('/professores', methods=['POST'])
def adicionar_professor():
    dados = request.get_json()
    novo_professor = Professor(
        nome=dados['nome'],
        idade=dados['idade'],
        materia=dados['materia'],
        observacoes=dados.get('observacoes')
    )
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify(novo_professor.to_dict()), 201

@professor_bp.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    professor = Professor.query.get_or_404(id)
    dados = request.get_json()
    professor.nome = dados['nome']
    professor.idade = dados['idade']
    professor.materia = dados['materia']
    professor.observacoes = dados.get('observacoes')
    db.session.commit()
    return jsonify(professor.to_dict())

@professor_bp.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    professor = Professor.query.get_or_404(id)
    db.session.delete(professor)
    db.session.commit()
    return jsonify({'message': 'Professor deletado'}), 204
