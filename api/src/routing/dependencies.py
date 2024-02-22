
from repositories.users import UsersRepository
from services.user_service import UserService


def user_service():
    return UserService(UsersRepository)

