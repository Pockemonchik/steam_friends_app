from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreate, UserUpdate
from models import User as UserModel


async def get_users(session: AsyncSession) -> list[UserModel]:
    stmt = select(UserModel).order_by(UserModel.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)

async def create_user(session: AsyncSession, user_in: UserCreate) ->UserModel:
    user = UserModel(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user