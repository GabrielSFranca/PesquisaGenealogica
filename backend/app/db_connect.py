from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
# lib psycopg2

# postgresql+psycopg2://<usuario>:<senha>@<host>:<porta>/<nome_do_banco>

# usuario / senha: Suas credenciais do Postgres.
# host: localhost (se o banco estiver na sua máquina) ou o IP do servidor.
# porta: O padrão do Postgres é 5432.
# nome_do_banco: O nome do banco de dados que você criou (ex: genealogia_db).

# defininso a str de conexao com o db;
# Trocando o 5432 pela sua porta real (ex: 5433)
DATABASE_URI = "postgresql+psycopg2://adm:123456@localhost:5435/acervo"

# criando a engine/motor que gerancia conexoes
# echo=True faz com que o SQLAlchemy imprima o SQL gerado no console (ótimo para debug)
engine=create_engine(DATABASE_URI, echo=False)

# sessao
Session=sessionmaker(bind=engine)

# testa se o banco esta respondendo
def try_connection():
    try:
        with engine.connect() as connection:
            print("Conexao c o psql estabelecida c sucesso")
            return True
    except OperationalError as e:
        print(f"Erro ao conectar ao db {e}")
        return False

# executa o teste
if __name__ == "__main__":
    if try_connection():
        # inicia sessao
        session=Session()
            

