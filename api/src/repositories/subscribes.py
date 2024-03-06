from models import SubscribeModel
from repositories.base import SQLAlchemyRepository


class SubsRepository(SQLAlchemyRepository):
    model = SubscribeModel