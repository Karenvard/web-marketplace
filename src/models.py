from pydantic import BaseModel, validator
from typing import Optional
from fastapi import HTTPException
from datetime import datetime
import re


class SignupModel(BaseModel):
    email: str
    fullname: str
    password: str

    @validator("email")
    def validate_email(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Email is required.")
        elif (not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value)):
            raise HTTPException(status_code=400, detail="Email has not the valid format.")
        elif (len(value) > 50):
            raise HTTPException(status_code=400, detail="Email is too long.")
        return value
    
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
    

class SigninModel(BaseModel):
    email: str
    password: str
    remember_me: Optional[bool] = None

class PayloadModel(BaseModel):
    id: int
    email: str
    fullname: str


class UserModel(BaseModel):
    id: int
    fullname: str
    email: str
    basket_id: int
    seller_id: Optional[int] = None
    created: datetime


class createSellerModel(BaseModel):
    name: str
    description: str

    @validator("name")
    def validate_name(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Name is required.")
        elif (len(value) < 4):
            raise HTTPException(status_code=400, detail="Name is too short, must be at least 4.")
        elif (len(value) > 50):
            raise HTTPException(status_code=400, detail="Name is too long.")
        return value
    
    @validator("description")
    def validate_description(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Description is required.")
        elif (len(value) < 20):
            raise HTTPException(status_code=400, detail="Description is too short, must be at least 20.")
        elif (len(value) > 255):
            raise HTTPException(status_code=400, detail="Description is too long.")
        return value
    


class addProductModel(BaseModel):
    title: str
    description: str
    price: float
    type_id: int
    brand_id: int
    color_id: int

    @validator("title")
    def validate_title(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Title is required.")
        elif (len(value) < 3):
            raise HTTPException(status_code=400, detail="Title is too short, must be at least 3.")
        elif (len(value) > 50):
            raise HTTPException(status_code=400, detail="Title is too long.")
        return value
    
    @validator("description")
    def validate_description(cls, value: str) -> str:
        if not value:
            raise HTTPException(status_code=400, detail="Description is required.")
        elif (len(value) < 20):
            raise HTTPException(status_code=400, detail="Description is too short, must be at least 20.")
        elif (len(value) > 255):
            raise HTTPException(status_code=400, detail="Description is too long.")
        return value
    
    @validator("price")
    def validate_price(cls, value: float) -> float:
        if not value:
            raise HTTPException(status_code=400, detail="Price is required.")
        elif (value < 0):
            raise HTTPException(status_code=400, detail="Price cannot be negative.")
        return value
