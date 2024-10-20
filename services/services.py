from core.db_utils import DbManager
from models.models import UserIn


USERS = 'users'

class UserService:

    async def create_user(self, user_data :UserIn):
        user = DbManager().db[USERS].insert_one(user_data.model_dump())
        return user
    
    async def get_user(self):
        user = DbManager().db[USERS].find_one({})
        user.pop('_id')
        return user