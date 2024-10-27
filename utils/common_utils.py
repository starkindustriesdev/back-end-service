import uuid
import requests

def generate_user_id(prefix ='act'):
    user_id  = prefix + '-' + str(uuid.uuid4())[:8]
    return user_id 

