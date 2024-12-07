from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.api.models.person import Person as PersonModel

async def create_person(db: Session, person):
    db_person = PersonModel(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

async def get_person(db: Session, person_id: int):
    person = db.query(PersonModel).filter(PersonModel.id == person_id).first()
    return person

async def delete_person(db: Session, person_id: int):
    person = db.query(PersonModel).filter(PersonModel.id == person_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    
    db.delete(person)
    db.commit()
    return {"message": "Person deleted successfully"}