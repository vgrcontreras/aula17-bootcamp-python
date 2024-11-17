from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

# Supondo que engine já foi definido anteriormente e os modelos Produto e Fornecedor foram definidos conforme o exemplo anterior.
from desafio import Fornecedor, Produto

engine = create_engine('sqlite:///desafio.db')

Session = sessionmaker(bind=engine)
session = Session()

resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto, Fornecedor.id == Produto.fornecedor_id
).group_by(Fornecedor.nome).all()

for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")