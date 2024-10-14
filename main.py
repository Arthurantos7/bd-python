import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados. 
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela.

Base = declarative_base()

class Aluno(Base): 
    __tablename__ = "alunos"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

def solicitar_dados():
    # CRUD.
    # Create - Insert - Salvar.
    os.system("cls || clear")
    print("Solicitando dados para o usúario. ")
    inserir_nome = input("Digite seu nome: ")
    inserir_email = input("Digite seu e-mail: ")
    inserir_senha = input("Digite sua senha: ")

    aluno = Aluno(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
    session.add(aluno)
    session.commit()

def exibir_dados_dos_alunos():
    # Read - Select - Consulta
    print("\nExibindo dados de todos os alunos. ")
    lista_alunos = session.query(aluno).all()

    for aluno in lista_alunos:
        print(f"{aluno.id} - {aluno.nome} - {aluno.email} - {aluno.senha}")

def atualizar_dados():
    # U - Update - UPDATE - Atualizar
    print("\nAtualizando dados do usuário.")
    email_aluno = input("Digite o e-mail do aluno que será atualizado: ") 

    aluno = session.query(aluno).filter_by(email = email_aluno).first()

    if aluno:
        aluno.nome = input("Digite seu nome: ")
        aluno.email = input("Digite seu e-mail: ")
        aluno.senha = input("Digite sua senha: ")

        session.commit()
    else: 
        print("aluno não encontrado.")

def exibir_dados_dos_alunos2():
    # R - Read - SELECT -Consulta
    print("\nExibindo dados de todos os alunos. ")
    lista_alunos = session.query(aluno).all()

    for aluno in lista_alunos:
        print(f"{aluno.id} - {aluno.nome} - {aluno.email} - {aluno.senha}")

def excluir_dados():
    # D - Delete - DELETE - Excluir 
    print("\nExcluindo os dados de um aluno. ")
    email_aluno = input("Digite o e-mail do aluno que será excluído: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        session.delete(aluno)
        session.commit()
        print(f"Aluno {aluno.nome} excluido com sucesso!")
    else:
        print("Aluno não encontrado.")

def exibir_dados_dos_alunos3():
    # R - Read - SELECT - Consulta
    print("\nExibindo dados de todos os alunos. ")
    lista_alunos = session.query(Aluno).all()

    for aluno in lista_alunos:
        print(f"{aluno.id} - {aluno.nome} - {aluno.email} - {aluno.senha}")

def consultar_dados_um_aluno():
    # R - Read - SELECT - Consulta
    print("\nConsultando os dados de apenas um aluno. ")
    email_aluno = input("Digite o e-mail do aluno:  ")

    aluno = session.query(aluno).filter_by(email = email_aluno).first()

    if aluno:
        print(f"{aluno.id} - {aluno.nome} - {aluno.email} - {aluno.senha}")
    else:
        print("Aluno não encontrado.")

# Fechando conexão.
session.close()