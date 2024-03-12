from steam import Steam
import asyncio
KEY = "53DCDE6701B169E877EADFDB023D78EA"
steam = Steam(KEY)
# steam id 76561198381522154
async def aoi_get_steam_user_info(steam_id:str):
    return await steam.users.get_user_details(steam_id)

async def aoi_get_steam_user_friends_info(steam_id:str):
    return await steam.users.get_user_friends_list(steam_id)


def get_steam_user_info(steam_id:str):
    return steam.users.get_user_details(steam_id)

def get_steam_user_friends_info(steam_id:str):
    return steam.users.get_user_friends_list(steam_id)

def main() -> None:
    print(get_steam_user_friends_info("76561198381522154"))

if __name__ == "__main__":
    main()
