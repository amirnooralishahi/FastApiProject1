from sqlalchemy import Column,BigInteger,Integer,ForeignKey,String,DateTime
from database import Base 


class Payment(Base): 
    __tablename__='payment'
    id= Column(Integer, primary_key=True)
    Allpaid = Column(BigInteger)
    tuition=Column(Integer)
    debt= Column(Integer)
    paymentDate=Column(DateTime)




