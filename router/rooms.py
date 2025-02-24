from fastapi import HTTPException , Depends ,status,APIRouter 
from sqlalchemy.orm import Session
from schemas import rooms  as schemas
from models import Room as models
from fastapi.encoders import jsonable_encoder
from dependencies import get_db


router = APIRouter()


@router.post('/room/')
def create_room(room:schemas.RoomCreate,db: Session=Depends(get_db)):
    db_room= db.query(models.Room).filter(models.Room.Dormitory== room.Dormitory).first()
    if db_room: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Room is exist ')
    
    db.add(room)
    db.commit()
    db.refresh(room)
    return room


@router.get('/room/{room_id}',response_model=schemas.RoomShow)
def read_room(room_id:int , db: Session=Depends(get_db)): 
    db_room =db.query(models.Room).filter(models.room.id== room_id)
    if db_room is None : 
        raise HTTPException (status_code=404 , detail= ' room not found ')
    return db_room

@router.put('/room/{room_id}')
def UpdateRoom(room:schemas.RoomCreate,room_id:int, db: Session=Depends(get_db)):
    UpdateRoom = jsonable_encoder(room)
    db_room= db.query(models.Room).filter(models.Room.id==room_id).first()
    if db_room is None : 
        raise HTTPException ( status_code=404 , detail= ' room not found ')
    db.query(models.Room).filter(models.Room.id==room_id).update(UpdateRoom)
    db.commit()
    return { 'room  successfully updated '}

 
@router.delete('/room/{room_id}')
def DeleteRoom(room_id: int ,db: Session=Depends(get_db)):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first() 
    if db_room is None : 
        raise HTTPException (status_code=404 , detail= ' room not found ')
    db.query(models.Room).filter(models.Room.id==room_id).delete()
    db.commit()
    return { 'room successfully updated'}
