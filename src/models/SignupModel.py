from pydantic import BaseModel, validator
from fastapi import HTTPException
import re

class SignupModel(BaseModel):
    username: str
    fullname: str
    password: str
    
    @validator("username")
    def validate_username(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Username is required.")
        elif (len(value) < 4):
            raise HTTPException(status_code=400, detail="Username is too short, must be at least 4.")
        elif (len(value) > 50):
            raise HTTPException(status_code=400, detail="Username is too long.")
        elif not re.match(r"^[a-zA-Z0-9]+$", value):
            raise HTTPException(status_code=400, detail="Username must contain only letters and numbers.")
        return value.lower()

    @validator("password")
    def validate_password(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Password is required.")
        elif (len(value) < 8):
            raise HTTPException(status_code=400, detail="Password is too short, must be at least 8.")
        elif (len(value) > 255):
            raise HTTPException(status_code=400, detail="Password is too long.")
        return value
    
    @validator("fullname")
    def validate_fullname(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Fullname is required.")
        elif (len(value) > 50):
            raise HTTPException(status_code=400, detail="Fullname is too long.")
        elif (len(value.split(" ")) != 2):
            raise HTTPException(status_code=400, detail="Fullname must contain first and last name, separated by a space.")
        return value.title()
 
