from fastapi import FastAPI
from models import Room
from router import users

app= FastAPI()

app.include_router(users.router,tags=['user'])
