from sqlalchemy import Column, String, Integer

from sql_Pets.database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    species = Column(String(15), nullable=False)
