from sqlalchemy import Column,BigInteger,Integer,ForeignKey,String,DateTime,Boolean
from sqlalchemy.orm import relationship
from database import Base 








class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    location = Column(String)
    dormitory = Column(String)  # تغییر نام متغیر به `snake_case`
    building_information = Column(String)  # تغییر نام متغیر به `snake_case`
    bed_service = Column(String(100))  # تغییر نام متغیر به `snake_case`
    toilet_bathroom = Column(String(100))  # تغییر نام متغیر به `snake_case`
    accommodation_cap = Column(String(100), nullable=True)
    perspective = Column(String)
    internal_facilities = Column(String)  # تغییر نام متغیر به `snake_case`
    additional_details = Column(String)  # تغییر نام متغیر به `snake_case`
    time_reserve = Column(DateTime)

    payment = relationship("Payment", back_populates="room")
    recordreserve = relationship('RecordReserve', back_populates="room", uselist=False, cascade='all,delete')

    def __str__(self):
        return f'{self.dormitory}'

    


