from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update

from db.db_helper import db_helper


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError

    @abstractmethod
    async def update_one():
        raise NotImplementedError

    @abstractmethod
    async def delete_one():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        session = db_helper.get_scoped_session()
        stmt = insert(self.model).values(**data).returning(self.model.id)
        obj = await session.execute(stmt)
        await session.commit()
        await session.close()
        return obj.scalar_one()

    async def find_one(self, id: int):
        session = db_helper.get_scoped_session()
        obj = await session.get(self.model, id)
        if obj is None:
            await session.close()
            return None
        await session.close()
        return obj.to_read_model()

    async def find_all(self):
        session = db_helper.get_scoped_session()
        stmt = select(self.model)
        obj = await session.execute(stmt)
        await session.close()
        obj = [row[0].to_read_model() for row in obj.all()]
        return obj

    async def update_one(self, id: int, data: dict):
        session = db_helper.get_scoped_session()
        obj = await session.get(self.model, id)
        if obj is None:
            await session.close()
            return None
        for name, value in data.items():
            setattr(obj, name, value)
        await session.commit()
        
        return obj.id

    async def delete_one(self, id: int):
        session = db_helper.get_scoped_session()
        obj = await session.get(self.model, id)
        if obj is None:
            await session.close()
            return None
        await session.delete(obj)
        await session.commit()
        await session.close()
        return id
