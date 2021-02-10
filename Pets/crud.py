from sqlalchemy.orm import Session

from fastapi import HTTPException

from sql_Pets import models, schemas


def list_pets_with_filter(db: Session, species: str = None):
    if species:
        return db.query(models.Pet).filter(models.Pet.species == species)
    else:
        return db.query(models.Pet).all()
    # Bug in return - not a valid List

def create_pet(db: Session, new_pet: schemas.PetCreate):
    pet_db = models.Pet(**new_pet.dict())
    # Same as pet_db = models.Pet(name=new_pet.name, species=new_pet.species)
    duplicate_pet = db.query(models.Pet).filter(models.Pet.name == pet_db.name, models.Pet.species == pet_db.species)
    if duplicate_pet.count() >= 1:
        raise HTTPException(status_code=422, detail="Pet's already in database.")
    elif (pet_db.name == "string" or pet_db.species == "string"):
        raise HTTPException(status_code=400, detail="Values cant be 'string'.")
    else:
        db.add(pet_db)
        db.commit()
        db.refresh(pet_db)
        return pet_db
        # Bug in returning de pet_db...
