from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    icon_src: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config():
        from_attributes = True
class PhotoBase(BaseModel):
    title: str
    img_src: str

class PhotoCreate(PhotoBase):
    pass

class Photo(PhotoBase):
    id: int
    owner_id: int
    likes: list[User]

    class Config():
        from_attributes = True


class Like(BaseModel):
    user_id: int
