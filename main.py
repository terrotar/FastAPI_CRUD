from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class PET(BaseModel):
    id: int
    name: str
    species: str


PETS_LIST = [
    {"id": 1, "name": "Jamall", "species": "Cat"},
    {"id": 2, "name": "Luna", "species": "Cat"},
    {"id": 3, "name": "Faruke", "species": "Dog"},
    {"id": 4, "name": "Minnie", "species": "Dog"}
]


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/pets', response_model=List[PET])
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
