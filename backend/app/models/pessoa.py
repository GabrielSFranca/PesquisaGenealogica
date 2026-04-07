from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import declarative_base

##
engine=create_engine()
Base=declarative_base()


class Pessoa(Base):
    __tablename__ = "pessoas"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100))
