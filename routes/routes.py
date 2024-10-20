from models.models import UserIn
from services.services import UserService
from fastapi import APIRouter

app = APIRouter()
user_service = UserService()

@app.post('/form')
async def donation_form(user_data: UserIn):
    user = await user_service.create_user(user_data)
    return{"message":"Data submitted successfully"}

@app.get('/users')
async def get_users():
    user = await user_service.get_user()
    return user