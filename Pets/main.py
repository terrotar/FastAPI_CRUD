from typing import List

from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session

from sql_Pets import models, schemas
from sql_Pets.database import engine, SessionLocal
import crud


# Integrate and use all the other parts we created before.
models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Injection of function to get database for query
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@app.get('/pets', response_model=List[schemas.Pet])
async def list_pets(species: str = None, db: Session = Depends(get_db)):
    # Possibilities without a database
    # return [pet for pet in PETS_LIST if pet["species"] == species]
    # Another possibility using lambda...
    # return list(filter(lambda p: p['species'] == species, PETS_LIST))
    return crud.list_pets_with_filter(db, species)


@app.get('/pets/{pet_id}')
async def get_pet(pet_id: int):
    for pet in PETS_LIST:
        if pet["id"] == pet_id:
            return pet
    else:
        raise HTTPException(status_code=404, detail="Pet not found.")


@ app.post('/pets', response_model=schemas.Pet)
async def create_pet(new_pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return crud.create_pet(db, new_pet)
