
from pydantic import BaseModel

class SigninDto(BaseModel):
    username: str
    password: str
    remember_me: bool
