from sqladmin import ModelView
import models


class SubsAdmin(ModelView, model=models.SubscribeModel):
    column_list = [models.SubscribeModel.id, models.SubscribeModel.user_id,
                   models.SubscribeModel.game,models.SubscribeModel.gamer_name]


class UserAdmin(ModelView, model=models.UserModel):
    column_list = [models.UserModel.id, models.UserModel.username]



