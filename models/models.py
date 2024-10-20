from pydantic import BaseModel , EmailStr
from typing import Optional

class UserIn(BaseModel):
    first_name :Optional[str]
    last_name :Optional[str]
    email : Optional [EmailStr]
    address : Optional[str]
