from steam import Steam
from decouple import config

KEY = "53DCDE6701B169E877EADFDB023D78EA"
steam = Steam(KEY)
# steam id 76561198381522154
def get_steam_user_info(steam_id:str)-> dict:
    return steam.users.get_user_details(steam_id)

def get_steam_user_friends_info(steam_id:str)-> dict:
    return steam.users.get_user_friends_list(steam_id)
print(steam.users.search_user("76561198381522154"))
