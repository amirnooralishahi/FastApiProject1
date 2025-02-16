from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE= 'postgresql://postgres:13801211@localhost:5432/finalproject'
engine=create_engine(URL_DATABASE,echo=True)
SessionLocal=sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base=declarative_base() 
