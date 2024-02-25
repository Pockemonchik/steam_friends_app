from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from db.db_helper import db_helper


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        session = db_helper.get_scoped_session() 
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await session.execute(stmt)
        await session.commit()
        await session.close()
        return res.scalar_one()
    
    async def find_all(self):
        session = db_helper.get_scoped_session() 
        stmt = select(self.model)
        res = await session.execute(stmt)
        await session.close()
        res = [row[0].to_read_model() for row in res.all()]
        return res