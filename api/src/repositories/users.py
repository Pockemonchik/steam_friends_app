from models import UserModel
from repositories.base import SQLAlchemyRepository
from sqlalchemy import insert, select, update

class UsersRepository(SQLAlchemyRepository):
    model = UserModel

    # тут надо переделать на фильтр по любому полю
    async def find_one_by_name(self, username: str):
        statement = select(self.model).filter_by(username=username)
        print("stmt",statement)
        res = await self.session.execute(statement)
        obj_list = res.all()
        obj = [row[0].to_read_model() for row in obj_list][0]
        print(obj.username)
        if obj is None:
            await self.session.close()
            return None
        await self.session.close()
        return obj