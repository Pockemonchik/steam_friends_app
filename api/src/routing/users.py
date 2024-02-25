from typing import Annotated
from fastapi import APIRouter, Path, Depends,status

from schemas.user_schema import UserSchemaCreate,UserSchema, UserSchemaUpdate, UserSchemaUpdatePartial
from routing.dependencies import user_service
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=['users'])

@router.get("/",
            response_model=list[UserSchema])
async def get_users(
    users_service: Annotated[UserService, Depends(user_service)],
):
    users = await users_service.get_users()
    return users

@router.post("/",
             status_code=status.HTTP_201_CREATED,)
async def create_user(
    user: UserSchemaCreate,
    users_service: Annotated[UserService, Depends(user_service)],
    ):
    user_id = await users_service.add_user(user)
    return {"user_id": user_id}


# @router.get("/{user_id}/", response_model=UserSchema)
# async def get_user(
#     user: UserSchema = Depends(user_by_id),
# ):
#     return user

# @router.put("/{user_id}/")
# async def update_user(
#     user_update: UserSchemaUpdate,
#     user: UserSchema = Depends(user_by_id),
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await crud.update_user(
#         session=session,
#         user=user,
#         user_update=user_update,
#     )


# @router.patch("/{user_id}/")
# async def update_user_partial(
#     user_update: UserSchemaUpdatePartial,
#     user: UserSchema = Depends(user_by_id),
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await crud.update_user(
#         session=session,
#         user=user,
#         user_update=user_update,
#         partial=True,
#     )


# @router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_user(
#     user: UserSchema = Depends(user_by_id),
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ) -> None:
#     await crud.delete_user(session=session, user=user)
