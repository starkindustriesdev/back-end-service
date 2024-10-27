from core.db_utils import DbManager
from models.models import UserIn
from core.config import Config
from fastapi.exceptions import HTTPException
from loguru import logger
from utils.common_utils import generate_user_id
import requests


USERS = 'users'
MASTER_DATA = 'masterdata'

class UserService:

    async def create_user(self, user_data :UserIn):
        try:
            data = {
                    "user_id": generate_user_id(),
                    "first_name": user_data.first_name,
                    "last_name": user_data.last_name,
                    "dob": user_data.dob,
                    "email": user_data.email,
                    "country": user_data.country,
                    "state": user_data.state,
                    "city": user_data.city,
                    "pincode": user_data.pincode,
                    "address": user_data.address
            }
            if not data:
                logger.warning("Please fill all the required details")
                raise HTTPException(status_code= 400, detail="Please fill all the required details")
            
            user = DbManager().db[USERS].insert_one(data)
            return user
        
        except HTTPException as e:
            raise HTTPException()
    
    async def get_user(self):
        try:
            users = DbManager().db[USERS].find().to_list()
            for user in users:
                user.pop('_id')
            if not users:
                logger.error("user details not found")
                raise HTTPException(status_code= 404 , detail= " User not found")  
            return users
        
        except HTTPException as e:
            raise HTTPException()
    
    async def get_user_by_email(self, email):
        try:
            user = DbManager().db[USERS].find_one({"email": email})
            if not user:
                logger.error("user details not found")
                raise HTTPException(status_code= 404 , detail= " User not found")
            return user
        
        except HTTPException as e:
            raise HTTPException()
    
    async def get_states(self , country_name):
        try :
            payload = {"country": country_name} 
            if not payload:
                logger.error("Country name required")
                raise HTTPException(status_code= 400 , detail= " Country name required")
            
            if payload == {"country": "Others"}:
                    state_names =''
                    return state_names

            response = requests.post(Config.STATES_LIST, json=payload)
            if response.status_code == 200:
                states = response.json().get('data', {}).get('states', [])
                state_names = [state['name'] for state in states]
                return state_names
            
            else:
                logger.error("Failed to fetch states")
        
        except HTTPException as e:
            raise HTTPException()