from config import db
from datetime import datetime

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    id_turma = db.Column(db.String(20))  # Alterado para 'id_turma'
    data_nascimento = db.Column(db.Date)  # Agora como 'Date'
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float)

    def __init__(self, nome, idade, id_turma, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        self.nome = nome
        self.idade = idade
        self.id_turma = id_turma  # Alterado para 'id_turma'
        self.data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()  # Formato dd/mm/yyyy
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = self.calcular_media_final()  # Calcula a média final

    def calcular_media_final(self):
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'id_turma': self.id_turma,  # Alterado para 'id_turma'
            'data_nascimento': self.data_nascimento.strftime('%d/%m/%Y'),  # Converte para string
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self.media_final
        }

class AlunoNaoExiste(Exception):  # Alterado para 'AlunoNaoExiste'
    pass

def obter_aluno_por_id(aluno_id):  # Alterado para 'obter_aluno_por_id'
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        raise AlunoNaoExiste
    return aluno.to_dict()

def listar_todos_alunos():  # Alterado para 'listar_todos_alunos'
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def inserir_aluno(aluno_data):  # Alterado para 'inserir_aluno'
    # Validação das notas
    if aluno_data['nota_primeiro_semestre'] < 0 or aluno_data['nota_primeiro_semestre'] > 10:
        raise ValueError('Nota do primeiro semestre deve estar entre 0 e 10.')
    if aluno_data['nota_segundo_semestre'] < 0 or aluno_data['nota_segundo_semestre'] > 10:
        raise ValueError('Nota do segundo semestre deve estar entre 0 e 10.')

    novo_aluno = Aluno(
        nome=aluno_data['nome'],
        idade=aluno_data['idade'],
        id_turma=aluno_data['id_turma'],  # Alterado para 'id_turma'
        data_nascimento=aluno_data['data_nascimento'],
        nota_primeiro_semestre=aluno_data['nota_primeiro_semestre'],
        nota_segundo_semestre=aluno_data['nota_segundo_semestre']
    )
    db.session.add(novo_aluno)
    db.session.commit()

def modificar_aluno(aluno_id, novos_dados):  # Alterado para 'modificar_aluno'
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        raise AlunoNaoExiste

    aluno.nome = novos_dados['nome']
    aluno.idade = novos_dados['idade']
    aluno.id_turma = novos_dados['id_turma']  # Alterado para 'id_turma'
    aluno.data_nascimento = datetime.strptime(novos_dados['data_nascimento'], '%d/%m/%Y').date()
    aluno.nota_primeiro_semestre = novos_dados['nota_primeiro_semestre']
    aluno.nota_segundo_semestre = novos_dados['nota_segundo_semestre']
    aluno.media_final = aluno.calcular_media_final()  # Recalcula a média final
    db.session.commit()

def remover_aluno(aluno_id):  # Alterado para 'remover_aluno'
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        raise AlunoNaoExiste
    db.session.delete(aluno)
    db.session.commit()
