from fastapi import HTTPException , Depends ,status,APIRouter 
from sqlalchemy.orm import Session
from schemas import payment as schemas
from models import Payment as models 
from dependencies import get_db
from fastapi.encoders import jsonable_encoder




router = APIRouter()


@router.post('/payment/create')
def DonePayment(payment:schemas.PaymentCreate,db:Session=Depends(get_db)): 
    db_pay= db.query(models.Payment).filter(models.Payment.room_id == payment.room_id) 
    if db_pay is None : 
        raise HTTPException(status_code=404 , detail= ' room not found for done payment ')
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment 

@router.get('/payment/{payment_id}',response_model=schemas.PaymentShow)
def ReadPayment(payment_id:int , db: Session = Depends(get_db) ):
    db_pay = db.query(models.Payment).filter(models.Payment.id == payment_id ).first()
    if db_pay is None : 
        raise HTTPException ( status_code=404 , detail='room not found')
    return db_pay 



@router.put( '/payment/{payment_id}',response_model=schemas.PaymentShow)
def UpdatedPayment(payment: schemas.PaymentCreate,payment_id:int , db:Session= Depends(get_db )): 
    db_pay = db.query( models.Payment).filter(models.Payment.id == payment_id).first( )
    if db_pay is None : 
        raise HTTPException(status_code=404 , detail= ' room not found for done payment')
    UpdatePayment = jsonable_encoder(payment)
    db.query(models.Payment).filter(models.Payment.id == payment_id).update(UpdatedPayment)
    db.commit()
    return { 'payment  successfully updated '}


@router.delete('/payment/{payment_id}')
def DeletedPayment(payment_id:int, db: Session=Depends(get_db)): 
    db_pay = db.query( models.Payment ).filter( models.Payment.id == payment_id).first( )
    if db_pay is None : 
        raise HTTPException ( status_code= 404 , detail= "room not found for done payment")
    db.query(models.Payment).filter(models.Payment.id == payment_id ).delete()
    db.commit()
    return { ' payment successfully deleted '}
