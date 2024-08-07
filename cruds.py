from sqlalchemy.orm import Session
import models
import schemas


def get_user(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()


def create_user(db: Session, user: schemas.UserSchema):
    db_user = models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

