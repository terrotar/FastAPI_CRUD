from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


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


PETS_LIST = [
    {"id": 1, "name": "Jamall", "species": "Cat"},
    {"id": 2, "name": "Luna", "species": "Cat"},
    {"id": 3, "name": "Faruke", "species": "Dog"},
    {"id": 4, "name": "Minnie", "species": "Dog"}
]
ID_COUNTER = 5


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/pets', response_model=List[PetBase])
async def list_pets(species: str = None):
    if species:
        return [pet for pet in PETS_LIST if pet["species"] == species]
        # Another possibility using lambda...
        # return list(filter(lambda p: p['species'] == species, PETS_LIST))
    return PETS_LIST


@app.get('/pets/{pet_id}')
async def get_pet(pet_id: int):
    for pet in PETS_LIST:
        if pet["id"] == pet_id:
            return pet
    else:
        raise HTTPException(status_code=404, detail="Pet not found.")


@ app.post('/pets', response_model=Pet)
async def create_pet(new_pet: PetCreate):
    global ID_COUNTER
    new_pet = new_pet.dict()
    for animal in PETS_LIST:
        if (new_pet["name"] == animal["name"]):
            if (new_pet["species"] == animal["species"]):
                raise HTTPException(status_code=422, detail="Pet's already in database.")
    else:
        new_pet["id"] = ID_COUNTER
        ID_COUNTER += 1
        PETS_LIST.append(new_pet)
        return new_pet