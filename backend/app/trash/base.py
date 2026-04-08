from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Text
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

class EventTag(enum.Enum):
    BIRT = "Birth"
    CHR = "Christening"
    DEAT = "Death"
    MARR = "Marriage"
    DIV = "Divorce"
    IMMI = "Immigration"

class Pessoa(Base):
    __tablename__ = 'pessoas'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100))
    genero = Column(String(1)) # M / F
    
    # FK para a união de onde a pessoa nasceu
    pais_id = Column(Integer, ForeignKey('unioes.id'), nullable=True)
    
    # Relacionamentos
    eventos = relationship("Evento", back_populates="pessoa")
    familia_origem = relationship("Uniao", foreign_keys=[pais_id])

class Uniao(Base):
    __tablename__ = 'unioes'
    
    id = Column(Integer, primary_key=True)
    pai_id = Column(Integer, ForeignKey('pessoas.id'))
    mae_id = Column(Integer, ForeignKey('pessoas.id'))
    
    # Relacionamentos
    pai = relationship("Pessoa", foreign_keys=[pai_id])
    mae = relationship("Pessoa", foreign_keys=[mae_id])
    filhos = relationship("Pessoa", foreign_keys=[Pessoa.pais_id])
    eventos = relationship("Evento", back_populates="uniao")

class Evento(Base):
    __tablename__ = 'eventos'
    
    id = Column(Integer, primary_key=True)
    tag = Column(Enum(EventTag), nullable=False)
    data = Column(String(50)) # String para aceitar datas imprecisas (ex: "Circa 1890")
    local = Column(String(200))
    descricao = Column(Text)
    
    # Chaves Estrangeiras Polimórficas
    pers_id = Column(Integer, ForeignKey('pessoas.id'), nullable=True)
    union_id = Column(Integer, ForeignKey('unioes.id'), nullable=True)
    
    # Back-populates
    pessoa = relationship("Pessoa", back_populates="eventos")
    uniao = relationship("Uniao", back_populates="eventos")
    
    
    

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.exc import OperationalError

# # 1. Defina a string de conexão
# DATABASE_URI = 'postgresql+psycopg2://postgres:suasenha@localhost:5432/genealogia_db'

# # 2. Crie a "Engine" (o motor que gerencia as conexões)
# # echo=True faz com que o SQLAlchemy imprima o SQL gerado no console (ótimo para debug)
# engine = create_engine(DATABASE_URI, echo=False)

# # 3. Crie a fábrica de Sessões
# # A sessão é o que você usará para inserir, buscar e deletar dados
# Session = sessionmaker(bind=engine)

# def testar_conexao():
#     """Função simples para testar se o banco está respondendo."""
#     try:
#         # Tenta conectar ao banco de dados
#         with engine.connect() as connection:
#             print("Conexão com o PostgreSQL estabelecida com sucesso!")
#             return True
#     except OperationalError as e:
#         print(f"Erro ao conectar ao banco de dados: {e}")
#         return False

# # Executa o teste
# if __name__ == '__main__':
#     if testar_conexao():
#         # Aqui você instanciaria a sessão para começar a usar
#         session = Session()
#         # session.add(novo_registro) ...