from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import Base, engine, SessionLocal

# يعمل Create للجداول لو مش موجودة
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency للـ DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "FastAPI connected to PostgreSQL 🎉"}

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
