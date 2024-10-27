import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    CONNECTION_STRING = os.getenv('CONNECTION_STRING')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    STATES_LIST = os.getenv('STATES_LIST')