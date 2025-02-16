from sqlalchemy import Column,BigInteger,Integer,ForeignKey,String,DateTime,Boolean
from sqlalchemy.orm import relationship
from database import Base 
from datetime import datetime
from Passenger import Passenger 

class reservation(Base): 
    __tablename__='reserve'
    id = Column(Integer, primary_key=True)
    passenger=Column(Integer,ForeignKey('passenger.id'))
    DeliveryDate=Column(DateTime)
    DischargeDate=Column(DateTime)
    Evacution=Column(String)
    reserve=relationship("passenger",back_populates='passenger')
    def __str__(self):
        return f'{self.passenger}-{self.id}'
    