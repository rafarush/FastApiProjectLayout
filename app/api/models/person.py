from sqlalchemy import Column, Integer, String
from app.api.db.base_class import Base


class Person(Base):
    __tablename__ = "person"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
