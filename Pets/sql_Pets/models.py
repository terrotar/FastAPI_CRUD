from sqlalchemy import Column, String, Integer

from database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, auto_increment=True)
    name = Column(String(30), nullable=False)
    species = Column(String(15), nullable=False)
