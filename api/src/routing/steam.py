import json
from typing import Annotated
from fastapi import APIRouter, Depends

from core.config import settings
from utils.produser import AIOWebProducer
from schemas.steam_shemas import SteamFriendsSchema
from routing.dependencies import user_service
from services.user_service import UserService

router = APIRouter(prefix="/steam", tags=["steam"])


@router.get("/friends")
async def get_friends(
    params: Annotated[SteamFriendsSchema, Depends()],
    user_service: Annotated[UserService, Depends(user_service)],
):
    user = await user_service.get_user_by_name(username=params.username)
    message_to_produce = json.dumps(
        {
            "telegram_id": user.chat_id,
            "game": 'all',
            "gamer_name": 'all',
            "steam_id": user.steam_id,
        }
    ).encode(encoding="utf-8")
    producer = AIOWebProducer(topic=settings.kafka_steam_topic)
    await producer.send(value=message_to_produce)
    return {"status": "process"}
