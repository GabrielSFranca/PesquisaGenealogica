from sqlalchemy import Column, Integer, String
from app.database.database_connect import Base
import enum

class EventTag(enum.Enum):
    BIRT = "Birth"
    CHR = "Christening"
    DEAT = "Death"
    MARR = "Marriage"
    DIV = "Divorce"
    IMMI = "Immigration"

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