import os
import json
import aiohttp
import asyncio

api_url = os.getenv("API_URL", "http://localhost:8000")


async def register(username: str, steam_id: str, chat_id: str):
    data = {
        "username": username,
        "steam_id": steam_id,
        "chat_id": chat_id,
    }
    print(data)
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{api_url}/users", json=data) as resp:
            print(resp.status)
            print(await resp.text())
            if await resp.status == 201:
                return "Вы успешно зарегистрировались"
            else:
                return "Ошибка при регистрации"

async def fetch_friends(username: str, chat_id: str):
    params = {
        "username": username,
        "chat_id": chat_id,
    }
    print(params)
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{api_url}/steam/friends", params=params) as resp:
            # print(resp.status)
            # print(await resp.text())
            if resp.status == 200:
                return "Проверяем Ваших друзей ..."
            else:
                return "Ошибка на сервере"

if __name__ == "__main__":

    asyncio.run(register("user", "1213", "1213"))
