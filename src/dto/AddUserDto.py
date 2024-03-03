from pydantic import BaseModel, validator
import re 

class AddUserDto(BaseModel):
    fullname: str
    username: str
    password: str

    @validator("fullname")
    def validate_fullname(cls, value: str) -> str:
        if not value:
            raise ValueError("Fullname is required.")
        elif (len(value) > 50):
            raise ValueError("Fullname is too long.")
        elif (len(value.split(" ")) != 2):
            raise ValueError("Fullname must contain first and last name, separated by a space.")
        return value.title()

    @validator("username")
    def validate_username(cls, value: str) -> str:
        if not value:
            raise ValueError("Username is required.")
        elif (len(value) < 4):
            raise ValueError("Username is too short, must be at least 4.")
        elif (len(value) > 50):
            raise ValueError("Username is too long.")
        elif not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError("Username must contain only letters and numbers.")
        return value.lower()

    @validator("password")
    def validate_password(cls, value: str) -> str:
        if not value:
            raise ValueError("Password is required.")
        elif (len(value) < 8):
            raise ValueError("Password is too short, must be at least 8.")
        elif (len(value) > 255):
            raise ValueError("Password is too long.")
        return value
