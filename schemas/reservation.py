from pydantic import BaseModel,EmailStr,constr,conint
from datetime import datetime

class reserationsBase(BaseModel): 
    passenger_id:int 
    DeliveryDate:datetime
    DischargeDatee:datetime
    Evacution:str
