from fastapi import HTTPException , Request , Depends ,status,APIRouter 
from sqlalchemy.orm import Session 
from schemas import users as schemas 
from models import Passenger as models 
from fastapi.encoders import jsonable_encoder 
from dependencies import get_db
router=APIRouter()
@router.get('/amir/')
def create_user(user:schemas.UserCreatePassenger,db:Session=Depends(get_db)):
   db_user=db.query(models.Passenger).filter(models.Passenger.NationalCode==user.NationalCode).first()
   if db_user: 
       raise HTTPException(status_code=400, detail= ' National code already is exist')
   user=models.Passenger(**user.model_dump(exclude_unset=True))
   db.add(user)
   db.commit()
   db.refresh(user)
   return user



@router.get('/users/{user_id}',response_model=schemas.UserShow)
def read_user(user_id:int , db: Session=Depends(get_db)):
    db_user=db.query(models.Passenger).filter(models.Passenger.id==user_id).first()
    if db_user is None: 
        raise HTTPException(status_code=404 ,detail='User not found')
    return db_user

@router.put('/users/{user_id}/update')
async def UpdateUser(user: schemas.UserCreatePassenger,user_id: int , db: Session=Depends(get_db)): 
    Update = jsonable_encoder(user)
    db_user = db.query(models.Passenger).filter(models.Passenger.id==user_id).first()
    if db_user is None : 
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail='User not found ')
    
    db.query(models.Passenger).filter(models.Passenger.id==user_id).update(Update)
    db.commit()
    
    return { ' user successfully updated'}

# @router.patch('')
