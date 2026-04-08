from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database_connect import Base
import enum

class Gender(enum.Enum):
    M = "masculino"
    F = "feminino"
class Pessoa(Base):
    __tablename__ = 'pessoas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100), nullable=True)
    genero = Column(Enum(Gender), nullable=True)
    
    # FK para a união de onde a pessoa nasceu
    pais_id = Column(Integer, ForeignKey('unioes.id'), nullable=True)
    
    # Relacionamentos
    eventos = relationship("Evento", back_populates="pessoa")
    familia_origem = relationship("Uniao", foreign_keys=[pais_id])
    
    # facilita consultas
    # Eventos únicos de pessoa:
    # Nascimento
    # Batismo
    # Falecimento
    
    




# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, sessionmaker

# # 1. Configuração da Conexão
# DATABASE_URI = 'postgresql+psycopg2://admin_acervo:sua_senha_aqui@localhost:5432/acervo_veneto'
# engine = create_engine(DATABASE_URI)
# Base = declarative_base()

# # 2. Definição dos Modelos (Baseado no GEDCOM)
# class Source(Base):
#     __tablename__ = 'sources'
#     id = Column(Integer, primary_key=True)
#     book_number = Column(Integer, nullable=False) # Livro (1-121)
#     page_number = Column(Integer, nullable=False) # Página
#     description = Column(Text)

# class Person(Base):
#     __tablename__ = 'people'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     child_in_family_id = Column(Integer, ForeignKey('families.id'))

# class Family(Base):
#     __tablename__ = 'families'
#     id = Column(Integer, primary_key=True)
#     husband_id = Column(Integer, ForeignKey('people.id'))
#     wife_id = Column(Integer, ForeignKey('people.id'))

# # 3. Comando Mágico: Cria as tabelas no Postgres automaticamente
# def init_db():
#     Base.metadata.create_all(engine)
#     print("Tabelas criadas com sucesso no PostgreSQL!")

# if __name__ == "__main__":
#     init_db()