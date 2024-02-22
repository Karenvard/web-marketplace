from pydantic import BaseModel

class SignupModel(BaseModel):
    username: str
    password: str