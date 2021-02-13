from sqlalchemy.orm import Session

from fastapi import HTTPException

from sql_Pets import models, schemas


# Funcion to list pets with "species" or not
def list_pets_with_filter(db: Session, species: str = None, name: str = None):
    if species and name:
        species_name_filter = db.query(models.Pet).filter(models.Pet.name == name, models.Pet.species == species).all()
        results = []
        for animal in species_name_filter:
            animal = {
                      "name": animal.name,
                      "species": animal.species,
                      "id": animal.id
                     }
            results.append(animal)
        if len(results) >= 1:
            return results
        else:
            raise HTTPException(status_code=422,
                                detail=f"Pet(s) with name({name}) and species({species}) not found.")
    elif name:
        name_filter = db.query(models.Pet).filter(models.Pet.name == name).all()
        results = []
        for animal in name_filter:
            animal = {
                      "name": animal.name,
                      "species": animal.species,
                      "id": animal.id
                     }
            results.append(animal)
        if len(results) >= 1:
            return results
        else:
            raise HTTPException(status_code=422,
                                detail=f"Pet(s) with name({name}) not found.")
    elif species:
        species_filter = db.query(models.Pet).filter(models.Pet.species == species).all()
        results = []
        for animal in species_filter:
            animal = {
                      "name": animal.name,
                      "species": animal.species,
                      "id": animal.id
                     }
            results.append(animal)
        if len(results) >= 1:
            return results
        else:
            raise HTTPException(status_code=422,
                                detail=f"Pet(s) with species({species}) not found.")
    else:
        no_filter = db.query(models.Pet).all()
        results = []
        for animal in no_filter:
            animal = {
                      "name": animal.name,
                      "species": animal.species,
                      "id": animal.id
                     }
            results.append(animal)
        if len(results) >= 1:
            return results
        else:
            raise HTTPException(status_code=422,
                                detail="No pet(s) found.")
        return results


# Function to create a new_pet
def create_pet(db: Session, new_pet: schemas.PetCreate):
    pet_db = models.Pet(**new_pet.dict())
    # Same as pet_db = models.Pet(name=new_pet.name, species=new_pet.species)
    duplicate_pet = db.query(models.Pet).filter(
        models.Pet.name == pet_db.name, models.Pet.species == pet_db.species)
    if duplicate_pet.count() >= 1:
        raise HTTPException(status_code=422, detail="Pet's already in database.")
    elif (pet_db.name == "string" or pet_db.species == "string"):
        raise HTTPException(status_code=400, detail="Values cant be 'string'.")
    else:
        db.add(pet_db)
        db.commit()
        db.refresh(pet_db)
        return {
                "name": pet_db.name,
                "species": pet_db.species,
                "id": pet_db.id
               }


# Function get a pet by pet_id
def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).get(pet_id)
    # Another solution db.query(models.Pet).filter(models.Pet.id == pet_id).first()


# Function to delete a pet by pet_id
def delete_pet(db: Session, pet_id: int):
    db.query(models.Pet).filter(models.Pet.id == pet_id).delete()
    db.commit()
    return {"message": f"Pet {pet_id} deleted."}


# Function to update a pet name and/or species by pet_id
def update_pet(db: Session, pet_id: int, name: str, species: str):
    pet_changed = db.query(models.Pet).get(pet_id)
    if name and species:
        pet_changed.name = name
        pet_changed.species = species
        db.commit()
        db.refresh(pet_changed)
        return get_pet(db, pet_id)
    elif name:
        pet_changed.name = name
        db.commit()
        db.refresh(pet_changed)
        return get_pet(db, pet_id)
    elif species:
        pet_changed.species = species
        db.commit()
        db.refresh(pet_changed)
        return get_pet(db, pet_id)
    else:
        raise HTTPException(status_code=422, detail=f"Pet({pet_id}) not found.")
