from pydantic import BaseModel,EmailStr,constr,conint
from datetime import datetime

class PaymentCreate(BaseModel):
    passenger_id:int
    room_id:int
    Allpaid:int
    tuition:int
    debt:int
    paymentDate:datetime
    
class PaymentShow(PaymentCreate):
    id:int