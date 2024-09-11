##  Create a new app for Users.
from fastapi import FastAPI
from pydantic import BaseModel
## Base model es 

app = FastAPI()
##  Se inicia el servidor: uvicorn users:app --reload.

class User(BaseModel):
    id: int
    firstName: str
    lastName: str
    Url: str
    age: int

usersDATA = [User(id = 1 , firstName = "John" , lastName = "Perez" , Url = "google.com" , age = 23),
            User( id = 2 , firstName = "Carlos" , lastName = "Perez" , Url = "facebook.com" , age = 23),
            User( id = 3 , firstName = "Mejia" , lastName = "Perez" , Url = "instagram.com" , age = 54)]


@app.get("/usersjson")
async def users():
    return [{"first_name": "John", "last_name": "Perez" , "url": "google.com" , "age": 23},
            {"first_name": "Carlos", "last_name": "Valencia" , "url": "instagram.com" , "age": 23},
            {"first_name": "Samuel", "last_name": "Mejia" , "url": "youtube.com" , "age": 23},
            {"first_name": "Jhon Alex", "last_name": "Otoño" , "url": "facebook.com" , "age": 23}]

@app.get("/user")
async def usersclass():
    return usersDATA


@app.get("/userquery/")
async def userId(id: int):
    try:
        filter_id = filter(lambda user: user.id == id, usersDATA)
        return list(filter_id)[0]
    except:
        return {"Error, Usuario no existente!"}
