from sqlalchemy import Column,BigInteger,Integer,ForeignKey,String,DateTime,Boolean
from sqlalchemy.orm import relationship
from database import Base 
from datetime import datetime


class Reservation(Base): 
    __tablename__ = 'reserve'
    id = Column(Integer, primary_key=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'))
    DeliveryDate = Column(DateTime)
    DischargeDate = Column(DateTime)
    Evacuation = Column(String)

    passenger = relationship("Passenger", back_populates='reserve')  # اصلاح این خط

    def __str__(self):
        return f'{self.passenger_id}-{self.id}'
