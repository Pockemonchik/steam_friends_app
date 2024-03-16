from pydantic import BaseModel, ConfigDict


class SubscribeSchemaBase(BaseModel):
    user_id: int
    gamer_name: str
    game: str

class SubscribeSchemaCreate(SubscribeSchemaBase):
    pass


class SubscribeSchemaUpdate(SubscribeSchemaCreate):
    pass


class SubscribeSchemaUpdatePartial(SubscribeSchemaCreate):
    user_id: int | None


class SubscribeSchema(SubscribeSchemaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
