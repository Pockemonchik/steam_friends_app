from typing import Annotated
from fastapi import APIRouter,Path

from users import crud
from users.schemas import CreateUser
router = APIRouter(prefix="/users", tags=['users'])



@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)

@router.get("/{user_id}/")
def get_user_by_id(user_id: Annotated[int, Path(ge=1,lt =1000000)]):
    return {user_id}