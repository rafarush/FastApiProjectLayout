from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.schemas.person import Person
from app.api.crud.person import create_person, get_person, delete_person
from app.api.db.sessions import get_db

router = APIRouter()

@router.post("/persons/", response_model=Person)
async def create_new_person(person: Person, db: Session = Depends(get_db)):
    return await create_person(db=db, person=person)

@router.get("/persons/{person_id}", response_model=Person)
async def get_person_by_id(person_id: int, db: Session = Depends(get_db)):
    person = await get_person(db, person_id)
    return person


@router.delete("/persons/{person_id}")
async def delete_person_id(person_id: int, db: Session = Depends(get_db)):
    return await delete_person(db, person_id)
