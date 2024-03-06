from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from schemas.subscribe_shema import SubscribeSchema
from .base_model import BaseModel

if TYPE_CHECKING:
    from models.user_model import UserModel


class SubscribeModel(BaseModel):
    __tablename__ = "subscribes"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["UserModel"] = relationship(back_populates="subscribes")

    def to_read_model(self) -> SubscribeSchema:
        return SubscribeSchema(
            id=self.id,
            user_id=self.user_id,
        )
