from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreate, UserUpdate, UserUpdatePartial
from models import User as UserModel


async def get_users(session: AsyncSession) -> list[UserModel]:
    stmt = select(UserModel).order_by(UserModel.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)

async def create_user(session: AsyncSession, user_in: UserCreate) -> UserModel:
    user = UserModel(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user

async def get_user(session: AsyncSession, user_id: int) -> UserModel:
    return await session.get(UserModel, user_id)

async def update_user(
    session: AsyncSession,
    user: UserModel,
    user_update: UserUpdate or UserUpdatePartial,
    partial: bool = False,
) -> UserModel:
    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()
    return user


async def delete_user(
    session: AsyncSession,
    user: UserModel,
) -> None:
    await session.delete(user)
    await session.commit()