from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas
import cruds

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/createuser")
async def create_user(user: schemas.UserSchema, db: Session = Depends(get_db)):
    db_user = cruds.get_user(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return db_user


@app.get("/users/{user_email}")
async def get_user(user_email: str, db: Session = Depends(get_db)):
    user = cruds.get_user(db, user_email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
