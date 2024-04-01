from typing import List, TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from schemas.user_schema import UserSchema
from .base_model import BaseModel


if TYPE_CHECKING:
    from models.subscribe_model import SubscribeModel


class UserModel(BaseModel):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(index=True, unique=True)
    steam_id: Mapped[str]
    chat_id: Mapped[str]
    subscribes: Mapped[List["SubscribeModel"]] = relationship(back_populates="user")

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            chat_id=self.chat_id,
            username=self.username,
            steam_id=self.steam_id,
        )

    def __str__(self):
        return self.username
