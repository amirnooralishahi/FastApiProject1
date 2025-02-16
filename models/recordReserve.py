from sqlalchemy import Column,BigInteger,Integer,ForeignKey,String,DateTime,Boolean
from sqlalchemy.orm import relationship
from database import Base 
from datetime import datetime
from Passenger import Passenger 

class RecordReserve(Base) :
    __tablename__='RecordReserve'
    id=Column(Integer,primary_key=True)
    passenger_id=Column(Integer,ForeignKey('passenger.id',ondelete="CASCADE"))
    room_id=Column(Integer,ForeignKey('room.id',ondelete="CASCADE"))
    payment_id=Column(Integer,ForeignKey('payment.id',ondelete="CASCADE"))
    passenger = relationship("passenger", back_populates="recordReserve")
    room=relationship('room',back_populates='recordReserve')
    payment= relationship('payment',back_populates='recordReserve' )
    date=Column(DateTime,default=datetime.utcnow )
    
    def __str__(self):
        return f' {self.passenger_id}'
    
    