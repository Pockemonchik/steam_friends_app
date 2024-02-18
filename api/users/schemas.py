from pydantic import BaseModel, ConfigDict

class UserShemaBase(BaseModel):
    username: str
    steam_token: str


class UserShemaCreate(UserShemaBase):
    pass

class UserShemaUpdate(UserShemaCreate):
    pass

class UserShemaUpdatePartial(UserShemaCreate):
    username: str or None
    steam_token: str or None


class UserShema(UserShemaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int