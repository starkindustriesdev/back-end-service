from fastapi import FastAPI
from routes.routes import app as user_app

app = FastAPI()

app.include_router(user_app)