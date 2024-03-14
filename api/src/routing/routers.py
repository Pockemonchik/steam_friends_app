from routing.users import router as user_router
from routing.subscribes import router as subs_router
from routing.steam import router as steam_router

all_routers = [
    user_router,
    subs_router,
    steam_router
]
