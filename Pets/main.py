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


@app.get('/')
async def root():
    return {"message": "Hello World"}


# Route to list pet(s) with optional filter(name and species)
@app.get('/pets', response_model=List[schemas.Pet])
async def list_pets(name: str = None,
                    species: str = None,
                    db: Session = Depends(get_db)):
    if species and name:
        return crud.list_pets_with_filter(db, species, name)
    elif name:
        return crud.list_pets_with_filter(db, None, name)
        # Note the value None as parameter of the function...
        # It took me a lot of time to debbug it. The problem
        # is the function order of parameters(db, species, name)
        # If you use instead (db, name), the name will be consider
        # species... Found it by creating a test to raise an HTTPResponse
        # returning the name: {name}, but it was returning species: {species}
    elif species:
        return crud.list_pets_with_filter(db, species)
    else:
        return crud.list_pets_with_filter(db)


# Route to get a certain pet by it's ID
@app.get('/pets/{pet_id}')
async def get_pet(pet_id: int, db: Session = Depends(get_db)):
    pet_db = crud.get_pet(db, pet_id)
    if pet_db:
        return pet_db
    else:
        raise HTTPException(status_code=404, detail="Pet not found.")


# Route to create a new pet
@ app.post('/pets', response_model=schemas.Pet, status_code=201)
async def create_pet(new_pet: schemas.PetCreate,
                     db: Session = Depends(get_db)):
    return crud.create_pet(db, new_pet)


# Route to delete a certain pet by it's id
@app.delete('/pets/{pet_id}', status_code=204)
async def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    pet_db = crud.get_pet(db, pet_id)
    if pet_db:
        return crud.delete_pet(db, pet_id)
    else:
        raise HTTPException(status_code=404, detail="Pet not found.")
