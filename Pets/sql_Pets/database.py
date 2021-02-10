from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Creation of database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///.sql_app.db"


# Creation of database conection
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})


# Creation of a local session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# sqlalchemy Base class to create classes
Base = declarative_base()
