from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///desafio.db')

print('Conexão realizada com sucesso')

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    
    # Estabelece a relação entre Produto e Fornecedor
    fornecedor = relationship("Fornecedor")

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    with Session() as session:
        fornecedores = [
            Fornecedor(nome='VGR CONSULTING', telefone='15123456', email='teste@teste.com', endereco='Rua dos Sonhos'),
            Fornecedor(nome='TESTE', telefone='TESTE', email='TESTE', endereco='TESTE'),
            Fornecedor(nome='TESTE1', telefone='TESTE2', email='TESTE3', endereco='TESTE4'),
            Fornecedor(nome='TESTE2', telefone='TESTE2', email='TESTE2', endereco='TESTE2')
        ]

        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e:
    print(f'Erro ao inserir produtos: {e}')

try:
    with Session() as session:
        fornecedores = [
            Produto(nome='Produto1', descricao='Descricao produto 1', preco='Preco produto 1', fornecedor_id=1),
            Produto(nome='Produto2', descricao='Descricao produto 2', preco='Preco produto 2', fornecedor_id=2),
            Produto(nome='Produto3', descricao='Descricao produto 3', preco='Preco produto 3', fornecedor_id=3),
            Produto(nome='Produto4', descricao='Descricao produto 4', preco='Preco produto 4', fornecedor_id=4)
        ]

        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e:
    print(f'Erro ao inserir produtos: {e}')
