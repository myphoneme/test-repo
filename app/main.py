from fastapi import FastAPI, Depends
from app.database import get_db, engine
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models import Base
from app.routers import router
from app.auth import router as auth_router
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
    

@app.get("/dbtest")
def db_test(db: Session = Depends(get_db)):
    try:
        db.execute(text("Select 1"))
        return {"status": "database connection successful"}
    except Exception as e:
        return {"status" : "database connection failed", "error": str(e)}
     