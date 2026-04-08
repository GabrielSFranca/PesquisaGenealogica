from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship

# 1. A CONEXÃO COM O BANCO QUE VOCÊ CRIOU
# Lembre-se: Usamos a porta 5433 que descobrimos no terminal!
DATABASE_URI = 'postgresql+psycopg2://admin_acervo:projeto123@localhost:5433/acervo_veneto'

engine = create_engine(DATABASE_URI, echo=True) # echo=True mostra o que está acontecendo nos bastidores
Base = declarative_base()

# 2. AS TABELAS (MODELO GEDCOM)
class Source(Base):
    """Tabela que representa os 121 livros físicos de Nova Palma"""
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True)
    book_number = Column(Integer, nullable=False)
    page_number = Column(Integer, nullable=False)
    description = Column(Text)

class Person(Base):
    """Tabela dos imigrantes e descendentes"""
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    child_in_family_id = Column(Integer, ForeignKey('families.id'))

class Family(Base):
    """Tabela que une casais e cria o elo para os filhos"""
    __tablename__ = 'families'
    id = Column(Integer, primary_key=True)
    husband_id = Column(Integer, ForeignKey('people.id'))
    wife_id = Column(Integer, ForeignKey('people.id'))

# 3. O COMANDO QUE CRIA TUDO
if __name__ == "__main__":
    print("Conectando ao PostgreSQL e criando as tabelas...")
    Base.metadata.create_all(engine)
    print("Sucesso! O banco de dados está pronto para receber os registros.")