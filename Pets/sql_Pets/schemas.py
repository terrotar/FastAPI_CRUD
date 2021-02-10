from pydantic import BaseModel


# Public attributes
class PetBase(BaseModel):
    name: str
    species: str


# Required attributes to create an instance
class PetCreate(PetBase):
    pass


# Private attributes of an object Pet()
class Pet(PetBase):
    id: int

    class Config:
        orm_mode: True
