from pydantic import BaseModel,EmailStr,constr,conint


class UserBase(BaseModel):
    firstname: constr(min_length=3, max_length=50)
    lastname: constr(min_length=4, max_length=64)
    username: constr(min_length=4, max_length=64)
    email: EmailStr



class UserCreatePassenger(UserBase):
     
    password: constr(min_length=6)
    NationalCode: conint(ge=1000000000, le=9999999999)
    Phone:conint(ge=100000000000,le=999999999999)
    is_owner:bool
    Is_inspector:bool
    Job_title=str
    
    
class UserShow(UserBase):
    id:int
    class config: 
        orm_mode=True

    


    
    