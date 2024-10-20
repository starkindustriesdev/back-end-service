import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

CONNECTION_STRING= os.getenv('CONNECTION_STRING')
DATABASE_NAME = os.getenv('DATABASE_NAME')

class DbManager:
    def __init__(self):
        mongo_client = MongoClient(CONNECTION_STRING)
        self.db = mongo_client[DATABASE_NAME]

