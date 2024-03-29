from pydantic import BaseModel, ConfigDict

class UserSchemaBase(BaseModel):
    username: str
    steam_id: str
    chat_id: str


class UserSchemaCreate(UserSchemaBase):
    pass

class UserSchemaUpdate(UserSchemaCreate):
    pass

class UserSchemaUpdatePartial(UserSchemaCreate):
    username: str | None
    steam_id: str | None
    chat_id: str | None


class UserSchema(UserSchemaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int