
from sqlalchemy import declared_attr, Mapped,mapped_column, DeclarativeBase 


class Base(DeclarativeBase):
    __abstract__ = True
    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    