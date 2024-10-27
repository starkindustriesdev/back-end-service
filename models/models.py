from pydantic import BaseModel , EmailStr
from typing import Optional
from utils.common_utils import generate_user_id

class UserIn(BaseModel):
    first_name :Optional[str]
    last_name :Optional[str]
    dob : Optional[str]
    email : Optional [EmailStr]
    country : Optional[str]
    state : Optional[str]
    city : Optional[str]
    pincode : Optional[int]
    address : Optional[str]

class UserOut(BaseModel):  
    user_id : Optional[str]
    first_name :Optional[str]
    last_name :Optional[str]
    dob : Optional[str]
    email : Optional [EmailStr]
    country : Optional[str]
    state : Optional[str]
    city : Optional[str]
    pincode : Optional[int]
    address : Optional[str]



