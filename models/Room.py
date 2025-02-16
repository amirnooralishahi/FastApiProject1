from sqlalchemy import Column,BigInteger,Integer,ForeignKey,String,DateTime,Boolean
from sqlalchemy.orm import relationship
from database import Base 








class Room(Base):
    __tablename__='room'
    id=Column(Integer,primary_key=True)
    location=Column(String)
    Dormitory=Column(String)
    Building_Information=Column(String)
    Bed_Service=Column(String(100))
    Toilet_Bathroom=Column(String(100))
    Accommodation_cap=Column(String(100),nullable=False)
    Perspective=Column(String)
    Internal_Faclities=Column(String)
    Additional_Details=Column(String)
    Time_reserve=Column(DateTime)
    payment = relationship("payment", back_populates="room")
    recordreserve=relationship('RecordReserve', back_populates="room",uselist=False,cascade='all,delete')
    
    def __str__(self):
        return f'{self.Dormitory}'
    
    


