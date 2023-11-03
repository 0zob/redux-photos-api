from sqlalchemy.orm import Session

from . import models, schemas

def get_photos(db: Session):
    return db.query(models.Photo).all()

def create_photo(db: Session, photo: schemas.PhotoCreate):
    db_photo = models.Photo(title=photo.title, like=photo.like, img_src=photo.img_src)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo
