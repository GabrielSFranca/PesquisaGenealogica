from app.database.database_connect import Base, engine
# importa modelos
from app.models.pessoa import Pessoa
from app.models.uniao import Uniao
from app.models.evento import EventTag, Evento

def db_init():
    Base.metadata.create_all(bind=engine)
    
if __name__ == "__main__":
    db_init()
    print('banco criado com sucesso')