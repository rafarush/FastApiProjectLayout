from fastapi import FastAPI
from app.api.controllers import person

app = FastAPI()

app.include_router(person.router)

@app.get("/")
async def root():
    return {"Hello" : "World"}
