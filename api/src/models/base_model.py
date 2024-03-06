
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Mapped,mapped_column, DeclarativeBase



class BaseModel(DeclarativeBase):
    __abstract__ = True
       
    id: Mapped[int] = mapped_column(primary_key=True)
    