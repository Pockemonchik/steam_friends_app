from steam import Steam
import os

KEY = os.environ.get("STEAM_KEY", "53DCDE6701B169E877EADFDB023D78EA")
steam = Steam(KEY)

# steam id 76561198381522154
async def aoi_get_steam_user_info(steam_id: str):
    return await steam.users.get_user_details(steam_id)


async def aoi_get_steam_user_friends_info(steam_id: str):
    return await steam.users.get_user_friends_list(steam_id)


def get_steam_user_info(steam_id: str):
    return steam.users.get_user_details(steam_id)


def get_steam_user_friends_info(steam_id: str, filter_str: str = None):
    steam_data = steam.users.get_user_friends_list(steam_id)
    print(steam_data["friends"][0])
    online_friends = list(
        filter(
            lambda x: "gameextrainfo" in x or x["personastate"] == 1,
            steam_data["friends"],
        ),
    )

    gaming_friends = list(
        map(
            lambda x: str(x["personaname"])
            + " ---->> "
            + (x["gameextrainfo"] if "gameextrainfo" in x else "В сети")
            + "\n",
            online_friends,
        ),
    )

    result = "".join(gaming_friends)
    return result


def main() -> None:
    print(get_steam_user_friends_info("76561198381522154"))


if __name__ == "__main__":
    main()
