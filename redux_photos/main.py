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

@app.get("/", response_model=list[schemas.Photo])
def read_photos(db: Session = Depends(get_db)):
    photos = crud.get_photos(db)
    return photos

@app.post("/", response_model=schemas.Photo)
def create_photos(photo: schemas.PhotoCreate, db: Session = Depends(get_db)):
    return crud.create_photo(db, photo)

