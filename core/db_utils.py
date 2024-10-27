import os
from pymongo import MongoClient
from dotenv import load_dotenv
from core.config import Config

class DbManager:
    def __init__(self):
        mongo_client = MongoClient(Config.CONNECTION_STRING)
        self.db = mongo_client[Config.DATABASE_NAME]

