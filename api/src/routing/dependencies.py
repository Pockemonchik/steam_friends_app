
from repositories import UsersRepository,SubsRepository
from services.user_service import UserService
from services.subscribe_service import SubscribeService
from db.db_helper import db_helper


def user_service():
    return UserService(UsersRepository(db_helper.get_scoped_session()))


def subs_service():
    return SubscribeService(SubsRepository(db_helper.get_scoped_session()))