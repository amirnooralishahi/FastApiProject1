from sqlalchemy import Column,BigInteger,Integer,ForeignKey,String,DateTime,Boolean
from sqlalchemy.orm import relationship
from database import Base 

class Passenger(Base):
    __tablename__ = 'passenger' 
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    username = Column(String, unique=True)
    password = Column(String(128))
    NationalCode = Column(Integer, unique=True, index=True)
    is_owner = Column(Boolean, default=False, nullable=True)
    is_inspector = Column(Boolean, default=False, nullable=True)  # تغییر نام متغیر به `snake_case`
    email = Column(String(128))
    job_title = Column(String, nullable=True)  # تغییر نام متغیر به `snake_case`

    payment = relationship("Payment", back_populates="passenger")
    recordreserve = relationship("RecordReserve", back_populates="passenger", cascade='all,delete')
    reserve = relationship("Reservation", back_populates='passenger')  # اصلاح مقدار

    def __str__(self):
        return f'{self.NationalCode}-{self.lastname}'



print(Passenger ,'\n')