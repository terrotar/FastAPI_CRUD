from sqlalchemy.orm import Session

from sql_Pets import models, schemas


def list_pets_with_filter(db: Session, species: str = None):
    if species:
        return db.query(models.Pet).filter(models.Pet.species == species)
    else:
        return db.query(models.Pet).first(50)
