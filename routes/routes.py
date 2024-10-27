from models.models import UserIn
from services.services import UserService
from services.masters import Masterservice
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi import Header
from loguru import logger

from fastapi import APIRouter

app = APIRouter()
user_service = UserService()
master_service = Masterservice()

@app.post('/form')
async def donation_form(user_data: UserIn):
    try :
        data = await user_service.create_user(user_data)
        if not data:
            logger.error("unable to submit form")
            raise HTTPException(status_code= 400 , detail = "unable to submit donation form")
        
        return JSONResponse (
            status_code= 200,
            content= {
                "message": "Data submitted successfully"
                }
            )
    except HTTPException as e:
        raise HTTPException()

@app.get('/users')
async def get_users():
    user = await user_service.get_user()

    return user

@app.get('/countries')
async def get_countries():
    countries = await master_service.get_countries()
    return countries

@app.get('/states')
async def get_states(country_name):
    states = await user_service.get_states(country_name)
    return states













    
