from sqlalchemy import Column,BigInteger,Integer,ForeignKey,String,DateTime,Boolean
from sqlalchemy.orm import relationship
from database import Base 
from datetime import datetime


class RecordReserve(Base):
    __tablename__ = 'record_reserve'  # تغییر نام جدول به صورت استاندارد
    id = Column(Integer, primary_key=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id', ondelete="CASCADE"))
    room_id = Column(Integer, ForeignKey('room.id', ondelete="CASCADE"))
    payment_id = Column(Integer, ForeignKey('payment.id', ondelete="CASCADE"))
    date = Column(DateTime, default=datetime.utcnow)

    passenger = relationship("Passenger", back_populates="recordreserve")  # اصلاح مقدار
    room = relationship("Room", back_populates="recordreserve")  # اصلاح مقدار
    payment = relationship("Payment", back_populates="recordreserve")  # اصلاح مقدار

    def __str__(self):
        return f'{self.passenger_id}'

    