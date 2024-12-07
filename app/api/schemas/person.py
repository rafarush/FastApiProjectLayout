from typing import Optional
from pydantic import BaseModel

class Person(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True 
