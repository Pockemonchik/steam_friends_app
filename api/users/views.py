from typing import Annotated
from fastapi import APIRouter, Path, Depends,status
from users import crud
from users.schemas import UserCreate,User, UserUpdate, UserUpdatePartial
from models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import user_by_id

router = APIRouter(prefix="/users", tags=['users'])

@router.get("/", response_model=list[User])
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_users(session=session)

@router.post("/",
             response_model=User,
             status_code=status.HTTP_201_CREATED,)
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(user_in=user, session=session)


@router.get("/{user_id}/", response_model=User)
async def get_user(
    user: User = Depends(user_by_id),
):
    return user

@router.put("/{user_id}/")
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )


@router.patch("/{user_id}/")
async def update_user_partial(
    user_update: UserUpdatePartial,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
        partial=True,
    )


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_user(session=session, user=user)
