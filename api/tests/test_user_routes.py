from httpx import AsyncClient


async def test_user_add(ac: AsyncClient):
    response = await ac.post(
        "/users/",
        json={
            "username": "string",
            "steam_token": "string",
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    assert response.status_code == 201


async def test_users_get(ac: AsyncClient):
    response = await ac.get("/users/", params={})

    assert response.status_code == 200
    # assert response.json()["status"] == "success"
    # assert len(response.json()["data"]) == 1
