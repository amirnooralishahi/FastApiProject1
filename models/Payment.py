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
    all_paid = Column(BigInteger)  # تغییر نام متغیر به `snake_case`
    tuition = Column(Integer)
    debt = Column(Integer)
    payment_date = Column(DateTime)

    passenger = relationship("Passenger", back_populates="payment")
    room = relationship("Room", back_populates="payment")
    recordreserve = relationship("RecordReserve", back_populates="payment", uselist=False, cascade='all,delete')

    def __str__(self):
        return f'{self.tuition}-{self.debt}'




