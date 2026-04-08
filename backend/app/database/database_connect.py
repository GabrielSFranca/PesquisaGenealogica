from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

DB_URI = os.getenv("DATABASE_URI")

# from sqlalchemy.exc import OperationalError
# DATABASE_URI="SQLITE"

engine = create_engine(DB_URI)

Session = sessionmaker(bind=engine, echo=True)

Base = declarative_base()

