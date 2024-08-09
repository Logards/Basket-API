from sqlalchemy.orm import Session
import models
import schemas
import bcrypt
import uuid


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def get_user(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()


def connect_user(db: Session, user: schemas.UserConnectSchema):
    db_user = get_user(db, user.email)
    if db_user is None:
        return "User not found"
    if verify_password(user.password, db_user.password) is False:
        return "Invalid password"
    return db_user


def create_user(db: Session, user: schemas.UserSchema):
    db_user = models.User(email=user.email,
                          password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

