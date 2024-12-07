from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.api.models.person import Person as PersonModel

#CREATE
async def create_person(db: Session, person):
    db_person = PersonModel(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


#GET
async def get_person(db: Session, person_id: int):
    person = db.query(PersonModel).filter(PersonModel.id == person_id).first()
    return person

async def read_all_person(skip: int, limit: int, db: Session):
    #list = db.query(PersonModel).offset(skip).limit(limit).all
    list = db.query(PersonModel).order_by(PersonModel.id).all()
    #list = db.query(PersonModel).all()
    return list

#UPDATE
async def update_data(db: Session, person_id: int, person_name: str, person_age: int):
    person = db.query(PersonModel).filter(PersonModel.id == person_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    
    person.name = person_name 
    person_age = person_age
    db.commit()
    db.refresh(person)
    return {"message": "Person's info updated successfully"}

#DELETE
async def delete_person(db: Session, person_id: int):
    person = db.query(PersonModel).filter(PersonModel.id == person_id).first()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    
    db.delete(person)
    db.commit()
    return {"message": "Person deleted successfully"}

    