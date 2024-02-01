from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name: str
    steam_token: str


class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int