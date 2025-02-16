from pydantic import BaseModel,EmailStr,constr,conint
from datetime import datetime




class recordReserveCreate(BaseModel) : 
    
    passenger_id:int
    room_id: int 
    payment :int 
    date:datetime.utcnow
    
class recordReserveShow(recordReserveCreate): 
       id: int