from fastapi import FastAPI,Depends,HTTPException
from database import SessionLocal,engine
from typing import Annotated, List
from sqlalchemy.orm import Session
import models
app= FastAPI()
models.Base.metadata.create_all(bind=engine)


async def get_db(): 
    db=SessionLocal()
    try: 
        yield db 
    finally : 
        db.close( )
        
db_dependency=Annotated[Session,Depends(get_db)]