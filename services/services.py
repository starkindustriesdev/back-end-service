from core.db_utils import DbManager
from models.models import UserIn


USERS = 'users'

class UserService:

    async def create_user(self, user_data :UserIn):
        user = DbManager().db[USERS].insert_one(user_data.model_dump())
        return user
    
    async def get_user(self):
        users = DbManager().db[USERS].find().to_list()
        for user in users:
            user.pop('_id')
        return users