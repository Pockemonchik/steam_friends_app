from schemas.user_schema import UserSchemaCreate
from repositories.base import AbstractRepository


class UserService:
    def __init__(self, users_repo: AbstractRepository):
        self.users_repo: AbstractRepository = users_repo()

    async def add_user(self, user: UserSchemaCreate):
        user_dict = user.model_dump()
        user = await self.users_repo.add_one(user_dict)
        return user

    async def get_users(self):
        users = await self.users_repo.find_all()
        return users