from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreate, UserUpdate, User

from users.schemas import UserCreate

async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)

async def create_user(session: AsyncSession, user_in: UserCreate) ->dict:
    user = User(user_in.model_dump())
    session.add(user)
    await session.commit()
    return {"success": "True",
            "user": user}