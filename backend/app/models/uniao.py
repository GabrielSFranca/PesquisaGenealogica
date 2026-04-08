from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database_connect import Base
from app.models.pessoa import Pessoa
    
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
    
    
    
# class Uniao(Base):
#     __tablename__ = 'unioes'
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
    