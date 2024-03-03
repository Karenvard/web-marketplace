from typing import Optional
from pydantic import BaseModel

class SigninModel(BaseModel):
    email: str
    password: str
    remember_me: Optional[bool] = False


