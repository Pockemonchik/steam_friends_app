from typing import Annotated
from fastapi import APIRouter, Depends, status,HTTPException


from schemas.subscribe_shema import (
    SubscribeSchemaCreate,
    SubscribeSchema,
    SubscribeSchemaUpdate,
    SubscribeSchemaUpdatePartial,
)
from routing.dependencies import subs_service
from services.subscribe_service import SubscribeService

router = APIRouter(prefix="/subs", tags=["subs"])


@router.get("/", response_model=list[SubscribeSchema])
async def get_subs(
    subs_service: Annotated[SubscribeService, Depends(subs_service)],
):
    subs = await subs_service.get_subs()
    return subs

@router.get("/user-subs/", response_model=list[SubscribeSchema])
async def get_subs_by_user(
    user_name:str,
    subs_service: Annotated[SubscribeService, Depends(subs_service)],
):
    subs = await subs_service.get_subs_by_user(user_name=user_name)
    return subs


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_sub(
    sub: SubscribeSchemaCreate,
    subs_service: Annotated[SubscribeService, Depends(subs_service)],
):
    sub_id = await subs_service.add_sub(sub)
    return {"sub_id": sub_id}


@router.get("/{sub_id}/")
async def get_sub(
    sub_id: int, subs_service: Annotated[SubscribeService, Depends(subs_service)]
):
    sub = await subs_service.get_sub(id=sub_id)
    if not sub:
        raise HTTPException(status_code=404, detail="Item not found")
    return sub


@router.patch("/{sub_id}/")
async def update_sub_partial(
    sub_id: int,
    sub_update: SubscribeSchemaUpdatePartial,
    subs_service: Annotated[SubscribeService, Depends(subs_service)],
):
    sub_id = await subs_service.update_sub(id=sub_id, sub=sub_update)
    if not sub_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"sub_id": sub_id}


@router.put("/{sub_id}/")
async def update_sub(
    sub_id: int,
    sub_update: SubscribeSchemaUpdate,
    subs_service: Annotated[SubscribeService, Depends(subs_service)],
):
    sub_id = await subs_service.update_sub(id=sub_id, sub=sub_update)
    if not sub_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"sub_id": sub_id}


@router.delete("/{sub_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sub(
    sub_id: int,
    subs_service: Annotated[SubscribeService, Depends(subs_service)],
) -> None:
    sub_id = await subs_service.delete_sub(id=sub_id)
    if not sub_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"sub_id": sub_id}
