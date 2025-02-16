
from database import engine, SessionLocal
import uvicorn 
from models import Room,Payment

# Passenger.Base.metadata.create_all(bind=engine)
# Payment.Base.metadata.create_all(bind=engine)
# Room.Base.metadata.create_all(bind=engine)
if __name__=='__main__':
    uvicorn.run('config:app',host='0.0.0.0',port=8000,reload=True) 