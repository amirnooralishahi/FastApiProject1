from pydantic import BaseModel,EmailStr,constr,conint
from datetime import datetime





class RoomBase(BaseModel): 
        location:str
        Dormitory:constr(max_length=64)
        Bed_Service:constr(max_length=256)
        Perspective:str
        Time_reserve:datetime
class RoomCreate(RoomBase):
        Building_Information:str
        Toilet_Bathroom:constr(max_length=64)
        Accommodation_cap:constr(max_length=100)
        Internal_Faclities:str
        Additional_Details:str
        
class RoomShow(RoomBase):
    id:int
    class config: 
        orm_mode=True