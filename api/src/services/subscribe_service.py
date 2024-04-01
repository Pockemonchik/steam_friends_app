from schemas.subscribe_shema import SubscribeSchemaCreate
from repositories.base import AbstractRepository


class SubscribeService:
    def __init__(self, subs_repo: AbstractRepository):
        self.subs_repo: AbstractRepository = subs_repo

    async def add_sub(self, sub: SubscribeSchemaCreate):
        sub_dict = sub.model_dump()
        sub = await self.subs_repo.add_one(sub_dict)
        return sub

    async def get_subs(self):
        subs = await self.subs_repo.find_all()
        return subs
    
    async def get_subs_with_users(self):
        subs = await self.subs_repo.find_all_with_users()
        return subs

    async def get_sub(self, id: int):
        sub = await self.subs_repo.find_one(id=id)
        return sub

    async def get_subs_by_user(self, user_name: str):
        subs = await self.subs_repo.filter_by_user(user_name=user_name)
        return subs

    async def update_sub(self, id: int, sub: SubscribeSchemaCreate):
        sub_dict = sub.model_dump()
        sub = await self.subs_repo.update_one(id=id, data=sub_dict)
        return sub

    async def delete_sub(self, id: int):
        sub = await self.subs_repo.delete_one(id=id)
        return sub
