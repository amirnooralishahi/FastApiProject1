from pydantic import BaseModel,EmailStr,constr,conint
from datetime import datetime

class reserationsBase(BaseModel): 
    passenger_id:int 
    DeliveryDate:datetime
    DischargeDate:datetime
    Evacution:str
    class config: 
        orm_mode=True