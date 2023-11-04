from pydantic import BaseModel


class PhotoBase(BaseModel):
    title: str
    like: bool = False
    img_src: str

class PhotoCreate(PhotoBase):
    pass

class Photo(PhotoBase):
    id: int
    owner_id: int

    class Config():
        orm_mode = True

class UserBase(BaseModel):
    name: str
    icon_src: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    photo: list[Photo] = []

    class Config():
        orm_mode = True
