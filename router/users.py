from fastapi import HTTPException , Request , Depends ,status,APIRouter 
from sqlalchemy.orm import Session 
from schemas import users as schemas 
from models.Passenger import Passenger
from fastapi.encoders import jsonable_encoder 
from dependencies import get_db
router=APIRouter()
@router.post('/users/create',response_model=schemas.UserShow)
def create_user(user:schemas.UserCreatePassenger,db:Session=Depends(get_db)):
   db_user=db.query(Passenger).filter(Passenger.NationalCode==user.NationalCode).first()
   if db_user: 
       raise HTTPException(status_code=400, detail= ' National code already is exist')
   user=Passenger(**user.model_dump(exclude_unset=True))
   db.add(user)
   db.commit()
   db.refresh(user)
   return user



@router.get('/users/{user_id}',response_model=schemas.UserShow)
def read_user(user_id:int , db: Session=Depends(get_db)):
    db_user=db.query(Passenger).filter(Passenger.id==user_id).first()
    if db_user is None: 
        raise HTTPException(status_code=404 ,detail='User not found')
    return db_user

@router.put('/users/{user_id}/update')
async def UpdateUser(user: schemas.UserCreatePassenger,user_id: int , db: Session=Depends(get_db)): 
    
    db_user = db.query(Passenger).filter(Passenger.id==user_id).first()
    if db_user is None : 
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail='User not found ')
    
    db.query(Passenger).filter(Passenger.id==user_id).update()
    db.commit()
    
    return { ' user successfully updated'}

@router.delete('/users/{user_id}')
def delete_user(user_id : int , db: Session=Depends(get_db)):
    db_user = db.query(Passenger).filter(Passenger.id == user_id).first()
    if db_user is None : 
        raise HTTPException ( status_code=404 , detail= ' user not found ')
    db.query(Passenger).filter(Passenger.id==user_id).delete()
    db.commit()
    return {"user with successfully deleted "} 

@router.get('/users/')
def ShowAllUser(db: Session=Depends(get_db)) :
    db_user = db.query(Passenger).all()
    return db_user