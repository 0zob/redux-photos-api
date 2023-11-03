from pydantic import BaseModel


class PhotoBase(BaseModel):
    title: str
    like: bool = False
    img_src: str

class PhotoCreate(PhotoBase):
    pass

class Photo(PhotoBase):
    id: int

    class Config():
        orm_mode = True
