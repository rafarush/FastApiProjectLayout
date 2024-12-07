from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.schemas.person import Person
from app.api.crud.person import create_person, get_person, delete_person, read_all_person, update_data
from app.api.db.sessions import get_db

router = APIRouter()

#CREATE
@router.post("/persons/", response_model=Person)
async def create_new_person(person: Person, db: Session = Depends(get_db)):
    return await create_person(db=db, person=person)

#GET
@router.get("/persons/")
async def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    list = await read_all_person(skip, limit, db)
    return list

@router.get("/persons/{person_id}", response_model=Person)
async def get_person_by_id(person_id: int, db: Session = Depends(get_db)):
    person = await get_person(db, person_id)
    return person

#UPDATE
@router.put("/persons/{person_id}")
async def change_info(person_id: int,person_name: str, person_age: int,db: Session = Depends(get_db)):
    return await update_data(db, person_id, person_name, person_age)

#DELETE
@router.delete("/persons/{person_id}")
async def delete_person_id(person_id: int, db: Session = Depends(get_db)):
    return await delete_person(db, person_id)
