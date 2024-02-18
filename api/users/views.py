from typing import Annotated
from fastapi import APIRouter, Path, Depends,status
from users import crud
from users.schemas import UserCreate,User
from models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/users", tags=['users'])


@router.post("/",
             response_model=User,
             status_code=status.HTTP_201_CREATED,)
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(user_in=user, session=session)


@router.get("/{user_id}/")
async def get_user_by_id(user_id: Annotated[int, Path(ge=1, lt=1000000)]):
    return {user_id}
