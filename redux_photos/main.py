from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/photos", response_model=list[schemas.Photo])
def read_photos(db: Session = Depends(get_db)):
    photos = crud.get_photos(db)
    return photos


@app.post("/photos/like/{photo_id}", response_model=schemas.Photo)
def like_photo(photo_id: int, data: schemas.Like, db: Session = Depends(get_db)):
    return crud.like_photo(db, photo_id, data.user_id)


@app.post("/users/{user_id}/photos", response_model=schemas.Photo)
def create_photo_for_user(
    user_id: int, photo: schemas.PhotoCreate, db: Session = Depends(get_db)
):
    return crud.create_user_photo(db, photo, user_id)


@app.get("/users", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
