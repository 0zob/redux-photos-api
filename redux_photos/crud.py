from sqlalchemy.orm import Session

from . import models, schemas

def get_photos(db: Session):
    return db.query(models.Photo).all()

def create_user_photo(db: Session, photo: schemas.PhotoCreate, user_id: int):
    db_photo = models.Photo(**photo.model_dump(), owner_id=user_id)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, icon_src=user.icon_src)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
