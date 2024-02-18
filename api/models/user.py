from .base import Base
from sqlalchemy.orm import Mapped 


class User(Base):
    username: Mapped[str]
    steam_token: Mapped[str]
