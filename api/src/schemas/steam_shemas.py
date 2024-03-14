from pydantic import BaseModel, ConfigDict

class SteamFriendsSchema(BaseModel):
    username: str
    chat_id: str