from .base import Base
from sqlalchemy import Mapped 


class User(Base):
    username: Mapped(str)
    password: Mapped(str)
