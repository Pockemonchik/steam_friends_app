from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    username: str
    steam_token: str


class UserCreate(UserBase):
    pass

class UserUpdate(UserCreate):
    pass

class UserUpdatePartial(UserCreate):
    username: str or None
    steam_token: str or None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int