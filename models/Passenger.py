from sqlalchemy import Column,BigInteger,Integer,ForeignKey,String,DateTime,Boolean
from sqlalchemy.orm import relationship
from database import Base 

class Passenger(Base):
    __tablename__='passenger' 
    id=Column(Integer,primary_key=True)
    firstname=Column(String)
    lastname=Column(String)
    username=Column(String,unique=True)
    password=Column(String(128))
    NationalCode=Column(Integer, unique=True,index=True)
    is_owner=Column(Boolean,default=False)
    Is_inspector=Column(Boolean,default=False)
    email=Column(String(128))
    Job_title=Column(String)
    payment= relationship("payment", back_populates="passenger")
    recordreserve=relationship('RecordReserve', back_populates="Passenger",uselist=False,cascade='all,delete')
    reserve=relationship("reserve",back_populates='passenger')

    def __str__(self):
        return f'{self.NationalCode}-{self.lastname}'
    


