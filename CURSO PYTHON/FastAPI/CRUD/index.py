from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import requests
app = FastAPI()

# Configurar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    url: str
    age: int

users_data: List[User] = []

@app.post("/")
async def create_user(user: User):
    users_data.append(user)
    return user

@app.get("/users")
async def get_users():
    return users_data

@app.get("/Products")
async def get_products():
    return "products_data"