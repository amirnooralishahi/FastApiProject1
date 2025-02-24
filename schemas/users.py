from pydantic import BaseModel,EmailStr,constr,conint


class UserBase(BaseModel):
    firstname: constr(min_length=3, max_length=50)
    lastname: constr(min_length=4, max_length=64)
    username: constr(min_length=4, max_length=64)
    email: EmailStr|None 



class UserCreatePassenger(UserBase):
     
    password: constr(min_length=6)
    NationalCode: int
    # Phone:conint(ge=100000000000,le=999999999999)
    is_owner:bool|None
    is_inspector:bool |None
    job_title:str 
    
class UserShow(UserBase):
    id:int
    class config: 
        orm_mode=True

    


    
    