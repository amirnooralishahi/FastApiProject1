from sqlalchemy import Column,BigInteger,Integer,ForeignKey,String,DateTime
from sqlalchemy.sql import func
from datetime import datetime
from database import Base 
from sqlalchemy.orm import relationship

class Payment(Base): 
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'))
    room_id = Column(Integer, ForeignKey('room.id'))
    Allpaid = Column(BigInteger)
    tuition = Column(Integer)
    debt = Column(Integer)
    paymentDate = Column(DateTime)

    passenger = relationship("passenger", back_populates="payment")
    room = relationship("room", back_populates="payment")
    recordreserve = relationship("RecordReserve", back_populates="payment", uselist=False,cascade='all,delete')

    def __str__(self):
        return f'{self.tuition}-{self.debt}'




