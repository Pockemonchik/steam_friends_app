from sqlalchemy import select
from models import SubscribeModel
from repositories.base import SQLAlchemyRepository


class SubsRepository(SQLAlchemyRepository):
    model = SubscribeModel

    async def filter_by_user(self, user_name: str):
        statement = select(self.model).where(self.model.user.username == user_name)
        print("stmt",statement)
        res = await self.session.execute(statement)
        obj_list = res.all()
        result = [row[0].to_read_model() for row in obj_list]
        print(result)
        if result is None:
            await self.session.close()
            return None
        await self.session.close()
        return result